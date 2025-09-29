from models.db import Db, pd
from threading import Thread, Lock
from models import config


class Orders(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'crm_global', 'orders')
        self.set_constraint('orders_pk', ['order_id', 'crm_id', 'month_date'])
        self._crm_id = crm_id
        self._oc_cols = ['bc_inferred', 'attempt_count', 'retry_attempt_count', 'step', 'ancestor_id']

    def get_orders_by_customer(self, order_ids=False, customer_ids=False):
        qry = None
        if order_ids and len(order_ids) > 50:
            if not isinstance(order_ids, list):
                order_ids = [order_ids]
            qry = """
               select a.order_id from {s}.{t} as a
               inner join (select distinct(a.customer_id) as customer_id, crm_id from {s}.{t} as a
                           inner join unnest(ARRAY{oids}::int[]) as b(order_id) on a.order_id = b.order_id
                           where a.customer_id <> 0 and a.crm_id = '{c}'
                    ) as b on b.customer_id = a.customer_id  and a.crm_id = b.crm_id
               where a.customer_id <> 0 and a.crm_id = '{c}'
                       """.format(s=self.schema, t=self.table, c=self._crm_id, r=self._append_relation(), oids=list(set(order_ids)))

        elif order_ids:
            if not isinstance(order_ids, list):
                order_ids = [order_ids]
            qry = """SELECT order_id FROM {r} 
            WHERE customer_id <> 0 AND crm_id = '{c}' AND customer_id in( select customer_id from {r} where order_id in({oids}))
            """.format(c=self._crm_id, r=self._append_relation(), oids=self._make_list(list(set(order_ids))))

        elif customer_ids and len(customer_ids) > 500:
            qry = """select a.order_id from {s}.{t} as a
                     inner join unnest(ARRAY{cids}::int) as b(cid) on a.customer_id = b.cid
                       """.format(c=self._crm_id, s=self.schema, t=self.table, r=self._append_relation(), cids=list(set(customer_ids)))
        elif customer_ids:
            qry = """SELECT order_id FROM {r} 
            WHERE customer_id <> 0 and customer_id in({cids})
            """.format(c=self._crm_id, r=self._append_relation(), cids=self._make_list(list(set(customer_ids))))

        else:
            raise ValueError("you must pass either order_ids or customer_ids as a list or set")
        return[str(q[0]) for q in self.engine.execute(qry+""" AND order_id <> 0 ORDER BY order_id""")]

    def update_recurring_status(self, order_ids, status=0):
        self.engine.execute(f"""
        Update {self.schema}.{self.table} 
        set is_recurring = {status} 
        where order_id = Any(Array{order_ids}::int[])
        and crm_id = '{self._crm_id}'
        """)

    def get_orders_by_id(self, ids, cols=False):
        return self.get(cols, where=f"""
         where crm_id = '{self._crm_id}' 
         and  order_id = ANY(ARRAY{ids}::bigint[])""")

    def daily_approval_by_gateway(self, gateway_id, date):
        return self.engine.execute(
            f"""select case when o_count=0 then 1         
                        else (case when approved  = 0 then 0 else approved::numeric /o_count::numeric end)::numeric end   
                        from(
                            select sum (case when decline_reason is null then 1 else 0 end) approved, count(order_id) o_count 
                            from {self.schema}.{self.table}
                            where  time_stamp  >= '{date}'::date and gateway_id =  {gateway_id} and crm_id  = '{self._crm_id}'
             
                        ) a """).scalar()

    def recent_orders_by_gateway(self, gateway_id, limit, cols=['gateway_id', 'order_id', 'decline_reason'], **kwargs):
        _whr = lambda x: f"""
        where crm_id = '{self._crm_id}' 
        and  gateway_id = {int(x)}
        order by gateway_id, order_id desc
        limit {limit}
        """
        if isinstance(gateway_id, list):
            _lock = Lock()
            df = None

            def _getter(gid):
                nonlocal _lock, df, _whr
                we = _whr(gid)
               # print(we)
                res = self.get(cols, where=we)
                _lock.acquire()
                if isinstance(res, (pd.DataFrame, pd.Series)):
                    df = res if df is None else df.append(res)
                _lock.release()

            threads = []

            def _join():
                nonlocal threads
                for t in threads:
                    t.join()
                threads = []

            for i in range(len(gateway_id)):
                _getter(gateway_id[i])
                #threads.append(Thread(target=_getter, args=(gateway_id[i],)))
                #threads[len(threads)-1].start()
                if len(threads) > 4:
                    _join()
            _join()
            return df
        return self.get(cols, where=_whr(gateway_id))

    def check_recurring(self, oids):
        if not isinstance(oids, list):
            oids = [oids]
        return self.get(['order_id'], where=f"""        
                where crm_id='{self._crm_id}'
                and is_recurring > 0 
                and order_id = any(ARRAY{oids}::int[])""").order_id.tolist()

    def get_orders_by_recurring(self, cols=False, constrain_crm=False, is_test=False):
        b_cols = []
        a_cols = []
        for c in cols:
            if c in self._oc_cols:
                b_cols.append(f'b.{c}')
            else:
                a_cols.append(f'a.{c}')
        if len(b_cols):
            qry = f""" SELECT {','.join(a_cols)}, {','.join(b_cols)}  
                               From crm_global.orders as a
                               INNER JOIN augmented_data.order_cycles as b 
                               on b.order_id = a.order_id and a.crm_id = b.crm_id
                               where a.is_recurring > 0 and a.decline_reason is null
                                    -- and (a.on_hold is null or a.on_hold = 0)
                                    {f"and a.crm_id ='{self._crm_id}'" if constrain_crm else ''}
                                    and is_test_cc {'= 1' if is_test else '<> 1'}  
                                     and coalesce(a.is_blacklisted, 0) = 0
                                       and coalesce(a.is_chargeback, 0) = 0
                             
                               """

          #  print(qry)
            ret = pd.read_sql(qry, self.engine)
            return ret
        return self.get(cols, where=f"""
        where is_recurring > 0 
        and coalesce(is_blacklisted, 0) = 0
         and coalesce(is_chargeback, 0) = 0
        {f"and crm_id= '{self._crm_id}'" if constrain_crm else ''}""")

    def get_orders_by_recurring2(self, cols=False, constrain_crm=False, is_test=False, customer_ids=None):
        if customer_ids and not isinstance(customer_ids, list):
            customer_ids = [customer_ids]
        b_cols = []
        a_cols = []
        for c in cols:
            if c in self._oc_cols:
                b_cols.append(f'b.{c}')
            else:
                a_cols.append(f'a.{c}')
        if len(b_cols):
            qry = f""" SELECT {','.join(a_cols)}, {','.join(b_cols)}  
                               From crm_global.orders as a
                               INNER JOIN augmented_data.order_cycles as b
                               on b.order_id = a.order_id and a.crm_id = b.crm_id
                               where
                                     a.is_recurring > 0 and
                                     a.decline_reason is null
                                     {f"and a.customer_id = any(ARRAY{customer_ids}::int[])" if customer_ids else ""}
                                   -- and (a.on_hold is null or a.on_hold = 0)
                                    and coalesce(a.is_blacklisted, 0) = 0
                                       and coalesce(a.is_chargeback, 0) = 0
                                    {f"and a.crm_id ='{self._crm_id}'" if constrain_crm else ''}
                                    and is_test_cc {'= 1' if is_test else '<> 1'}  


                               """

            ret = pd.read_sql(qry, self.engine)
            return ret
        return self.get(cols,
                        where=f"""where is_recurring > 0 
                                       and coalesce(is_blacklisted, 0) = 0
                                       and coalesce(is_chargeback, 0) = 0
                        {f"and crm_id= '{self._crm_id}'" if constrain_crm else ''}""")

    def max_last_modified(self):
        return self.max('last_modified', f"where crm_id = '{self._crm_id}'")

    def max_time_stamp(self):
        return self.max('time_stamp', f"where crm_id = '{self._crm_id}'")

    def flag_extended(self, native_order_ids):
        tbl = f'{self.schema}.{self.table}'
        self.engine.execute(f"""update {self.schema}.{self.table} set is_extended = 1 
                                where {tbl}.crm_id = '{self._crm_id}'
                                and {tbl}.decline_reason is not null
                                and {tbl}.native_order_id = any(ARRAY{native_order_ids})
                                """)

    def flag_all_extended(self):
        tbl = f'{self.schema}.{self.table}'
        self.engine.execute(f""" update {tbl}                             
                            set is_extended = 1
                            from
                            (select distinct(native_order_id) from {self.schema}.system_notes 
                            where crm_id = '{self._crm_id}' and note ilike '%%trial extended%%' ) ext
                            where {tbl}.native_order_id = ext.native_order_id                             
                            and {tbl}.crm_id = '{self._crm_id}'
                            and {tbl}.decline_reason is not null
                            """)

    def update_recurring(self, df, min_ts):
        df = df.loc[(df.is_recurring.astype(float) == 1) & (df.on_hold.astype(float) != 1)]
        self.engine.execute(f"""               
                UPDATE {self.schema}.{self.table}
                SET is_recurring = 1,
                on_hold = 0              
                where {self.schema}.{self.table}.crm_id = '{self._crm_id}'
                and {self.schema}.{self.table}.order_id = any(ARRAY{df.order_id.tolist()}::bigint[])
                and month_date >= '{min_ts}'::date 
           """, self.engine)
        # self.engine.execute(f"""
        #                 UPDATE {self.schema}.{self.table}
        #                 SET is_recurring = 0,
        #                 on_hold = 1
        #                 where {self.schema}.{self.table}.crm_id = '{self._crm_id}'
        #                 and month_date >= '{min_ts}'::date
        #                 and is_recurring = 1
        #                 and {self.schema}.{self.table}.order_id <> any(ARRAY{df.order_id.tolist()}::bigint[])
        #
        #            """, self.engine)

    def delete_all(self):
        self.engine.execute(f"""delete from {self.schema}.{self.table} where crm_id='{self._crm_id}'""")

    def set_cust_last_modified(self, customer_id, max_inc=500):
        import datetime as dt
        if not isinstance(customer_id, list):
            customer_id = [customer_id]
        sdex = 0
        err = ''
        while sdex <= len(customer_id):
            cids = customer_id[sdex: sdex+max_inc]
            try:
                self.engine.execute(f"""
                    UPDATE {self.schema}.{self.table}
                    set cust_last_modified = '{dt.datetime.now()-dt.timedelta(hours=config.timeOffset)}'
                    where customer_id = any(ARRAY{cids}::int[]) and crm_id = '{self._crm_id}'
                                        """)
            except Exception as e:
                return False, f'Customer Last Modified error: {str(e)}'

            sdex += max_inc
        return True, ''


class EmployeeNotes(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, crm_id, 'employee_notes')
        self._crm_id = crm_id
        self.set_constraint('employee_notes_pk', ['date_time', 'order_id', 'note_index'])

    def delete_all(self):
        self.engine.execute(f"""delete from {self.schema}.{self.table} where crm_id='{self._crm_id}'""")


class SystemNotes(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, crm_id, 'system_notes')
        self._crm_id = crm_id
        self.set_constraint('system_notes_pk', ['date_time', 'order_id', 'note_index'])

    def delete_all(self):
        self.engine.execute(f"""delete from {self.schema}.{self.table} where crm_id='{self._crm_id}'""")


class OrdersCCFirst8(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'crm_global', 'cc_first_8')
        self.set_constraint('cc_first_8_pk', ['order_id', 'crm_id'])