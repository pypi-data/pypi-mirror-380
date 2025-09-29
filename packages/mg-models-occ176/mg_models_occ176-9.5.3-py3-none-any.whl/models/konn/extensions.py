from models.db import Db, pd, np
import datetime as dt


class Extensions(Db):
    col_map = {'customerId': 'customer_id'}

    def __init__(self, db, crm_id):
        Db.__init__(self, db, f'crm_global', 'orders')
        self.set_constraint('extensions_pk', ['crm_id', 'customer_id', 'billing_cycle'])
        self._crm_id = crm_id

    def update(self, df):
        df = df.rename(columns=self.col_map)
        df = df.merge(pd.read_sql(f"""SELECT order_id, time_stamp, bc_inferred as billing_cycle 
                                where customer_id = ANY(ARRAY{df.customer_id.tolist})
                                AND is_recurring = 1
                                AND crm_id = '{self._crm_id}'
                                """, self.engine))
        df['extended_date'] = np.nan
        df.loc[(df.billing_cycle == 0) & (~df.extend_by == 0), 'extended_date'] = pd.to_datetime(df.time_stamp + dt.timedelta(days=15+df.extend_by)).dt.date
        df.loc[(df.billing_cycle == 0) & (~df.extend_by == 0), 'extended_date'] = pd.to_datetime(df.time_stamp + dt.timedelta(days=15 + df.extend_by))