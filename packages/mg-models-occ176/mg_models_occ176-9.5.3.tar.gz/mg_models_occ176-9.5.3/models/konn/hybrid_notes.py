from models.db import Db, pd, np
from models.konn.kk_struc import KKStruc
import re


class HybridNotes(Db):
    def __init__(self, db, crm_id, table):
        Db.__init__(self, db, 'crm_global', table)
        self._crm_id = crm_id
        self._col_map = {'orderId': 'native_order_id', 'customerId': 'customer_id', 'campaignId': 'campaign_id',
                         'date': 'date_time', 'dateCreated': 'date_time', 'message': 'note', 'agentName': 'source'}

    def format_data(self, df):
        df = HybridNotes._sub_mod_from_array_col(df, 'notes', ['customerId'], orient='records').replace(r'^\s*$', np.nan, regex=True).drop_duplicates(subset=['customerId', 'message'])

        def _parse(x):
            try:
                val = x.message.split(' ')
            except:
                return np.nan
            source = x.agent_name

            if source == 'System':
                if val[0] == 'Order' and val[1][0] != '#' and val[1] != 'Confirmation':
                    #print(val[0], val[1])
                    return val[1]
            elif ' '.join(val[:3]) == 'New customer order' and val[5] == 'created.':
                return val[3]
            elif val[0] == 'Order' and val[1][0] == '#' and val[2] in ['cancelled.', 'shipped', 'STOP']:
                return val[1][1:]
            elif val[0] == 'Order#' and val[2] in ['cancelled.', 'STOP']:
                return val[1]

            return np.nan
        if 'order_id' not  in df.columns:
            df['order_id'] = df.apply(_parse, axis=1)
            df = df.loc[df.message != 'Updated customer.']
            try:
                df.customer_id = df.customer_id.astype(int)
                df.date_created = pd.to_datetime(df.date_created)
            except Exception as e:
                print('note parse error:', str(e))
                return
            # missing KK orderId from most recent value above
            df = df.sort_values(['customer_id', 'date_created']).reset_index(drop=True)
            df['p_cust'] = df.shift(1).reset_index(drop=True)[:-1].customer_id
            df['n_cust'] = df.shift(-1).customer_id
            fir_msk = ((df.p_cust != df.customer_id) & (~df.n_cust.isna())) & (df.order_id.isna())
            lst_msk = (df.n_cust != df.customer_id) & (df.order_id.isna())

            # df['index']  =  df.index
            df.loc[fir_msk] = df.loc[fir_msk].reset_index(drop=False).drop('order_id', axis=1).merge(
                df.loc[~df.order_id.isna(), ['customer_id', 'order_id']].drop_duplicates('customer_id', keep='first'),
                on='customer_id', how='left').set_index('index', drop=True)

            lst_msk = (df.n_cust != df.customer_id) & (df.order_id.isna())
            df.loc[lst_msk] = df.loc[lst_msk].reset_index(drop=False).drop('order_id', axis=1).merge(
                df.loc[~df.order_id.isna(), ['customer_id', 'order_id']].drop_duplicates('customer_id', keep='last'),
                on='customer_id').set_index('index', drop=True)
            df = df.set_index(['customer_id', 'date_created'], drop=False).sort_index()
            df.order_id.fillna(method='ffill', inplace=True)
            df = df.reset_index(drop=True).set_index(['customer_id', 'order_id', 'date_created'], drop=False).sort_index()
            df['note_index'] = df.groupby(level=[0, 1])['message'].cumcount()
            # Set Remaining indexes
            df = df.dropna()
            df.customer_id = df.customer_id.astype(int)
        if 'crm_id' not in df.columns:
            df['crm_id'] = self.crm_id

        return df.drop(columns=['p_cust', 'n_cust'], errors='ignore').reset_index(drop=True)

    def delete_crm(self):
        self.engine.execute(f"Delete from {self.schema}.{self.table} where crm_id = '{self._crm_id}'")
        return self

    @staticmethod
    def formatted_map(dict_):
        res = {re.sub("(\w)([A-Z])", r"\1_\2", f'{c}').lower(): v for c, v in dict_.items()}
        try:
            res['3_dtxn_result'] = res['three_d_txn_result']
        except KeyError:
            pass
        return res

    def reverse_maps(self):
        self._col_map = self.formatted_map(self._col_map)

    def _translate(self, _df):
        if list(_df.columns)[0] not in list(self._col_map.keys())[0]:
            self.reverse_maps()
        df = _df.rename(columns=self._col_map).drop('orderId', axis=1, errors='ignore')
        df = df.set_index(['customer_id', 'native_order_id', 'date_time'], drop=False).sort_index()
        df['note_index'] = df.groupby(level=[0, 1])['note'].cumcount()
        df['crm_id'] = self._crm_id
        df['crm_brand'] = 'Konnektive'
        return df.reset_index(drop=True)


class HybridEmployeeNotes(HybridNotes):
    def __init__(self, db, crm_id):
        HybridNotes.__init__(self, db, crm_id, 'employee_notes')
        self.set_constraint('employee_notes_pk', ['date_time', 'native_order_id', 'note_index', 'crm_id'])

    def translate(self, df):
        return self._translate(df.loc[df.agentName.str.strip() != 'System'])

    def format_data(self, df):
        df = KKStruc.format_ts_offset(df)
        return self.translate(df)


class HybridSystemNotes(HybridNotes):
    def __init__(self, db, crm_id):
        HybridNotes.__init__(self, db, crm_id, 'system_notes')
        self.set_constraint('system_notes_pk', ['date_time', 'native_order_id', 'note_index', 'crm_id'])
        self.crm_id = crm_id

    def translate(self, df):
        return self._translate(df)

    def format_data(self, df):
        df = KKStruc.format_ts_offset(df)
        return self.translate(df)

    def update_recurring_status_from_notes(self, df):
        cb_cids = df.loc[df.note.str.contains('chargeback', case=False)].customer_id.unique()
        bl_cids = df.loc[df.note.str.contains('blacklist', case=False)].customer_id.unique()
        oids = df.loc[df.note.str.contains('cancelled.', case=False)].customer_id.unique()

        self.engine.execute(f"""
            update crm_global.orders set is_chargeback=1, is_recurring=0
            where customer_id::int = any(ARRAY{cb_cids}::int[] )
            and crm_id='{self.crm_id}'
            """)
        self.engine.execute(f"""
            update crm_global.orders set is_blacklisted=1, is_recurring=0
            where customer_id::int = any(ARRAY{bl_cids}::int[]) 
            and crm_id='{self.crm_id}'
            """)
        return list(set(cb_cids+bl_cids))



