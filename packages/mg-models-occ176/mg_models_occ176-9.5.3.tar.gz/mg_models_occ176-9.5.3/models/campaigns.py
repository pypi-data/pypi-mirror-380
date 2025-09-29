import pandas as pd
import warnings
import json
from models.db import OfferStructure
from DataFactory.sqlinterface import Session
from models import api

# Pandas Settings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 4000)
pd.set_option('display.width', 3000)


class Campaigns(OfferStructure):
    def __init__(self, db, account_id='54407332'):
        OfferStructure.__init__(self, db, 'campaigns', account_id)
        self.set_constraint('campaigns_pk', ['campaign_id', 'crm_id'])

    def Get(self, crm_id=None, columns=False, where='', orderBy=False,**kw):
        if crm_id:
            if where == '':
                where = f" where crm_id = '{crm_id}' "
            else:
                where += f" and crm_id = '{crm_id}' "

        df = self.get(columns, where, orderBy)
        # Set types explicitly

        df['campaign_id'] = df['campaign_id'].astype(int)
        if 'rebill_period' in df.columns:
            df['rebill_period'] = df['rebill_period'].astype(int)
        if 'trial_period' in df.columns:
            df['trial_period'] = df['trial_period'].astype(int)
        return df.set_index('campaign_id', drop=False).fillna("")

    def delete(self, crm_id, campaign_id):
        self.engine.execute(f""" delete from {self.schema}.{self.table} where crm_id = '{crm_id}' and campaign_id='{int(campaign_id)}'""")

    def get_campaigns_list(self, crm_id, exclude=False):
        w = f" Where crm_id = '{crm_id}' "
        if exclude:
            w += " and campaign_id not in({excl})".format(excl=",".join([str(c) for c in exclude]))
        campaign_list = self.get(
            ['campaign_id', 'campaign_name'],

            where=w,
            orderBy='campaign_id desc').rename({'campaign_name': 'text', 'campaign_id': 'value'}, axis=1)
        campaign_list['key'] = campaign_list['value']

        return campaign_list

    def get_campaigns_list_ui(self, crm_ids=False, crm_sorted=False,exclude=False,  **kw):
        campaign_list = self.get(['campaign_id', 'campaign_name', 'crm_id'],
        where = f"where crm_id = ANY(ARRAY{crm_ids})" if crm_ids else False,
        orderBy='campaign_id desc').rename({'campaign_name': 'text', 'campaign_id': 'value'}, axis=1)
        campaign_list['key'] = campaign_list['value']
        campaign_list['text'] = campaign_list['value'].astype(str) + ' - ' + campaign_list['text']
        if crm_sorted:
            return {c: campaign_list.loc[campaign_list.crm_id == c].drop(columns='crm_id').to_dict(orient='records')
                    for c in campaign_list.crm_id.unique().tolist()}
        return campaign_list.drop(columns='crm_id')

    def unique_update(self, payload, warn):
        payload = payload.loc[payload.campaign_id.astype(int) > 0]
        if warn:
            lst = payload.campaign_id.astype(str).tolist()
            mlst = payload.astype(str).master_id.tolist()
            crmlst = payload.astype(str).crm_id.tolist()
            qry= """
                SELECT offer_id, master_id from {sch}.{tbl}
                WHERE master_id not in({m}) and campaign_id in({c}) and crm_id = '{crm}'
            """.format(m=",".join(mlst), c=",".join(lst), crm=str(crmlst[0]), tbl=self.table, sch=self.schema)
            offids = ''
            count = 0
            for q in self.engine.execute(qry):
                count += 1
                offids += str(q[0])+' '
            if count:
                return api.Response().fail(290).data({'warn': 'You are about to re-assign campaigns to this offer and provider that are already assigned to offers {o}.You should review this carefully, and reassign the campaigns on the other provider/offer if necessary. If these campaigns are still used on another offer it can mess stuff up.'.format(o=offids)})

        self.engine.execute(
            "UPDATE {}.{} set master_id=null, offer_id=null where offer_id = '{}' and provider='{}' and crm_id='{}'".format(self.schema, self.table,
                payload.iloc[0].offer_id, payload.iloc[0].provider, crmlst[0]))
        return self.upsert(payload)

    def assoc_offer_globals_x(self, globs, offer_id):
        payload = []
        for c in globs.rebill_campaign.tolist():
            payload.append({'class': 'rebill', 'offer_id': offer_id, 'campaign_id': c})
        for c in globs.saves_campaign.tolist():
            payload.append(
                {'class': 'saves', 'offer_id': offer_id, 'campaign_id': c})
        return self.upsert(pd.DataFrame(payload))

    def assoc_offer_globals(self, globs, offer_id, camp_cols,  **kwargs):
        payload = []
        msk = globs.is_upsell > 0
        g_ups = globs.loc[msk]
        df_payload = globs.loc[~msk]
        if len(g_ups):
            df_payload.is_upsell = g_ups.is_upsell.max()

        for v in df_payload.to_dict(orient='records'):
            for c in camp_cols:
                if v[c]  ==  ''  or v[c] == pd.np.nan or v[c] == None:
                    continue
                payload.append({**{
                     'class': c.split('_')[1] if c == 'bin_block_campaign' else c.split('_')[0],
                     'offer_id': offer_id,
                     'campaign_id': v[c],
                     'step': v['step'],
                     'crm_id': v['crm_id'],
                     'is_upsell': v['is_upsell'],
                     'provider': 'ALL'},
                      **kwargs})

        return self.upsert(pd.DataFrame(payload), check_cols=True)

