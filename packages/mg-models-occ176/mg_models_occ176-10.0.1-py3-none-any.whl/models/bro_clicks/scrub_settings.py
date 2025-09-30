from models.db import Db, pd
from threading import Lock
import datetime as dt


class ScrubSettings(Db):
    def __init__(self, db, version=1):
        v = ''
        if version > 1:
            v = f'_v{int(version)}'
        Db.__init__(self, db, f"bro_clicks", f'scrub_settings{v}')
        self.set_constraint(f'scrub_settings{v}_pk', (['crm_id'] if v else []) + ['offer_id', 'provider', 'affid'])
        self._version = version

    def get_setting(self, offer_id, provider, affid, as_type='dict', crm_id=None, **kwargs):
        df = self.get(
            where=f"""where offer_id='{offer_id}' and provider='{provider}' and affid='{affid}'
                        {f"and crm_id = '{crm_id}'" if self._version > 1 else ""}         
        """)
        if df is None or not len(df):
            offer_data = pd.read_sql(
                f"select default_scrub_ratio, default_scrub_percent,default_pp_percent from ui_54407332_offers.offers where offer_id= {offer_id}",
                self.engine)
            if len(offer_data):
                offer_data = offer_data.rename(
                    columns={'default_scrub_ratio': 'ratio', 'default_scrub_percent': 'pub_s1_pct',
                             'default_pp_percent': 'pp_pct'}).to_dict(orient='records')[0]
                offer_data['ratio'] = offer_data['ratio'].strip()
                try:
                    check = offer_data['ratio'].split(':')
                    x = int(check[0])
                    x = int(check[1])
                except:
                    offer_data.pop('ratio')
            else:
                offer_data = {}
            blacklist = self.engine.execute(
                f"""
                select provider, affid, is_blacklisted 
                from bro_clicks.pub_blacklist 
                where provider='{provider}' and affid='{affid}'

                """)
            try:
                blacklist = [dict(b) for b in blacklist]
                blacklist = blacklist[0]
            except:
                blacklist = {}
            payload = {'offer_id': offer_id, 'provider': provider, 'affid': affid, **offer_data, **blacklist}
            if self._version > 1:
                payload['crm_id'] = crm_id
            self.upsert([payload])
            df = self.get(
                where=f"""where offer_id='{offer_id}' and provider='{provider}' and affid='{affid}' 
                         {f"and crm_id = '{crm_id}'" if self._version > 1 else ""}
                        """)
        if as_type == 'dict':
            return df.to_dict(orient='records')[0]
        return df

    def increment_look_back(self, offer_id, provider, affid, crm_id=None, **kwargs):
        try:
            self.engine.execute(f""" update {self.schema}.{self.table} set look_back = look_back+1 
                                where offer_id='{offer_id}' 
                                    and provider='{provider}' 
                                    and affid='{affid}'
                                    and look_back <100
                                     {f"and crm_id = '{crm_id}'" if self._version > 1 else ""}
                                """)
        except Exception as e:
            print(e)

    def delete_pub(self, provider, affid, crm_id=None, **kw):
        self.engine.execute(f"""
            DELETE FROM {self.schema}.{self.table}
            WHERE provider= '{provider}' and affid='{affid}'
             {f"and crm_id = '{crm_id}'" if self._version > 1 else ""}
        """)

    def set_pub_blacklist(self, providers, affids, is_blacklisted, **kw):
        if not isinstance(providers, list) or not len(providers):
            return True
        con = self.engine.raw_connection()
        cur = con.cursor()
        ret = True
        try:
            cur.execute(f"""
            create temp table t_pubs on commit drop as ( select
                unnest(ARRAY{providers}::text[]) provider,
                 unnest(ARRAY{affids}::text[]) affid,
                  unnest(ARRAY{is_blacklisted}::bool[]) is_blacklisted
            ) 
            """)
            cur.execute(f"""
            update {self.schema}.{self.table} up
            set is_blacklisted = dn.is_blacklisted
            from t_pubs dn
            where dn.provider = up.provider and dn.affid = up.affid

            """)
            con.commit()
        except Exception as e:
            con.rollback()
            print(str(e))
            ret = False
        finally:
            cur.close()
            con.close()
        return ret


class PubBlacklist(Db):
    def __init__(self, db):
        Db.__init__(self, db, f"bro_clicks", 'pub_blacklist')
        self.set_constraint('pub_blacklist_pk', ['provider', 'affid'])


class ScrubSettingsV2(ScrubSettings):
    def __init__(self, db):
        ScrubSettings.__init__(self, db, 2)


class SubBlacklist(Db):
    _sublist = None
    _sub_lock = Lock()
    _last_update = dt.datetime.now()

    def __init__(self, db):
        Db.__init__(self, db, f"bro_clicks", 'sub_blacklist')
        self.set_constraint('sub_blacklist_pk', ['sub_affiliate'])
        if SubBlacklist._sublist is None:
            s = self.sublist

    @property
    def sublist(self):
        self._sub_lock.acquire()
        if SubBlacklist._sublist is None or self._last_update < dt.datetime.now() - dt.timedelta(minutes=3):
            try:
                SubBlacklist._sublist = self.get()
                SubBlacklist._last_update = dt.datetime.now()
            except Exception as e:
                print(str(e))
        self._sub_lock.release()
        return self._sublist

    def add(self, sub_affiliate):
        self._sub_lock.acquire()
        try:
            if not len(self._sublist.loc[self._sublist.sub_affiliate == sub_affiliate]):
                SubBlacklist._sublist = SubBlacklist._sublist.append(
                    pd.Series({'sub_affiliate': sub_affiliate, 'is_blacklisted': False, 'enable_fraud_checks': False}),
                    ignore_index=True)
                self.insert({'sub_affiliate': sub_affiliate}, return_id=True)
        except Exception as e:
            print(str(e))
        self._sub_lock.release()

    def delete_sub(self, sub_affiliate):
        self.delete('sub_affiliate', sub_affiliate)

    def is_blacklisted(self, sub_affiliate, **kw):
        sub_l = self.sublist.copy()
        msk = sub_l.sub_affiliate == sub_affiliate
        if not len(sub_l.loc[msk]):
            self.add(sub_affiliate)
            return False
        return bool(len(sub_l.loc[(msk) & (sub_l.is_blacklisted)]))

    def get_sub(self, sub_affiliate):
        sub_l = self.sublist.copy()
        sub_l = sub_l.loc[sub_l.sub_affiliate == sub_affiliate]
        if len(sub_l):
            return sub_l[['is_blacklisted', 'scrub_all', 'enable_fraud_checks']].to_dict(orient='records')[0]
        else:
            self.add(sub_affiliate)
        return {'is_blacklisted': False, 'scrub_all': False, 'enable_fraud_checks': False}
