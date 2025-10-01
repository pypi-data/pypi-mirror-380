from models.db import OfferStructure, pd


class BillingModels(OfferStructure):
    def __init__(self, db, account_id):
        OfferStructure.__init__(self, db, 'billing_models', account_id)
        self.set_constraint('billing_models_pk', ['crm_id', 'id'])

    @staticmethod
    def get_internal_type(offer_type):
        if offer_type == 'ssc':
            return 'internal_cont'
        return 'internal_one_x'

    def get_default(self, offer_type, as_type='dict'):
        ret = self.get(where=f" where internal_type = '{self.get_internal_type(offer_type)}'")
        if as_type == 'dict':
            ret = ret.to_dict(orient='records')[0]
        return ret
