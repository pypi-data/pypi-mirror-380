from models.db import Db, pd, np
from models.konn.products import Products
import re
from threading import Thread, Lock
import datetime as dt
from models.offers import Offers
from models.offer_globals import OfferGlobals
#from models.internal_orders import InternalOrders


class Hybrid(Db):
    def __init__(self, db, crm_id, is_continuity_model=False):
        Db.__init__(self, db, f'crm_global', 'orders')
        self.set_constraint('orders_pk', ['order_id', 'crm_id', 'month_date'])
        self.is_continuity_model = is_continuity_model
        self._index = {}
        self.offers = Offers(db, '54407332').get(['offer_id', 'offer_type']).merge(
            OfferGlobals(db, '54407332').get(where=f" where crm_id= '{crm_id}'"),
            on='offer_id'
        )
        self._rs_lock = Lock()
        self._cancel_sync_err = ""
        self._cb_sync_err = ""
        #self._internal = InternalOrders(db, crm_id)

        self.crm_id = crm_id

        self._used_tran = False

        self._used_ord = False

        self._used_ti = False

        self._used_oi = False

        self._used_comp = False

        self._comp_map = {
            'orderId': 'native_order_id',
            'affId': 'affid',
            'agentUserId': 'created_by_user_name',
            'transactionId': 'order_id',
            'dateUpdated': 'last_modified',
            'billingCycleNumber': 'billing_cycle',
            'authCode': 'auth_id',
            'isChargedback': 'is_chargeback',
            'city': 'billing_city',
            'country': 'billing_country',
            'firstName': 'billing_first_name',
            'lastName': 'billing_last_name',
            'postalCode': 'billing_postcode',
            'state': 'billing_state',
            'address1': 'billing_street_address',
            'address2': 'billing_street_address2',
            'campaignId': 'campaign_id',
            'cardExpiryDate': 'cc_expires',
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
            'ipAddress': 'ip_address',
            'salesTax': 'order_sales_tax',
            #'totalRefunded': 'refund_amount',
            'shipCity': 'shipping_city',
            'shipCountry': 'shipping_country',
            'shipFirstName': 'shipping_first_name',
            'shipLastName': 'shipping_last_name',
            'shipState': 'shipping_state',
            'shipAddress1': 'shipping_street_address',
            'shipAddress2': 'shipping_street_address2',
            'merchantTxnId': 'transaction_id',
            'shipProfileId': 'shipping_id',
            'parentTxnId': 'parent_id',


        }

        self._misc_map = {}

        self._cust_map = {
            'dateCreated': 'acquisition_date',

        }

        self._itm_ord_map = {

            'purchaseStatus': 'purchaseStatus',
        }

        self._itm_tran_map = {
            'fulfillmentStatus': 'order_status',
            'dateShipped': 'shipping_date',
            'lastCancellationDate': 'hold_date',
            'trackingNumber': 'tracking_number',
            'productId': 'campaign_product_id',
            'quantity': 'main_product_quantity',
            'status': 'is_recurring',

        }

        self._ord_map = {
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
            #'reviewStatus': 'order_confirmed',
            'cardIsPrepaid': 'prepaid_match',
            'hasUpsell': 'is_upsell',
            'orderId': 'native_order_id',
            'orderStatus': 'real_order_status',
            'dateCreated': 'time_stamp',
            'dateUpdated': 'last_modified',
            'sourceTitle': 'c1',
            'sourceValue2': 'sub_affiliate',
            'sourceValue3': 'c2',
            'sourceValue4': 'c3',

        }

        self._mer_map = {
            'merchantDescriptor': 'gateway_descriptor',
        }

        self._pur_map = {'status': 'status', 'next_bill_date': 'recurring_date'}

        self._tran_map = {
            'affId': 'affid',
            'sourceValue1': 'affiliate',
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
            'merchantTxnId': 'transaction_id',
            'orderId': 'native_order_id',
            'totalAmount': 'order_total',
            'refund_date': 'refund_date',
            'amount_refunded_to_date': 'amount_refunded_to_date',
            'refund_amount': 'refund_amount'


        }

        self._unk_map = {
            '??': 'ancestor_id', # order_cycles
            '??': 'extended_date', # wait for notes
            '??': 'extended_by', # wait for notes
            '??': 'shipping_method_name', # nope
            '??': 'rma_reason', # nope
            '??': 'refund_date', # nope
            '??': 'rebill_discount_percent', # nope
            '??': 'on_hold_by', # you can get it from notes when there are some notes
            '??': 'order_confirmed_date',
            '??': 'is_fraud',
            '??': 'is_blacklisted',
        }

        self._del_cols = ['fulfillmentStatus', 'cardType', 'txnType']

        self._int_cols = ['order_id', 'main_product_id', 'order_status', 'prepaid_match', 'customer_id', 'created_by_user_name', 'is_upsell', 'created_by_employee_name', 'billing_cycle', 'gateway_id', 'is_void', 'is_refund', 'is_test_cc', 'on_hold', 'is_rma', 'native_transaction_id',  'is_chargeback', 'main_product_quantity']

        self._enforce_text_cols = ['native_transaction_id', 'created_by_user_name', 'created_by_employee_name']

    def format_data(self, comp, tran, ords, products, trans_i, ords_i=None, notes=None, pur=None, reversed=False, **kwargs):
        #ords_i has pretty much been elimnated all it has is the ability to get is recurring.
        o_key = 'orderId'
        t_key = 'transactionId'
        ty_key = 'txnType'
        if reversed:
            o_key = 'order_id'
            t_key = 'transaction_id'
            ty_key = 'txn_type'


        if not len(tran):
            print('nothing to format')
            return
        c_help = [ty_key]
        df = tran[list(self._tran_map.keys())].rename(columns=self._tran_map)
        df['crm_id'] = self.crm_id
        df['crm_brand'] = 'Konnektive'
        # Supplemantal models add
        _data_map = lambda x, idx: {** {k: v for k, v in x.items() if v not in df.columns}, **idx}

        if not self._used_ord:
            self._used_ord = _data_map(self._ord_map, {o_key: 'native_order_id'})
           # print(self._used_ord)
        if len(self._used_ord):
            df = pd.merge(df, ords[list(self._used_ord.keys())].rename(columns=self._used_ord), on='native_order_id')

        if not self._used_comp:
            self._used_comp = _data_map(self._comp_map, {t_key: 'order_id'})
           # print(self._used_comp)
        if len(self._used_comp):
            df = pd.merge(df, comp[list(self._used_comp.keys())+c_help].rename(columns={**self._used_comp}), on='order_id', how='left')

        if not self._used_ti:
            self._used_ti = _data_map(self._itm_tran_map, {t_key: 'order_id'})
           # print(self._used_ti)

        trans_i = trans_i.reset_index(drop=True)
        if len(self._used_ti):
            try:
                df = pd.merge(df, trans_i[list(self._used_ti.keys())].rename(columns=self._used_ti), on='order_id', how='left')
            except Exception as e:
                print(str(e))

        if ords_i is not None:
            if not self._used_oi:
                self._used_oi = _data_map(self._itm_ord_map, {t_key: 'order_id'})
              #  print(self._used_oi)
            df = pd.merge(df, ords_i[list(self._used_ord.keys())].reset_index().rename(columns=self._used_oi), on='native_order_id', how='left')
        if pur is not None and len(pur):
            df = pd.merge(df, pur.drop('order_id', axis=1).rename(columns={
                'transaction_id': 'order_id'
            })[list(self._pur_map.keys())+['order_id']].reset_index().rename(columns=self._pur_map), on='order_id', how='left')
        # derive columns
        for c in ['is_void', 'is_refund', 'is_test_cc', 'on_hold', 'is_rma']:
            df[c] = 0
        df['order_status'] = df.order_status.fillna(0).astype(str).replace(
            {'0.0': '0', 'CANCELLED': '5', 'SHIPPED': '8', 'DELIVERED': '9', 'PENDING': '11', 'PENDING_SHIPMENT': '11',
             'HOLD': '1', 'FAILED': '12', 'RMA': '13', 'RMA_PENDING': '13', 'RETURNED': '14', 'RECYCLE_FAILED': '0', 'RECYCLE': '0'}).astype(int)

        df['is_test_cc'] = (df['cc_type'] == 'TESTCARD').astype(int)
        df['on_hold'] = ((df.order_status == 1) | (df.order_status == 6)).astype(int)
        df.loc['is_rma'] = (df.order_status == 2).astype(int)
        df.loc[df.order_status < 6, 'order_status'] = df.loc[df.order_status < 6].real_order_status.replace({
            'CANCELLED': '5',
            'COMPLETE': '2',
            'DECLINED': '7',
            'PARTIAL': '0',
            'REFUNDED': '6',
            'PENDING': '11',
        })
        df = df.drop('real_order_status', axis=1)
        # purchase Status to be joined in from ords
        df['is_recurring'] = df.is_recurring.replace({np.nan: '0', None: '0', 'ACTIVE': '1', 'CANCELLED': '0', 'PAUSED': '0'})

        df.loc[df.is_recurring != '1', 'is_recurring'] = '0'
        # duplicate at end
        df['created_by_employee_name'] = df.created_by_user_name
        if len(comp):
            df['is_void'] = (df[ty_key] == 'VOID').astype(int)
            df['is_refund'] = (df[ty_key] == 'REFUND').astype(int)
          #  df['amount_refunded_to_date'] = df['refund_amount']
            df['void_amount'] = '0.00'
            df['order_sales_tax_amount'] = df['order_sales_tax']
            df.loc[df.is_void == 1, 'void_amount'] = df.loc[df.is_void == 1, 'refund_amount']

        df['native_transaction_id'] = df['order_id']
        df = df.dropna(subset=['order_id'])
        df.campaign_product_id = df.campaign_product_id.fillna(0).astype(int)

        # Purchase Table over-writes
        if pur is not None and len(pur):
            pm = (df.status.fillna('') != '')
            df.loc[pm, 'is_recurring'] = 1
            df.loc[pm & (df.status != 'ACTIVE'), 'is_recurring'] = 0
            #df.loc[~df.total_refunded.isna(), 'amount_refunded_to_date'] = df.loc[~df.total_refunded.isna(), 'total_refunded']
            df = df.drop(['status', 'total_refunded'], axis=1, errors='ignore')

        df = df.merge(
            products[['campaign_product_id', 'product_id']], on='campaign_product_id', how='left'
        ).drop('campaign_product_id', axis=1).rename(columns={'product_id': 'main_product_id'})
        #print(df.loc[df.order_status == 'PENDING'])
        df = df.loc[~df.order_id.isna()]
        df.parent_id = df.parent_id.fillna(0).astype(int).astype(str).replace({'0':''})
        df[self._int_cols] = df[self._int_cols].fillna(0)
        df.amount_refunded_to_date = df.amount_refunded_to_date.fillna(0)
        df.refund_amount = df.refund_amount.fillna(0)
        for c in self._int_cols:
            try:
                df[c] = df[c].astype(int)
            except:
                print(c)
        df.order_total = df.order_total.astype(float)
        df.loc[df.order_total.isna(), 'order_total'] = 0
        df[self._int_cols] = df[self._int_cols].astype(int)
        df[self._enforce_text_cols] = df[self._enforce_text_cols].astype(str)
        df = df.drop(columns=c_help, errors='ignore')
        df.loc[(df.decline_reason.str.lower().str.contains('approv')) | (df.decline_reason.str.lower().str.contains('test charge')), 'decline_reason'] = np.nan
        date_cols = ['hold_date', 'time_stamp', 'refund_date', 'chargeback_date', 'shipping_date']
        if 'last_modified' in df.columns:
            date_cols += ['last_modified']
        df['rep_last_modified'] = df[date_cols].apply(pd.to_datetime).max(axis=1)
        return df.drop_duplicates(subset='order_id')

    @staticmethod
    def formatted_map(dict_):
        res = {re.sub("(\w)([A-Z])", r"\1_\2", f'{c}').lower(): v for c, v in dict_.items()}
        try:
            res['3_dtxn_result'] = res['three_d_txn_result']
        except KeyError:
            pass
        return res

    def reverse_maps(self):
        self._pur_map = self.formatted_map(self._pur_map)
        self._comp_map = self.formatted_map(self._comp_map)
        self._tran_map = self.formatted_map(self._tran_map)
        self._itm_tran_map = self.formatted_map(self._itm_tran_map)
        self._itm_ord_map = self.formatted_map(self._itm_ord_map)
        self._ord_map = self.formatted_map(self._ord_map)

    def update_product_ids(self, crm_id):
        df_phist = pd.read_sql(
            "select crm_id, offer_id, step, main_product_id::text from ui_54407332_offers.product_history", self.engine).drop_duplicates()
        df = pd.read_sql(f"""select  crm_id,  order_id,  time_stamp, main_product_id 
                from crm_global.orders  a 
                where crm_id='{crm_id}' and main_product_id =any(ARRAY{df_phist.main_product_id.dropna().unique().tolist()}::int[]::text[])""",
                                 self.engine)
        if len(df):
            df = df.merge(df_phist, on=['crm_id', 'main_product_id'], how='left')
            off_list = df.offer_id.dropna().unique().tolist()
            off = pd.read_sql(f"""select crm_id, offer_id, step, main_product_id::int::text as new_product from ui_54407332_offers.offer_globals 
                                      where offer_id = any(ARRAY{off_list}::numeric[])  and  main_product_id is not null""",self.engine)
            df = df.merge(off, on=['crm_id', 'offer_id', 'step'], how='left')
            df.loc[~df.new_product.isna(), 'main_product_id'] = df.loc[~df.new_product.isna(), 'new_product']
            df = df.drop(['new_product', 'offer_id','step'], axis=1, errors='ignore')
            self.upsert(df)

    def upsert_data(self, order_ids=False, is_ssc_support=False, max_batch=100000, max_days_back=180):
        cids = []
        if not order_ids:
            order_ids = pd.read_sql(f"""select distinct(order_id) order_id from {self.crm_id}.transactions where txn_type='SALE' and date_created>='{dt.datetime.now() - dt.timedelta(days=max_days_back)}'""", self.engine).order_id.unique().tolist()
        elif not isinstance(order_ids, list):
            order_ids = [order_ids]

        results = {'comp': None, 'tran': None, 'ords': None, 'trans_i': None, 'pur': None, 'reversed': True}
        _lock = Lock()

        def _getter(table, oids, col, res_key, and_='', columns='*'):
            nonlocal results
            nonlocal _lock
            if columns != '*':
                columns = ','.join(columns)
            col_oids = f"{col} = any(ARRAY{oids}) " if oids else ''
            if col_oids and and_:
                and_ = " and "+and_

            whr = ''
            if col_oids or and_:
                whr = f" where {col_oids} {and_}"
            qry = f""" SELECT {columns} from {self.crm_id}.{table} {whr}"""
           # print(qry)

            res = pd.read_sql(qry, self.engine)
            print('done', table)
            _lock.acquire()
            results[res_key] = res
            _lock.release()

        def _getter2(table, oids, col, res_key, and_='', columns='*'):
            nonlocal results
            nonlocal _lock
            col_oids = f"inner join (select unnest(ARRAY{oids}) as {col}) b on b.{col}=a.{col}"


            if columns != '*':
                columns = 'a.' + ',a.'.join(columns)
            else:
                columns = 'a.*'
            qry = f""" SELECT {columns} from {self.crm_id}.{table} a 
                    {col_oids}
                    {f'where {and_}' if and_ else ''}
                    """
            # print(qry)
            if table == 'composite':
                print('composite')
            try:
                res = pd.read_sql(qry, self.engine)
                print('done', table)
                _lock.acquire()
                results[res_key] = res
                _lock.release()
            except Exception as e:
                print(str(e))

        def _get_prod():
            nonlocal results
            nonlocal _lock
            res = Products(self.engine, self.crm_id).get()

            _lock.acquire()
            results['products'] = res
            _lock.release()
        sdex, edex = 0, len(order_ids)
        while sdex <= edex:
            oids = order_ids[sdex: sdex+max_batch]
            sdex += max_batch
            t6 = False
            if self.is_continuity_model:
                t6 = Thread(target=_getter, args=('purchases', order_ids, 'order_id', 'pur'))
                t6.start()
            self.reverse_maps()
            get_func = _getter if len(oids) <10000 else _getter2
            t1 = Thread(target=get_func, args=('transactions', oids, 'order_id', 'tran', "txn_type = 'SALE'"))
            t1.start()

            t2 = Thread(target=get_func, args=('orders', oids, 'order_id', 'ords'))
            t2.start()
            t3 = Thread(target=_get_prod)
            t3.start()
            t7 = Thread(target=get_func, args=('transactions', oids, 'order_id', 'refunds', "txn_type in('VOID','REFUND') and transaction_id!= parent_txn_id and response_type='SUCCESS' and order_type= 'NEW_SALE' ", ['parent_txn_id::int', 'date_created', 'total_amount::numeric']))
            t7.start()
            t1.join()
            ids = results['tran'].transaction_id.tolist()
            if not order_ids:
                ids = False
            t4 = Thread(target=get_func, args=('composite', ids, 'transaction_id', 'comp'))
            t4.start()
            t5 = Thread(target=get_func, args=('transaction_items', ids, 'transaction_id', 'trans_i'))
            t5.start()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            if t6:
                t6.join()
            t7.join()
            ref = results.pop('refunds')
            ref.total_amount = ref.total_amount.astype(float)
            n_ref = ref[['parent_txn_id', 'date_created']].dropna().groupby('parent_txn_id').max().reset_index().rename({'parent_txn_id': 'transaction_id', 'date_created': 'refund_date'}, axis=1)
            n_ref = n_ref.merge(ref[['parent_txn_id', 'total_amount']].dropna().groupby('parent_txn_id').sum().reset_index().rename({'parent_txn_id': 'transaction_id', 'total_amount': 'amount_refunded_to_date'},axis=1), on='transaction_id', how='left')
            n_ref['refund_amount'] = n_ref['amount_refunded_to_date']
            results['tran'] = results['tran'].merge(n_ref, on='transaction_id', how='left')
            results['tran'].refund_date = pd.to_datetime(results['tran'].refund_date)

            df = self.format_data(**results)
            df.loc[df.decline_reason == 'Zero Amount Transaction Not Sent to Gateway', 'decline_reason'] = np.nan
            self.upsert(df)
            cids += df.customer_id.unique().tolist()
        self.update_product_ids(self.crm_id)

        # if not is_ssc_support:
            # return
        # df = df.loc[df]
        return list(set(cids))
        # # internal rebiller tracking.
        # df.main_product_id = df.main_product_id.astype(int)
        # df = df.merge(self.offers[['main_product_id', 'offer_id', 'offer_type']], on='main_product_id')

    @staticmethod
    def get_wm(ids, multiplier=0.1):
        wm = len(ids) * multiplier
        if wm < 4:
            wm = 4
        elif wm > 10000:
            wm = 10000
        return f"{str(int(wm))}MB"

    def get_cid_stmt(self, cids, cur):
        if cids and len(cids) and len(cids) < 1500:
            cur.execute("drop table if exists kk_rec_cust")
            cur.execute(f"""create temp table kk_rec_cust as select  unnest(ARRAY{cids}::numeric[]) customer_id""")
            cur.execute(f"""alter table kk_rec_cust add primary key(customer_id)""")
            return f"inner join kk_rec_cust krc on a.customer_id = krc.customer_id and a.crm_id = '{self.crm_id}'"
        return ""

    def reset_sync_errors(self):
        self._cb_sync_err = ""
        self._cancel_sync_err = ""

    @staticmethod
    def close_session(con, cur):
        try:
            cur.close()
        except:
            pass
        try:
            con.close()
        except:
            pass

    def sync_cancellations(self, customer_ids=False):
        print(f'sync cancellations {self.crm_id} {dt.datetime.now()}')
        con = self.engine.raw_connection()
        cur = con.cursor()
        try:
            cid = self.get_cid_stmt(customer_ids, cur)
            cur.execute(f"""SET LOCAL WORK_MEM = '10GB'""")
            cur.execute(f"""
             drop table if exists kk_cn;
                        """)
            print(f'kk_cn {self.crm_id} {dt.datetime.now()}')
            cur.execute(f"""
             create temp table kk_cn as
             select distinct on (b.native_order_id, b.order_id) b.native_order_id   native_order_id,
                                                                b.order_id::numeric order_id,
                                                                b.customer_id,
                                                                note
             from (select a.customer_id, native_order_id, note
                   from crm_global.system_notes a
                   {cid}
                   where a.crm_id = '{self.crm_id}'
                     and note ilike '%%Order #%%cancelled.%%') a
                     inner join  ( select crm_id, customer_id, native_order_id, order_id from crm_global.orders where crm_id='{self.crm_id}') b on b.native_order_id = a.native_order_id
                     left join (select crm_id, native_order_id, order_id from crm_global.cancellations where crm_id='{self.crm_id}')  c on c.native_order_id = b.native_order_id and c.order_id = b.order_id
                     where c.order_id is null;

                        """)
            cur.execute(f"""
                 delete
                     from kk_cn
                     where note ilike '%%/%%';
                        """)
            cur.execute(f"""
             create unique index kk_cn_pk on kk_cn (native_order_id, order_id);
                        """)
            cur.execute(f"""
             drop table if exists kk_tcn;
                                    """)
            print(f'kk_tcn {self.crm_id} {dt.datetime.now()}')
            cur.execute(f"""
             create temp table kk_tcn as
             select a.*
             from (select a.customer_id,
                          a.native_order_id,
                          a.note,
                          string_to_array(regexp_replace(trim(replace(
                                  split_part(replace(replace(note, ':', ''), 'Order #', 'Order#'), 'Order#', -1), ' ', '')),
                                                         E'[\\n\\r\\s+]+', '', 'g'), 'STOP') as s_str
                   from crm_global.system_notes a
                   {cid}
                   where a.crm_id = '{self.crm_id}'
                     and a.note like 'Order%%STOP%%'
                     and a.note not ilike '%%&ensp%%') a;
                                    """)
            cur.execute(f"""
                 drop table if exists kk_tcn_b;
                                    """)
            cur.execute(f"""
             create temp table kk_tcn_b as
             select distinct on (native_order_id,order_id) native_order_id, order_id, customer_id, note
             from (select customer_id,
                          case when native_order_id ~ '^([0-9]+)$' then null else native_order_id end native_order_id,
                          note,
                          case when order_id ~ '^([0-9]+)$' then order_id::numeric else null end      order_id
                   from (select customer_id,
                                trim(replace(s_str[1], 'OrderNumber', ''), '\n') as native_order_id,
                                note,
                                case
                                    when array_length(s_str, 1) > 1
                                        then s_str[2]
                                    else null end                                as order_id
                         from kk_tcn) a) a;
                                    """)
            cur.execute(f"""
                 drop table if exists kk_tcn;
                                             """)
            print(f'kk_cn amalgamate all {self.crm_id} {dt.datetime.now()}')
            cur.execute(f"""
                 insert into kk_cn
                 select *
                 from kk_tcn_b
                 on conflict do nothing;
                                             """)
            cur.execute(f"""
             drop table if exists kk_tcn_b;
                                             """)
            cur.execute(f"""
             alter table kk_cn add column crm_id text default '{self.crm_id}';

                                                        """)
            print(f'begin cancel inserts {self.crm_id} {dt.datetime.now()}')
            cur.execute(f"""
             insert into crm_global.cancellations select * from kk_cn on conflict do nothing;
                                                        """)
            try:
                print(f'begin locked cancels update {self.crm_id} {dt.datetime.now()}')
                self._rs_lock.acquire()
                print(f'cancels lock acquired {self.crm_id} {dt.datetime.now()}')
                cur.execute(f"""
                     update crm_global.orders up
                     set is_recurring = 0
                     from kk_cn
                     where up.crm_id = '{self.crm_id}'
                       and up.order_id = kk_cn.order_id
                       and kk_cn.order_id is not null
                       and up.is_recurring <> 0;
                     
                                                            """)

                cur.execute(f"""
                     update crm_global.orders up
                     set is_recurring = 0
                     from kk_cn
                     where up.crm_id = '{self.crm_id}'
                       and up.native_order_id = kk_cn.native_order_id
                       and kk_cn.order_id is null
                       and up.is_recurring <> 0;
                                                            """)
                cur.execute("drop table if exists kk_rec_recent")
                # cur.execute(f"""
                #  create temp table kk_rec_recent as select crm_id, customer_id, main_product_id, max(order_id) order_id
                #    from crm_global.orders
                #    where crm_id = '{self.crm_id}'
                #      and is_recurring > 0
                #      and decline_reason is null
                #    group by  crm_id, customer_id, main_product_id;
                #
                #  """)
                # cur.execute(f"""
                #  update crm_global.orders up set is_recurring = 0 from kk_rec_recent dn
                #  where up.is_recurring =1
                #  and up.main_product_id = dn.main_product_id
                #  and up.customer_id = dn.customer_id
                #  and up.order_id <> dn.order_id
                #  and up.crm_id=dn.crm_id;
                #
                #  """)
                con.commit()
                self._rs_lock.release()
            except Exception as ex:
                self._rs_lock.release()
                raise ex
        except Exception as e:
            self._cancel_sync_err = f"cancellation sync error: {str(e)}"
            print(self._cancel_sync_err)
            con.rollback()
        finally:
            self.close_session(con, cur)
            print(f'cancels complete {self.crm_id} {dt.datetime.now()}')

    def sync_cbs(self, customer_ids=False):
        print(f'sync cbs {self.crm_id} {dt.datetime.now()}')
        con = self.engine.raw_connection()
        cur = con.cursor()
        try:

            cid = self.get_cid_stmt(customer_ids, cur)
            cur.execute(f"""SET LOCAL WORK_MEM = '10GB'""")
            cur.execute(f"""drop table if exists kk_cb;""")
            print(f'kk_cb {self.crm_id} {dt.datetime.now()}')
            cur.execute(f"""
             create temp table kk_cb as
             select a.*
             from (select distinct a.customer_id::int, 1 as is_chargeback
                   from crm_global.system_notes a
                     {cid}
                   where crm_id='{self.crm_id}' and note ilike '%%chargeback%%') a
                      left join(select customer_id::int
                                from crm_global.customer_blacklist
                                where crm_id = '{self.crm_id}'
                                  and is_chargeback = '1') b on b.customer_id = a.customer_id
             where b.customer_id is null;
                        """)
            print(f'kk_bl  {self.crm_id} {dt.datetime.now()}')
            cur.execute(f"""drop table if exists kk_bl;""")
            cur.execute(f"""
             create temp table kk_bl as
             select a.*
             from (select distinct a.customer_id::int, 1 as is_blacklisted
                   from crm_global.system_notes a
                   {cid}
                   where crm_id = '{self.crm_id}'
                     and note ilike '%%blacklist%%') a
                      left join(select customer_id::int
                                from crm_global.customer_blacklist
                                where crm_id = '{self.crm_id}'
                                  and is_blacklisted = '1') b on b.customer_id = a.customer_id
             where b.customer_id is null;
                        """)
            print(f'c_main  {self.crm_id} {dt.datetime.now()}')
            cur.execute(f"""
             drop table if exists c_main;
                                    """)
            cur.execute(f"""
             create temp table c_main as
             select '{self.crm_id}'                                        crm_id,
                    coalesce(kk_cb.customer_id, kk_bl.customer_id) customer_id,
                    coalesce(is_chargeback, 0)                     is_chargeback,
                    coalesce(is_blacklisted, 0)                    is_blacklisted,
                    1 as                                           is_recurring
             from kk_cb
                      full outer join kk_bl on kk_cb.customer_id = kk_bl.customer_id;
                                    """)
            print(f'blacklist inserts  {self.crm_id} {dt.datetime.now()}')
            cur.execute(f"""
                     insert into crm_global.customer_blacklist
                     select *
                     from c_main
                     on conflict (crm_id,customer_id) do update set is_blacklisted=excluded.is_blacklisted,
                                                                    is_chargeback=excluded.is_chargeback,
                                                                    is_recurring=excluded.is_recurring;
                                    """)
            try:
                print(f' cb inserts {self.crm_id} {dt.datetime.now()}')
                self._rs_lock.acquire()
                print(f'cb inserts lock acquired  {self.crm_id} {dt.datetime.now()}')
                cur.execute(f"""

                     update crm_global.orders up
                     set is_recurring  = dn.is_recurring::smallint,
                       --  is_chargeback=dn.is_chargeback::smallint,
                         is_blacklisted=dn.is_blacklisted::smallint
                     from c_main dn
                     where dn.customer_id = up.customer_id and up.crm_id= dn.crm_id;
                                        """)
                con.commit()
                self._rs_lock.release()
            except Exception as ex:
                self._rs_lock.release()
                raise ex

        except Exception as e:
            self._cb_sync_err = f"chargeback sync error: {str(e)}"
            print(f'{self._cb_sync_err} {self.crm_id} {dt.datetime.now()}')
            con.rollback()
        finally:
            self.close_session(con, cur)
        print(f'sync cbs complete {self.crm_id} {dt.datetime.now()}')
        return

    def clean_customer_ids(self, customer_ids, recurring_only=False):
        return [c[0] for c in self.engine.execute(
            f"""select distinct(customer_id) customer_id from crm_global.orders where customer_id::int = Any(ARRAY{customer_ids}::int[]) 
                           and coalesce(is_blacklisted,0) <> 1 and coalesce(is_chargeback,0) <> 1 {"and is_recurring=1" if recurring_only else ""} and crm_id='{self.crm_id}'""")]

    def sync_recurring_n(self, customer_ids=False):
        print(f'sync recurring {self.crm_id} {dt.datetime.now()}')
        t1 = Thread(target=self.sync_cbs, args=(customer_ids,))
        t2 = Thread(target=self.sync_cancellations, args=(customer_ids,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        if self._cb_sync_err != "":
            err = self._cb_sync_err
            self.reset_sync_errors()
            print(f'sync recurring failed cb error {self.crm_id} {dt.datetime.now()}')
            return False, err
        if self._cancel_sync_err != "":
            err = self._cancel_sync_err
            self.reset_sync_errors()
            print(f'sync recurring failed cancel sync error{self.crm_id} {dt.datetime.now()}')
            return False, err
        print(f'sync recurring done {self.crm_id} {dt.datetime.now()}')
        return True, ""

    def sync_recurring(self, customer_ids=False, max_batch_size=1000, min_batch_size=100, max_threads=2, max_days_back=180, recurring_only=False, clean_cids=False):
        self.sync_cbs(customer_ids)
        if not customer_ids or isinstance(customer_ids, list) and not len(customer_ids):
            customer_ids = pd.read_sql(
                    f"""Select distinct customer_id from crm_global.orders where crm_id = '{self.crm_id}' and is_blacklisted <> 1 and is_chargeback <>1
                        and month_date >= '{dt.datetime.now()-dt.timedelta(days=max_days_back)}'::date {"and is_recurring=1" if recurring_only else ""}
                    """,
                    self.engine).customer_id.to_list()

        else:
            if clean_cids:
                customer_ids = self.clean_customer_ids(customer_ids, recurring_only)
            customer_ids = [c[0] for c in self.engine.execute(
                    f""" select distinct(customer_id) customer_id from crm_global.system_notes where customer_id::int = Any(ARRAY{customer_ids}::int[]) and crm_id='{self.crm_id}'""")]
        up_lock = Lock()
        error = ""

        def run_batch(_cids=False):
            print('execute sync recurring', dt.datetime.now())
            conn = self.engine.raw_connection()
            cur = conn.cursor()
            cur.execute(f"""SET LOCAL WORK_MEM = '{self.get_wm(_cids,10)}' """)
            #if _cids and len(_cids) > 1400:
            cur.execute("drop table if exists sync_cust")
            cur.execute(f"""CREATE TEMP TABLE sync_cust ON COMMIT DROP AS ( select customer_id from unnest(ARRAY{_cids}::int[]) customer_id) """)
            cur.execute(f"""Alter table sync_cust add constraint  _sc_pk primary key (customer_id)""")

            cid_c = f"and c.customer_id = any(ARRAY{_cids}::int[])" if _cids else ""
            cid = f"customer_id = any(ARRAY{_cids}::int[])" if _cids else ""
            cid_join = None
            # if len(_cids) <= 1400:
            #     cid_join = lambda x: f"inner join unnest(Array{_cids}::int[]) as sc(customer_id) on sc.customer_id = {x}.customer_id" if _cids else ""
            # else:
            cid_join = lambda x: f"inner join sync_cust sc on sc.customer_id = {x}.customer_id" if _cids else ""


            qry = f"""
            CREATE TEMP TABLE is_recurring_update_temp ON COMMIT DROP AS (select distinct on (c.order_id) c.order_id,
               c.crm_id,
               c.time_stamp,
               case
                   when (c.order_id = (max(c.order_id) over w_max))
                       and h.order_id is null
                       and c.is_blacklisted =0 and c.is_chargeback=0
                       and (f.retry_attempt_count is null or f.retry_attempt_count < g.salvage_attempts)
                       and ((d.order_status = 'COMPLETE' or (d.order_status = 'REFUNDED' and e.native_order_id is null))) then 1
                   else 0 end as is_recurring
                    from (select offer_id from ui_54407332_offers.offers where offer_type='ssc_no') a
                             inner join( SELECT crm_id, offer_id,step, main_product_id from ui_54407332_offers.offer_globals 
                             where  crm_id = '{self.crm_id}' ) b
                                        on b.offer_id = a.offer_id 
                             inner join (SELECT crm_id, order_id, main_product_id, customer_id, native_order_id, gateway_id, decline_reason, time_stamp, 
                             coalesce(is_blacklisted,0) is_blacklisted, coalesce(is_chargeback,0) is_chargeback
                              FROM crm_global.orders where crm_id = '{self.crm_id}' ) c
                                        on c.main_product_id::int = b.main_product_id::int and
                                           c.crm_id = b.crm_id
                             {cid_join('c')}
                    
                             inner join ( SELECT order_id, order_status FROM crm_kk_3.orders a
                                    --    {cid_join('a')}
                                --where cid
                                ) d on d.order_id = c.native_order_id
                        --and (d.order_status = 'COMPLETE' or d.order_status = 'REFUNDED')
                             left join (SELECT DISTINCT crm_id, native_order_id FROM crm_global.system_notes a
                                          {cid_join('a')}
                                WHERE note ILIKE '%%cancelled.%%' and crm_id='{self.crm_id}' 
                                --and cid 
                                ) e on (e.crm_id = c.crm_id and e.native_order_id = c.native_order_id)
                        /*and (e.note ilike any (ARRAY ['%cancelled.%']))*/
                            -- left join (SELECT DISTINCT crm_id, a.customer_id FROM crm_global.system_notes a 
                            --   {cid_join('a')}
                            -- WHERE note ilike any (ARRAY ['%%chargeback%', '%%blacklist%%']) and crm_id='{self.crm_id}' 
                             --and cid
                            -- ) x on (x.crm_id = c.crm_id and x.customer_id = c.customer_id)
                        /*and (x.note ilike any (ARRAY ['%chargeback%', '%blacklist%']))*/
                    
                            
                             left join (SELECT crm_id, order_id, retry_attempt_count, decline_reason FROM augmented_data.order_cycles) f
                                       on f.crm_id = c.crm_id and f.order_id = c.order_id and f.crm_id = 'crm_kk_3'
                             left join ui_54407332_clients.gateway_settings g on g.gateway_id = c.gateway_id and g.crm_id = c.crm_id
                             left join (select distinct order_id
                                        from reporting.ui_revenue_transactions
                                        where type = 'alert' and crm_id = '{self.crm_id}' ) h on h.order_id::int = c.order_id
                    where nullif(c.decline_reason, 'Zero Amount Transaction Not Sent to Gateway') is null
                        window w_max as (partition by a.offer_id, c.customer_id, b.step order by c.order_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
                    order by c.order_id desc);
             """


            try:
                nonlocal up_lock, error
             #   print(qry)
                cur.execute("drop table if exists is_recurring_update_temp")
                cur.execute(qry)
                print('exec 1 done', dt.datetime.now())
                up_lock.acquire()
                try:
                    cur.execute("""UPDATE crm_global.orders SET is_recurring = a.is_recurring 
                                    FROM is_recurring_update_temp AS "a" 
                                    WHERE orders.crm_id = a.crm_id 
                                    AND orders.month_date = a.time_stamp::date
                                    AND orders.order_id = a.order_id 
                                    AND orders.is_recurring::numeric <> a.is_recurring::numeric;
                                """)


                    print('exec 2 done')

                    cur.execute(
                        f"""update crm_global.orders set is_recurring = 0 
                        where decline_reason is not null  
                        and decline_reason <> 'Zero Amount Transaction Not Sent to Gateway'
                         and is_recurring <> 0 
                         and crm_id = '{self.crm_id}' 
                         {"and" if cid else ""} {cid}""")
                    up_lock.release()
                except Exception as e:
                    error += str(e) + ','
                    up_lock.release()
                    raise e

                print('exec 3 done')
            except Exception as e:
                try:
                    conn.rollback()
                    cur.close()
                    conn.close()
                except:
                    pass
                error += str(e) + ','
                print(str(e))
                return False, error
            conn.commit()
            cur.close()
            conn.close()
            #
            # self.engine.execute(qry)
            print('execute sync recurring complete')

        sdex, edex = 0, len(customer_ids)

        def joiner(*tr):
            for t in tr:
                try:
                    t.join()
                except:
                    pass
                return []

        batch_size = int(len(customer_ids)/max_threads) + 1
        if batch_size > max_batch_size:
            batch_size = max_batch_size

        if edex > batch_size + 1 and edex > min_batch_size:
            threads = []
            while sdex <= edex:
                threads.append(Thread(target=run_batch, args=(customer_ids[sdex:sdex + batch_size],)))
                threads[len(threads)-1].start()
                sdex += batch_size
                if len(threads) >= max_threads:
                    threads = joiner(*threads)
            joiner(*threads)
        else:
            run_batch(customer_ids)
        try:
            self.engine.execute(f"""
                                    update crm_global.orders up
                                    set is_recurring=0
                                    from (select distinct nullif(trim(split_part(note, 'STOP', 2)), '') tid
                                          from crm_global.system_notes
                                          where crm_id = '{self.crm_id}'
                                            {f"and customer_id::int = Any(ARRAY{customer_ids}::int[])" if customer_ids and len(customer_ids) <50000 else ""}
                                            and note like '%%STOP %%'
                                            and note like '%%Order%%'
                                            ) dn
                                          where up.order_id::text  = dn.tid::text and tid is not null  and up.is_recurring=1 and
                                               up.crm_id  = '{self.crm_id}'

                                               """)
        except Exception as e:
            return False, f"recurring sync error: {str(e)}"
        if error == '':
            return True, ""
        return False, f"recurring sync error:  {error}"
        # print([f  for  f  in t])

    def max_last_modified(self):
        return self.engine.execute(f"""SELECT max(last_modified) from {self.schema}.{self.table} 
                                where crm_id='{self.crm_id}'
                                and last_modified > time_stamp""").scalar()

    def max_time_stamp(self):
        return self.engine.execute(f"""SELECT max(last_modified) from {self.schema}.{self.table} 
                                where crm_id='{self.crm_id}'
                                """).scalar()

    def delete_crm(self):
        self.engine.execute(f"Delete from {self.schema}.{self.table} where crm_id = '{self.crm_id}'")

    def update_extended(self, df):
        col_map = {'customerId': 'customer_id'}
        df = df.rename(columns=col_map)
        df = df.merge(pd.read_sql(f"""SELECT a.crm_id,a.customer_id, a.order_id, b.time_stamp, a.bc_inferred as billing_cycle,b.rebill_discount_percent
                                        from augmented_data.order_cycles a 
                                        inner join crm_global.orders b on a.crm_id = b.crm_id and a.order_id=b.order_id
                                        where a.customer_id = ANY(ARRAY{df.customer_id.tolist()})
                                        AND is_recurring = 1
                                        AND a.crm_id = '{self.crm_id}'
                                     """, self.engine), on='customer_id')
        df['extended_date'] = np.nan
        disc = df.loc[df.discount.fillna(' ') != df.rebill_discount_percent.fillna('').astype(str)]
        disc.rebill_discount_percent = disc.discount
        df = df.loc[df.extend_by != '']
        df.loc[df.extend_by == 'Priority Billing', 'extended_date'] = pd.to_datetime(dt.datetime.now() - dt.timedelta(days=1))
        df.extend_by = df.extend_by.replace({'Priority Billing': '-1'}).astype(float)
        df.loc[(df.billing_cycle.astype(float) == 0) & (df.extend_by > 0), 'extend_by'] += 7
        df.loc[(df.billing_cycle.astype(float) > 0) & (df.extend_by > 0), 'extend_by'] += 30
        e_msk = df.extended_date.isna()
        df.loc[e_msk, 'extended_date'] = pd.to_datetime(df.loc[e_msk].time_stamp) + pd.to_timedelta(
            df.loc[e_msk].extend_by, 'D')
        df.extended_date = pd.to_datetime(df.extended_date).dt.date
        df.customer_id = df.customer_id.astype(int)
        df.order_id = df.order_id.astype(int)
        disc.order_id = disc.order_id.astype(int)
        self.upsert(df[['crm_id', 'order_id', 'extended_date', 'time_stamp']])
        self.upsert(disc[['crm_id', 'order_id', 'time_stamp', 'rebill_discount_percent']])
        return df, disc


if __name__ == '__main__':
    from DataFactory import sqlinterface as sqli
    from models import config
    DB = sqli.Db(connstr=config.conn_select('primary'))
    Hybrid(DB, 'crm_kk_3').sync_recurring_x()
    print('done')
