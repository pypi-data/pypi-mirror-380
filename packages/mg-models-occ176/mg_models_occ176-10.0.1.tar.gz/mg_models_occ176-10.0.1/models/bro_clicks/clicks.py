from models.db import Db, pd
import json

class Clicks(Db):
    _static_columns = None

    def __init__(self, db):
        Db.__init__(self, db, f"bro_clicks", 'clicks')
        self.set_constraint('clicks_pk', ['provider', 'click_id', 'page', 'event'])

    @property
    def static_columns(self):
        if not Clicks._static_columns:
            Clicks._static_columns = self.columns()
        return Clicks._static_columns

    @staticmethod
    def provider_aff_part(provider, affid=False):
        return f""" provider = '{provider}' {f"and affid = '{affid}'" if affid else '' }"""

    def _get_event_inc(self, provider, click_id, page, event, **kwargs):
        try:
            inc = self.engine.execute(f"""select e_inc from {self.schema}.{self.table} 
                                where provider = '{provider}' 
                                and click_id = '{click_id}' 
                                and page = '{page}'
                                and event = '{event}'
                                """).scalar()
        except Exception as e:
            print('Click Inc error:', click_id, provider, page, str(e))
            return 1
        return inc + 1 if inc else 1

    def set_event(self, event):
        if 'ip' in event:
            _e = event.pop('ip')
            if 'ip_address' not in event:
                event['ip_address'] = _e
        ne = {}
        s_cols = self.static_columns
        for k, v in event.items():
            if k in s_cols:
                ne[k] = str(v).replace('%', '') if k != 'event_data' else v
        event = ne
        if 'event_data' in event:
            event['event_data'] = json.dumps(json.loads(json.dumps(event['event_data']))).replace('%', '')
        event['e_inc'] = self._get_event_inc(**event)
        if 'api_key' in event:
            event.pop('api_key')
        if 'crm_id' in event:
            event.pop('crm_id')
        return self.insert(event, return_id='click_id')

    def clicks_per_min(self, look_back_min, provider, now, affid=False, distinct=True, ):
        val = self.engine.execute(f"""Select  count({'distinct(click_id)' if distinct else 'click_id'}) / {look_back_min}::numeric 
                From {self.schema}.{self.table} 
                WHERE {self.provider_aff_part(provider, affid)}
                AND time_stamp >= '{now}'::timestamp -  INTERVAL '{look_back_min} minutes' and is_network_referred is true 
            """).scalar()
        return val if val else 0

    def click_count_page(self, start_date, end_date, crm_id='all'):
        if crm_id != 'all' and not isinstance(crm_id, list):
            crm_id = [crm_id]
        return pd.read_sql(f"""
            SELECT offer_id, provider, affid, page, event,
                    count(distinct(ip_address)) unique_ip_access_count,
                    count(distinct(click_id)) as click_count,
                    count(click_id) as event_count,
                    sum(e_inc) as ha_click_count        
            from {self.schema}.{self.table} 
            where time_stamp::date >= '{start_date}'::date and time_stamp::date <= '{end_date}'::date and is_network_referred is true
                 {f" and crm_id = ANY(ARRAY{crm_id})" if crm_id != 'all' else ""}
            group by offer_id, provider, affid, page, event           
            
        """, self.engine)

    def click_count(self, start_date, end_date, crm_id='all'):
        if crm_id != 'all' and not isinstance(crm_id, list):
            crm_id = [crm_id]
        return pd.read_sql(f"""
            SELECT offer_id, provider, affid,
                    count(distinct(ip_address)) unique_ip_access_count,
                    count(distinct(click_id)) as click_count,
                    count(click_id) as event_count,
                    sum(e_inc) as ha_click_count        
            from {self.schema}.{self.table} 
            where time_stamp::date >= '{start_date}'::date and time_stamp::date <= '{end_date}'::date and is_network_referred is true
                 {f" and crm_id = ANY(ARRAY{crm_id})" if crm_id != 'all' else ""}
            group by offer_id, provider, affid         

        """, self.engine)


class CallCounter(Db):
    def __init__(self, db):
        Db.__init__(self, db, "public", 'cc')

