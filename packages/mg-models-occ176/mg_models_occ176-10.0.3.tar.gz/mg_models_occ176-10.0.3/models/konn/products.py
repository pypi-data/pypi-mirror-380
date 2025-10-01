from models.konn.kk_struc import KKStruc, np, pd


class Products(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'products')
        self.set_constraint('product_id_pk', ['product_id', 'campaign_product_id'])

    def format_data(self, df, format_col_names=True):
        res = Products._sub_mod_from_array_col(df, 'products', 'campaignId').replace(r'^\s*$', np.nan, regex=True)
        if format_col_names:
            return self.format_col_names(res)
        return res