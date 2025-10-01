from models.konn.kk_struc import KKStruc, np, pd


class Transactions(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'transactions')
        self.set_constraint('transactions_pk', ['transaction_id'])
        self.crm_id = crm_id
        self._col_map = {
            'affId': 'affid',
            'merchantDescriptor': 'gateway_descriptor',
            'chargebackDate': 'chargeback_date',
            'transactionId': 'order_id',
            'authCode': 'auth_id',
            'city': 'billing_city',
            'country': 'billing_country',
            'billingCycleNumber': 'billing_cycle',
            'firstName': 'billing_first_name',
            'lastName': 'billing_last_name',
            'midNumber': 'processor_id',
            'postalCode': 'billing_postcode',
            'state': 'billing_state',
            'address1': 'billing_street_address',
            'address2': 'billing_street_address2',
            'campaignId': 'campaign_id',
            'cardBin': 'cc_first_6',
            'cardLast4': 'cc_last_4',
            'cardType': 'cc_type',
            'achAccountNumber': 'check_account_last_4',
            'achRoutingNumber': 'check_routing_last_4',
            'customerId': 'customer_id',
            'phoneNumber': 'customers_telephone',
            'responseText': 'decline_reason',
            'emailAddress': 'email_address',
            'merchantId': 'gateway_id',
            'dateCreated': 'time_stamp',
            'merchantTxnId': 'transaction_id',
            'orderId': 'native_order_id',

        }
        self.int_cols = ['billing_cycle_number', 'transaction_id', 'is_chargedback','merchant_id']

    def global_update(self, df):
        up = df[list(self._col_map.keys())].rename(columns=self._col_map)
        for c in ['is_void', 'is_refund', 'is_test_cc',]:
            up[c] = 0
        up['crm_id'] = self.crm_id
        up['is_test_cc'] = (up['cc_type'] == 'TESTCARD').astype(int)

        self.update(up, ['order_id', 'crm_id'])