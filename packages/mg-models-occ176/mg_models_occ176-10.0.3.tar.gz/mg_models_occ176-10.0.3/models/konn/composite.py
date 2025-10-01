from models.konn.kk_struc import KKStruc, np, pd


class Composite(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'composite')
        self.set_constraint('composite_pk', ['transaction_id'])
        self.crm_id = crm_id

    def format_data(self, df, format_col_names=True, drop=[]):
        _df = self.format_ts_offset(df)
        _df = _df.drop(columns=['tItems', 'notes', 'oItems', 'fItems'] + drop).replace(r'^\s*$', np.nan, regex=True)
        if 'merchantId' in _df.columns:
            _df['merchantId'] = _df['merchantId'].fillna(0).astype(int)
            ln = len(_df.loc[_df.merchantId.isna()])
            if ln:
                print(f'{ln} null merchant ids')

        if format_col_names:
            return self.format_col_names(_df)
        return _df

    def global_update(self, df):
        up = df[list(self._col_map.keys())].rename(columns=self._col_map)
        up['crm_id'] = self.crm_id
        up['amount_refunded_to_date'] = up['refund_amount']
        up['void_amount'] = '0.00'
        up['order_sales_tax_amount'] = up['order_sales_tax']
        up.loc[up.is_void == 1, 'void_amount'] = up.loc[up.is_void == 1, 'refund_amount']
        self.update(df, ['order_id', 'crm_id'])
