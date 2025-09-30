from models.konn.kk_struc import KKStruc, np, pd


class Customers(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'customers')
        self.set_constraint('customers_pk', ['customer_id'])
        self.int_cols = ['bill_ship_same', 'source_id', 'pay_source_id', 'customer_id']

    def format_data(self, df, format_col_names=True):
        _df = self.format_ts_offset(df)
        _df = _df.drop(columns=['paySources', 'notes'], errors='ignore').replace(r'^\s*$', np.nan, regex=True)


        # the values are not reset until the recurring date is set (Not Here).

        if format_col_names:
            return self.format_col_names(_df)
        return _df

    def global_update(self, df):
        return


class History(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'customers')
        self.set_constraint('customers_pk', ['customer_id'])
        self.int_cols = ['bill_ship_same', 'source_id', 'pay_source_id', 'customer_id']

    @staticmethod
    def format_cancels(df):
        if not len(df):
            return pd.DataFrame()

        if isinstance(df, list):
            df = pd.DataFrame(df)
        df = df.loc[df.categoryType.isin(('ORDER_CANCELLED',))]
        # df.loc[df.status !=]
        if not len(df):
            return pd.DataFrame()
        df['orderId'] = np.nan
        f_canc_msk = df.message.str.contains('fulfillment for order', case=False)
        if len(df.loc[f_canc_msk]):
            df.loc[f_canc_msk, ['orderId']] = df.loc[f_canc_msk].message.apply(lambda x: x.split(' ')[3].strip())
        if len(df.loc[~f_canc_msk]):
            df.loc[~f_canc_msk, ['orderId']] = df.loc[~f_canc_msk].message.apply(lambda x: x.split('#')[1].split(' ')[0].strip())
        if len(df.loc[(df.orderId.isna()) | (df.orderId == '')]):
            print(df)
        return df[['orderId', 'categoryType']]
