from models.konn.kk_struc import KKStruc, np, pd


class TransactionItems(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'transaction_items')
        self.set_constraint('transaction_items_pk', ['transaction_id', 'product_id'])
        self._int_cols = ['quantity', 'product_id', 'customer_id', 'transaction_id']

    def format_data(self, df, format_col_names=True):
        if not len(df):
            return df
        try:
            t = TransactionItems._sub_mod_from_array_col(
                    df, 'tItems', ['customerId', 'transactionId'])

        except KeyError:
            t = TransactionItems._sub_mod_from_array_col(
                df, 'items', ['customerId', 'transactionId'])

        t = t.replace(r'^\s*$', np.nan, regex=True)
        t = self.format_ts_offset(t)
        if format_col_names:
            return self.format_col_names(t)
        return t

    def global_update(self, df):
        up = df[list(self._col_map.keys())].rename(columns=self._col_map)
        for c in ['on_hold', 'is_rma']:
            up[c] = 0
        up['crm_id'] = self._crm_id
        up['order_status'] = up.order_status.fillna(0).astype(str).replace(
            {'0.0': '0', 'CANCELLED': '5', 'SHIPPED': '8', 'DELIVERED': '9', 'PENDING': '11', 'PENDING_SHIPMENT': '11', 'HOLD': '1',  'FAILED': '12',
             'RMA': '13', 'RETURNED': '14', 'RECYCLE_FAILED': '0',
             }).astype(int)
        up['on_hold'] = ((up.order_status == 1) | (up.order_status == 6)).astype(int)
        up.loc['is_rma'] = (up.order_status == 2).astype(int)
        self.update(df.loc[df.order_status != 0], ['order_id', 'crm_id'])
        self.update(df.loc[df.order_status == 0].drop('order_status', axis=1), ['order_id', 'crm_id'])
