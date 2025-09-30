from models.db import Db, np


class FulfillmentItems(Db):
    def __init__(self, db, crm_index=1):
        Db.__init__(self, db, f'crm_kk_{str(crm_index)}', 'fullfillment_items')
        # self.set_constraint('', [''])

    @staticmethod
    def format_data(df):
        return FulfillmentItems._sub_mod_from_array_col(
            df, 'fItems', ['customerId', 'transactionId']).replace(
            r'^\s*$', np.nan, regex=True)