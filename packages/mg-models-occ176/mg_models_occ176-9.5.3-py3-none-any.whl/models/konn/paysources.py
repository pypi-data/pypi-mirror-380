from models.db import Db, np


class PaySources(Db):
    def __init__(self, db, crm_index=1):
        Db.__init__(self, db, f'crm_kk_{str(crm_index)}', 'pay_sources')
        # self.set_constraint('', [''])

    @staticmethod
    def format_data(df):
        return PaySources._sub_mod_from_array_col(df, 'paySources', 'customerId').replace(r'^\s*$', np.nan, regex=True).drop_duplicates(subset=['customerId', 'paySourceId'])