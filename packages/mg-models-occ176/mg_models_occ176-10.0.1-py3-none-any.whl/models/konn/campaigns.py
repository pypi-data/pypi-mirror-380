from models.db import Db, np


class Campaigns(Db):
    def __init__(self, db, crm_index=1):
        Db.__init__(self, db, f'crm_kk_{str(crm_index)}', 'campaigns')
        self.set_constraint('campaigns_pk', ['campaignId'])

    @staticmethod
    def format_data(df):
        return df.drop(columns=['countries', 'products', 'taxes', 'coupons', 'shipProfiles']).replace(r'^\s*$', np.nan, regex=True)




