from models.db import Db, pd
import datetime as dt


class SSCCont(Db):
    _time_cols = ['order_dt', 'rebilled_dt', 'due_dt']

    def __init__(self, db):
        Db.__init__(self, db, 'whitelabel', 'straight_sale_continuity_orders')
        #self.set_constraint('orders_pk', ['order_id', 'crm_id'])

    def get(self, columns=False, where='', orderBy=False):
        _cols = '*'
        _orderBy = ''
        if columns:
            _cols = ','.join(columns)
        if orderBy:
            _orderBy = "ORDER BY {}".format(orderBy)

        stmt = """SELECT {c} FROM {tbl} {whr} {ob} 
        """.format(c=_cols, ob=_orderBy, tbl=self.table, whr=where)

        df = pd.read_sql(stmt, self.engine).fillna("")
        return df

    @staticmethod
    def d2s(days):
        return days * 84000

    @staticmethod
    def _get_time_cols(df):
        return list(set(SSCCont._time_cols) - (set(SSCCont._time_cols) - set(list(df.columns))))

    @staticmethod
    def time_to_datetime(df):
        cols = SSCCont._get_time_cols(df)
        for c in cols:
            df[c] = pd.to_datetime(pd.to_datetime(df[c], unit='s') - dt.timedelta(hours=4))
        return df

    @staticmethod
    def time_to_utc(df):
        cols = SSCCont._get_time_cols(df)
        df[cols] = df[cols].apply(
            lambda x: (pd.to_datetime(x + dt.timedelta(hours=4)) - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s'),
            axis=1)
        return df

    def get_recurring(self, columns=['order_id', 'step', 'due_dt', 'order_dt','initial_mid','rebill_mid']):
        cols = '*'
        if columns and len(columns):
            cols = self.col_stmt(columns)
        df = pd.read_sql(f""" select {cols}
                              from {self.table} where due_dt > 0 """, self.engine)
        return self.time_to_datetime(df)

    def get_by_order_list(self, oids, cols=False, format_dt=False):
        joined = "','".join(oids)
        return self.get(cols, where=f"where order_id in('{joined}')")

    def get_by_interval(self, columns=False, interval=30, is_recurring=True):
        rec = ' and due_dt > 0 '
        if not is_recurring:
            rec = 'and due_dt = 0'

        df = self.get(columns=columns, where=
        f" where order_dt > UNIX_TIMESTAMP() -  UNIX_TIMESTAMP(DATE_SUB(now(),interval {interval} Day)) {rec}")
        return self.time_to_datetime(df)

    def upsert(self, df):
        return self