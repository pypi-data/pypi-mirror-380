from models.db import OfferStructure, pd


class MasterCampaigns(OfferStructure):
    def __init__(self, db, account_id):
        OfferStructure.__init__(self, db,  'master_campaigns', account_id)
        self.set_constraint('masters_campaigns_pk', ['provider', 'offer_id', 'step', 'crm_id'])

    def get_provider_campaign(self, provider, offer_id, crm_id, **kwargs):
        df =  pd.read_sql(f""" select a.use_provider, b.campaign_id
                                from {self.schema}.{self.table} a 
                                left join {self.schema}.campaigns b on a.master_id = b.master_id 
                                                        and a.provider=b.provider 
                                                        and a.offer_id=b.offer_id
                                                        and a.crm_id=b.crm_id
                                                        and b.class = 'provider'
                                where a.provider='{provider}' 
                                        and a.offer_id={offer_id} and a.crm_id = '{crm_id}' 
                            
                            """, self.engine)
        return df