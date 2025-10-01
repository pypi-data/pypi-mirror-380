from models.konn.kk_struc import KKStruc, np ,pd


class Orders(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'orders')
        self.set_constraint('orders_pk', ['order_id'])
        self.col_map = {
            'agentUserId': 'created_by_user_name',
            'cardExpiryDate': 'cc_expires',
            'shipProfileId': 'shipping_id',
            'shipCity': 'shipping_city',
            'shipCountry': 'shipping_country',
            'shipFirstName': 'shipping_first_name',
            'shipLastName': 'shipping_last_name',
            'shipPostalCode': 'shipping_postcode',
            'shipState': 'shipping_state',
            'shipAddress1': 'shipping_street_address',
            'shipAddress2': 'shipping_street_address2',
            'ipAddress': 'ip_address',
            'salesTax': 'order_sales_tax_amount',
            'reviewStatus': 'order_confirmed',
            'cardIsPrepaid': 'prepaid_match',
            'hasUpsell': 'is_upsell',
            'orderId': 'native_order_id',
            'orderStatus': 'order_status'
        }
        self.int_cols = ['agent_user_id', 'card_is_debit', 'campaign_id', 'customer_id', 'card_is_prepaid', 'is_decline_save', 'source_id']

    def format_data(self, df, format_col_names=True, drop=[]):
        _df = self.format_ts_offset(df)
        _df = _df.drop(columns=['fulfillments', 'items'] + drop, errors='ignore').replace(r'^\s*$', np.nan, regex=True)
        if format_col_names:
            return self.format_col_names(_df)
        return _df

    def global_update(self, df):
        up = df
        up['crm_id'] = self._crm_id
        keys = ['native_order_id', 'product_id', 'crm_id']
        up.order_status = up.order_status.replace({'CANCELLED': '5', 'REFUNDED': '6', 'DECLINED': '7', 'PARTIAL': '0', 'COMPLETE': '2'}).astype(int)
        self.update(up.loc[up.order_status != 'PARTIAL'].drop('order_status', axis=1), keys)
        self.update(up.loc[up.order_status != 'PARTIAL', ['order_status']+keys], keys, where='order_status is null OR order_status <6')
