from models.konn.kk_struc import KKStruc, np, pd


class OrderItems(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'order_items')
        self.set_constraint('order_id', ['order_id', 'product_id'])

    def format_data(self, df, format_col_names=True):
        try:
            res = OrderItems._sub_mod_from_array_col(
                df, 'oItems', 'transactionId')
        except KeyError:
            res = OrderItems._sub_mod_from_dict_col(
                df, 'items', 'orderId', orient='nested')
        res = res.replace(r'^\s*$', np.nan, regex=True)
        res = self.format_ts_offset(res)
        if format_col_names:
            return self.format_col_names(res)
        return res

    def global_update(self, df):
        self._global_update(df, ['order_id', 'product_id', 'crm_id'])
