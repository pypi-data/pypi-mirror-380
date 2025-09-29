from models.db import OfferStructure, err, api
import pandas as pd
import numpy as np
from threading import Thread, Lock


class OfferGlobals(OfferStructure):
    def __init__(self, db, account_id='54407332'):
        OfferStructure.__init__(self, db, 'offer_globals', account_id)
        self.set_constraint('offer_globals_pk', ['offer_id', 'step', 'crm_id'])

    def _check_input(self, payload, camp_cols):
        lst = []
        for c in camp_cols:
            lst += (payload.loc[payload.is_upsell.replace({'', np.nan}).fillna(0).astype(int) == 0, c].astype(str).tolist())
        #print(len(set(lst)), len(lst))
        return len(set(lst)) < len(lst)

    def _check_unique(self, payload, camp_cols, crm_id):
        lst = []
        col_map = {'saves_campaign': 1, 'rebill_campaign': 2, 'prepaid_campaign': 3, 'bin_block_campaign': 4, 'provider_campaign': 5}
        for c in camp_cols:
            lst += payload[c].astype(str).replace({'': pd.np.nan}).dropna().tolist()
        qry = """select offer_id,saves_campaign,rebill_campaign,prepaid_campaign, bin_block_campaign,provider_campaign  from {sch}.{tbl} 
                                         where (saves_campaign in({ls}) or rebill_campaign in({ls}) or prepaid_campaign in({ls}))
                                         and crm_id = '{crm}'
                                       """.format(ls=",".join(list(set(lst))), sch=self.schema, tbl=self.table, crm=crm_id)
        q = self.engine.execute(qry)
        count = 0
        for r in q:
            for c in camp_cols:
                if not (len(payload.loc[(payload.offer_id.astype(int) == r[0]) &
                                       (payload[c] == r[col_map[c]])]) or r[col_map[c]] is None):
                    count += 1
                    break
        return count

    def campaigns_have_sales_crm(self, offer_id, crm_id):
        return pd.read_sql(f"""Select d.campaign_id,  count(*) as order_count from {self.schema}.{self.table} as a
                    INNER JOIN {self.schema}.offer_globals as b on a.offer_id = b.offer_id
                    INNER JOIN {self.schema}.campaigns as c on b.rebill_campaign = c.campaign_id or  b.saves_campaign = c.campaign_id
                    INNER JOIN (select campaign_id from crm_global.orders where crm_id= '{crm_id}') as d on d.campaign_id = c.campaign_id 
                  WHERE a.offer_id = {offer_id}
                  GROUP BY d.campaign_id
                
                   """, self.engine)

    def campaigns_have_sales(self, offer_id, crms):
        threads = []
        df = None
        df_lock = Lock()

        def _get(off_id, crm):
            nonlocal df, df_lock
            _res = self.campaigns_have_sales_crm(off_id, crm)
            df_lock.acquire()
            if df is None:
                df = _res
            else:
                df = df.append(_res)
            df_lock.release()
        for c in crms:
            threads.append(Thread(target=_get, args=(offer_id, c)))
            threads[len(threads)-1].start()
        for t in threads:
            t.join()
        return df

    def unique_update(self, payload, camp_cols, crm_id):
        if self._check_input(payload, camp_cols):
            return api.Response().fail(290).data({'error_display': 'Campaigns must be unique.'})

        count = self._check_unique(payload, camp_cols, crm_id)
        if count:
            return api.Response().fail(290).data(
                {'error_display': str(count) + ' of the campaigns you tried to define are already in use by another offer.'})
        res = self.upsert(payload, check_cols=True)
        if not res.success():
            try:
                if isinstance(res.msg()['data']['exception'], err.UniqueViolation):
                    res.data({'error_display': 'One or More of the Campaigns defined is already in Use by another offer.'})
            except:
                pass
        return res

    def unique_insert(self, payload):
            if self._check_input(payload):
                return api.Response().fail(290).data({'error_display': 'Campaigns must be unique.'})

            count = self._check_unique(payload)
            if count:
                return api.Response().fail(290).data({'error_display': str(count)+' of the campaigns you tried to define are already in use by another offer.'})
            res = self.insert(payload.to_dict(orient='records'))
            if not res.success():
                try:
                    if isinstance(res.msg()['data']['exception'], err.UniqueViolation):
                        res.data({'error_display': 'One or More of the Campaigns defined is already in Use by another offer.'})
                except:
                    pass
            return res