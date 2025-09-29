from models.db import Db, pd, np


class CustomShipShipped(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'custom_shipping', 'shipped')
        self.set_constraint('campaigns_pkey', ['crm_id', 'email_address'])


class CustomShipCampaigns(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'custom_shipping', 'campaigns')
        self.set_constraint('shipped_pkey', ['custom_shipping_id'])
