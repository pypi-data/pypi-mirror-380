from models.db import Db, pd, np
from models.orders import Orders
from models.order_cycles import OrderCycles
import datetime as dt
from threading import Thread


class InternalStatus(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'crm_global', 'internal_orders')
        self.set_constraint('internal_orders_pk', ['crm_id', 'order_id'])
        self.crm_id = crm_id


class InternalChangeLog(Db):
    def __init__(self, db, crm_id):
        Db.__init__(db, 'crm_global', 'internal_change_log')
        # Transactional Model. No Constraints
        self.crm_id = crm_id


class InternalOrders:
    def __init__(self, db, crm_id):
        self.status = InternalStatus(db, crm_id)
        self.change_log = InternalChangeLog(db, crm_id)
        self.orders = Orders(db, crm_id)
        self.oc = OrderCycles(db, crm_id)
        self.crm_id = crm_id
        self.oc_sk = f'{self.oc.schema}.{self.oc.table}'
        self.cl_sk = f'{self.change_log.schema}.{self.change_log.table}'
        self.or_sk = f'{self.orders.schema}.{self.orders.table}'
        self.st_sk = f'{self.status.schema}.{self.status.table}'

    def _exec(self, *threads):
        for t in threads:
            t.start()
        for t in threads:
            self._join(t)

    @staticmethod
    def _join(t):
        try:
            t.join()
        except:
            pass

    def pause(self, df, user='internal'):
        self._exec(
            Thread(target=self.change_log.upsert, args=(df,)),
            Thread(target=self.status.update_recurring_status, args=(df.order_id.tolist(), 0)),
            Thread(target=self.orders.update_recurring_status, args=(df.order_id.tolist(), 0))
        )

    def unpause(self, df, user='internal'):
        self._exec(
            Thread(target=self.change_log.upsert, args=(df,)),
            Thread(target=self.status.update_recurring_status, args=(df.order_id.tolist(), 1)),
            Thread(target=self.orders.update_recurring_status, args=(df.order_id.tolist(), 1))
        )

    def refund_log(self, df, user='internal'):
        d = df[['order_id', 'refund_amount', 'status', 'user']].copy()
        self._exec(
            Thread(target=self.change_log.upsert, args=(df,)),
            Thread(target=self.status.refund, args=(df,)),

        )

    def extend(self, df, user='internal'):
        if 'extended_date' not in df.columns:
            d = df[['order_id', 'days', 'status', 'user']].copy()
            ords = self.oc.get(['order_id', 'bc_inferred as billing_cycle', 'time_stamp'],
                               where="order_id = ANY(ARRAY{df.order_id.tolist()}) and crm_id='{self.crm_id}'")
            ords = ords.merge(d, on='order_id', how='left')
            bc_msk = ords.billing_cycle > 0
            calc = ords.loc[bc_msk]
            calc.days += 30
            ords.loc[bc_msk, ['extended_date']] = pd.to_datetime(calc.time_stamp + pd.to_timedelta(calc.days, 'd'))
            calc = ords.loc[~(bc_msk)]
            calc.days += 15
            ords.loc[~(bc_msk), ['extended_date']] = pd.to_datetime(calc.time_stamp + pd.to_timedelta(calc.days, 'd'))
        else:
            ords = df
        if 'crm_id' not in ords.columns:
            ords['crm_id'] = self.crm_id
        self.exec(
            Thread(target=self.change_log.upsert, args=(ords,)),
            Thread(target=self.orders.upsert, args=(ords,)),
        )

        return ords

    def insert_recurring(self, orders):
        _or = orders[['order_id', 'customer_id', 'crm_id', 'decline_reason']].copy()
        _or['is_recurring'] = 0
        _or.loc[(orders.decline_reason.isna()) | (orders.decline_reason == ''), ['is_recurring']] = 1
        _or['crm_id'] = self.crm_id

        def _ctt(df, col):
            return f'unnest(ARRAY{df[col].tolist()}) {col}'

        qry = f"""
                 insert into {self.st_sk}
                         select a.order_id, a.crm_id, a.customer_id, a.is_recurring 
                         from (select {_ctt(_or, 'order_id')}, {_ctt(_or, 'customer_id')}, {_ctt(_or, 'crm_id')}, {_ctt(_or, 'is_recurring')}) a 
                             left join  {self.st_sk} b on b.crm_id = a.crm_id and b.order_id = a.order_id
                         where b.order_id is null            

             """
        self.engine.execute(qry)
        return self.sync_recurring(_or)

    def sync_recurring(self, orders=None):
        a_sel = False
        if orders is not None:
            a_sel = f"(select * from {self._or_sk} where order_id = Any(Array{orders.order_id.tolist()}::int[]) and crm_id='{self.crm_id}')"
        qry = f"""        
                update {self.or_sk}  
                set {self.or_sk}.is_recurring = b.is_recurring 
                from select * from {a_sel if a_sel else self.or_sk} a 
                left join {self.st_sk} b on b.order_id = a.order_id and a.crm_id ='{self.crm_id}' and b.crm_id = a.crm_id
                where b.order_id= {self.or_sk}.order_id and b.crm_id = {self.or_sk}.crm_id               
                    
            """
        return self.orders.engine.execute(qry)

