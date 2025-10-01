from models.db import OfferStructure, pd


class Offers(OfferStructure):

    def __init__(self, db,  account_id='54407332'):
        OfferStructure.__init__(self, db, 'offers', account_id)
        self.set_constraint('offers_pk', ['offer_id'])

    def alt_payment_router(self):
        return pd.read_sql(
            f"""
               select 
                       d.crm_id,
                       a.offer_id::int,                      
                       d.campaign_id::int,
                       a.name,                
                       d.campaign_name,
                       b.step::int,
                       b.main_product_id,
                       b.trial_product_id,
                       b.charge_product_id::int,
                       b.rebill_product_id::int,
                       b.mb_campaign,
                       case when b.mb_campaign is not null then b.mb_campaign::int else b.rebill_campaign::int end as rebill_campaign,                    
                       b.saves_campaign::int,
                       b.rebill_shipping_id::int,
                       b.charge_shipping_id::int,
                       b.crm_offer_id,
                       b.crm_billing_model_id,
                       b.is_rebill,
                       b.trial_period,
                       b.rebill_period                      
                                   
                       
               from {self.schema}.{self.table} as a
                         LEFT Join {self.schema}.offer_globals as b on a.offer_id = b.offer_id
                         LEFT Join {self.schema}.campaigns as d on b.crm_id = d.crm_id and ((d.step = b.step and b.offer_id = d.offer_id) or 
                                                                  (b.rebill_campaign = d.campaign_id or 
                                                                    b.saves_campaign = d.campaign_id or
                                                                    d.campaign_id = b.mb_campaign or 
                                                                    d.campaign_id = b.provider_campaign or
                                                                    d.campaign_id = b.prepaid_campaign or
                                                                    d.campaign_id = b.bin_block_campaign))
                         --LEFT Join {self.schema}.campaigns as e on b.crm_id = e.crm_id and b.motball_campaign = e.campaign_id                                         
            """,
            self.engine
        )
