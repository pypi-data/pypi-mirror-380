from models.db import Db, pd


class CampaignBalancer(Db):
    def __init__(self, db):
        Db.__init__(self, db, f"bro_clicks", 'campaign_balancer')
        self.set_constraint('campaign_balancer_pk', ['date', 'offer_id', 'crm_id'])
