from models.konn.kk_struc import KKStruc, np, pd


class Notes(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'notes')
        self.set_constraint('notes_pk', ['customer_id', 'order_id', 'note_index'])

    def format_data(self, df):
        if not len(df):
            return False
        df = self.format_ts_offset(df)
        df = self.format_col_names(
            Notes._sub_mod_from_array_col(
                df, 'notes', ['customerId'], orient='records'
            ).replace(r'^\s*$', np.nan, regex=True
                      ).drop_duplicates(subset=['customerId', 'dateCreated', 'message']))
        df = df.loc[~df.message.replace({np.nan,  ''}).astype(str).str.contains('Order Discounted by customer service|Recurring date changed by customer service')]

        def _parse(x):
            try:
                val = x.message.split(' ')
            except:
                return np.nan
            source = x.agent_name
            try:
                if source == 'System':
                    if val[0] == 'Order' and val[1][0] != '#' and val[1] != 'Confirmation':
                      #  print(val[0],  val[1])
                        return val[1]
                elif ' '.join(val[:3]) == 'New customer order' and val[5] == 'created.':
                    return val[3]
                elif val[0] == 'Order' and val[1][0] == '#' and val[2] in ['cancelled.',  'shipped',  'STOP']:
                    return val[1][1:]
                elif val[0] == 'Order#' and val[2] in ['cancelled.', 'STOP']:
                    return val[1]
            except IndexError:
                return np.nan
            return np.nan


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
        fir_msk = ((df.p_cust != df.customer_id)  & (~df.n_cust.isna()))  &  (df.order_id.isna())
        lst_msk = (df.n_cust != df.customer_id) &  (df.order_id.isna())

        #df['index']  =  df.index
        df.loc[fir_msk] = df.loc[fir_msk].reset_index(drop=False).drop('order_id', axis=1).merge(
            df.loc[~df.order_id.isna(), ['customer_id', 'order_id']].drop_duplicates('customer_id', keep='first'),
            on='customer_id', how='left').set_index('index',drop=True)

        lst_msk = (df.n_cust != df.customer_id) & (df.order_id.isna())
        df.loc[lst_msk] = df.loc[lst_msk].reset_index(drop=False).drop('order_id', axis=1).merge(
            df.loc[~df.order_id.isna(), ['customer_id', 'order_id']].drop_duplicates('customer_id', keep='last'),
            on='customer_id').set_index('index', drop=True)
        df = df.set_index(['customer_id', 'date_created'], drop=False).sort_index()
        df.order_id.fillna(method='ffill', inplace=True)
        df = df.reset_index(drop=True).set_index(['customer_id', 'date_created', 'order_id'], drop=False).sort_index()
        df['note_index'] = df.groupby(level=[0])['message'].cumcount()
        # Set Remaining indexes
        df = df.dropna()
        df.customer_id = df.customer_id.astype(int)
        df.note_index = df.note_index.astype(int)
        return df.drop(columns=['p_cust', 'n_cust']).reset_index(drop=True)

    def global_update(self, df):
        return

