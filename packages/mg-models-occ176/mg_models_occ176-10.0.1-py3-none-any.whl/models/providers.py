from models.db import OfferStructure


class Providers(OfferStructure):
    def __init__(self, db, account_id):
        OfferStructure.__init__(self, db, 'providers', account_id)
        self.set_constraint('providers_pk', ['provider_id', 'provider_name'])