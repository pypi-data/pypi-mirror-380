import pandas as pd
from models.order_cycles import OrderCycles, Db, np, Session
from models.orders import Orders


class InitialsRt(Db):
    _cm = {'dateCreated': 'time_stamp', 'customerId': 'customer_id', 'orderId': 'native_order_id'}
    _cols = ['order_id', 'time_stamp',  'native_order_id',
             'billing_first_name', 'billing_last_name', 'billing_street_address', 'billing_street_address2',
             'billing_city', 'billing_country', 'billing_state', 'billing_postcode',
             'shipping_first_name', 'shipping_last_name', 'shipping_street_address', 'shipping_street_address2',
             'shipping_city', 'shipping_country', 'shipping_state', 'shipping_postcode',
             'email_address', 'ip_address', 'gateway_id', 'customers_telephone', 'cc_expires', 'cc_type',
            # 'custom1', 'custom2', 'custom3', 'custom4', 'custom5'

             ]

    def __init__(self, db, crm_id,  account_id='54407332'):
        Db.__init__(self, db, 'processing', 'initials_rt')
        self.set_constraint('initials_rt_pk', ['crm_id', 'order_id'])
        self._crm_id = crm_id
        self._account_id = account_id
        self.oc = OrderCycles(db, crm_id, account_id)
        self.ord = Orders(db, crm_id)

    @staticmethod
    def translate(df):
        return df.rename(columns=InitialsRt._cm)

    def get_window(self, s_dt, e_dt, return_type='result'):
        return self.get(where=f" where time_stamp >='{s_dt}' and time_stamp <='{e_dt}' and crm_id='{self._crm_id}'", return_type=return_type)

    def get_confirmations(self, max_time):
        tsq = f"and time_stamp > now() - Interval '2 Days' and time_stamp <= '{max_time}'"
        qry = f"""
                select a.* from({self.ord.get(['crm_id', 'order_id', 'native_order_id', 'order_confirmed'], 
                                        where=f" where is_recurring = 1  {tsq} and order_confirmed is null", return_type="query")}) a
                inner join ({self.oc.get(['crm_id', 'order_id', 'bc_inferred'], 
                                             where=f"where bc_inferred=0 and decline_reason is null {tsq} ",return_type='query')}) b
                on b.order_id = a.order_id and b.crm_id = a.crm_id
                where a.crm_id = '{self._crm_id}'
        """

        return pd.read_sql(qry, self.engine)

    def get_order(self, order_id):
        return self.ord.get(InitialsRt._cols+['main_product_id'], where=f"where order_id = {order_id} and crm_id='{self._crm_id}'")


class InitialsAlerts(Db):

    def __init__(self, db, account_id='54407332'):
        Db.__init__(self, db, 'processing', 'initials_alerted')
        self.set_constraint('initials_alerted_pk', ['crm_id', 'order_id'])
        self._account_id = account_id

