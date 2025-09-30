from models.db import Db, pd, np, Session
from models.offer_globals import OfferGlobals
from models.campaigns import Campaigns
from models.orders import Orders

import math
from time import sleep
from threading import Thread
import datetime as dt
import threading
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 4000)
pd.set_option('display.width', 3000)
pd.set_option('display.max_colwidth', 3000)


class OrderCycles(Db):
    def __init__(self, db, crm_id, account_id='54407332'):
        Db.__init__(self, db, 'augmented_data', 'order_cycles')
        self.set_constraint('order_cycles_pk', ['order_id', 'crm_id', 'month_date'])
        self._crm_id = crm_id
        self.crm_id = crm_id
        self._offer_globals = OfferGlobals(db, account_id)
        self._campaigns = Campaigns(db, account_id)
        self._account_id = account_id
        self.session = False
        self._glob_ords = Orders(db, crm_id)

    def close_session(self):
        if self.session:
            self.session.close()
        return self

    def set_session(self):
        if not self.session:
            self.session = Session(self.engine)
        return self

    def _get_all_cids(self):
        return pd.read_sql(f""" 
                SELECT distinct(customer_id) from crm_global.orders where crm_id = '{self._crm_id}'
            """, self.engine).customer_id.tolist()

    def _get_batch_size(self, customer_ids, max_batch_size,min_batch_size, max_threads ):
        batch_size = math.ceil(len(customer_ids) / max_threads)
        if batch_size > max_batch_size:
            batch_size = max_batch_size
        elif batch_size < min_batch_size:
            batch_size = min_batch_size
        return batch_size

    def get_billing_model(self, recurring_parent_ids):
        try:
            conn = self.engine.raw_connection()
            cur = conn.cursor()

            cur.execute("""
                CALL augmented_data.billing_cycle_subset(ARRAY{}::numeric[])
            """.format(recurring_parent_ids))
            df = pd.read_sql("""select order_id::text, bc_inferred::int from temp_billing_cycle_subset""", conn)
            cur.close()
            conn.commit()
            conn.close()
            return df
        except Exception as e:
            print(e)
            try:
                cur.close()
            except:
                pass
            try:
                conn.rollback()
            except:
                pass
            try:
                conn.close()
            except:
                pass
        return False

    def get_last_child_v(self, parent_ids):
        qry = """
                SELECT parent_id::text as order_id, order_id::text as last_child, time_stamp as time_stamp_c, decline_reason
                FROM augmented_data.order_cycles
                WHERE order_id in( 
                    SELECT a.last_child from(
                        SELECT parent_id, max(order_id) as last_child
                        FROM augmented_data.order_cycles 
                        WHERE parent_id in({}) and parent_id != order_id
                GROUP BY parent_id
                )as a)""".format(','.join(parent_ids))

        df = pd.read_sql(qry, self.engine)

        return df

    def get_last_child_w(self, parent_ids, crm_ids):
        qry = f"""
                SELECT b.crm_id, b.order_id::int, c.last_child::int::text, c.time_stamp as last_retry_date, d.decline_reason
                FROM (SELECT unnest(ARRAY{parent_ids}::int[]) order_id, unnest(ARRAY{crm_ids}::text[]) crm_id ) as a
                INNER JOIN augmented_data.order_cycles as b on a.crm_id = b.crm_id and a.order_id = b.order_id
                INNER JOIN (
                        SELECT crm_id, parent_id, max(order_id) as last_child, max(time_stamp) as time_stamp
                        FROM augmented_data.order_cycles
                        GROUP BY crm_id, parent_id
                )as c on a.crm_id = c.crm_id and a.order_id = c.parent_id
                INNER JOIN crm_global.orders as d on d.order_id = c.last_child and d.crm_id = c.crm_id
                where b.order_id != last_child
                ORDER BY crm_id, last_child desc
                """

        df = pd.read_sql(qry, self.engine)

        return df

    def get_last_child_x(self, parent_ids, crm_ids):
        df = None

        try:
            sess = Session(self.engine).work_mem('500MB')
            sess.temp_table_from_arrays('t_lc_ids', order_id=parent_ids, crm_id=crm_ids)

            qry = f"""
                            SELECT a.crm_id, a.order_id::int, c.last_child::int::text, 
                            c.time_stamp as last_retry_date, d.decline_reason, d.gateway_id as proc_gateway
                            FROM t_lc_ids as a                         
                            INNER JOIN (
                                    SELECT b.crm_id, b.parent_id, max(b.order_id) as last_child, max(b.time_stamp) as time_stamp
                                    FROM t_lc_ids a
                                    INNER JOIN (select crm_id, order_id, time_stamp, parent_id from augmented_data.order_cycles) b 
                                    on a.crm_id = b.crm_id and a.order_id = b.parent_id
                                    GROUP BY b.crm_id, b.parent_id
                            )as c on a.crm_id = c.crm_id and a.order_id = c.parent_id
                            INNER JOIN (select crm_id, order_id, decline_reason, gateway_id from crm_global.orders) as d on d.order_id = c.last_child and d.crm_id = c.crm_id
                            where a.order_id != last_child
                            ORDER BY crm_id, last_child desc
                         """
            print(dt.datetime.now())
            df = pd.read_sql(qry, sess.conn)
            print(dt.datetime.now())
        except Exception as e:
            sess.conn.rollback()
            sess.close()
            raise e
        print('lc done')
        return df

    def get_last_child_y(self, crm_id, parent_ids=False,  start_date='2018-01-01', is_recurring=False):

        if isinstance(parent_ids, list):

            start_date = self.engine.execute(f"""select month_date from crm_global.orders where order_id = {min(parent_ids)}""").scalar()
        if not isinstance(is_recurring, bool) and is_recurring == 1:
            ir_dt = self.engine.execute(f"""select min(month_date) from crm_global.orders where is_recurring = {is_recurring}""").scalar()
            if isinstance(start_date, str):
                start_date = ir_dt
            elif ir_dt > start_date:
                start_date = ir_dt

        qry = f"""
                SELECT a.crm_id,
                           a.parent_id::int  AS order_id,
                           c.order_id::int   AS last_child,
                           c.time_stamp AS last_retry_date,
                           c.decline_reason,
                           c.gateway_id AS proc_gateway
                    FROM (SELECT crm_id, parent_id, max(order_id) AS last_order_id
                          FROM augmented_data.order_cycles
                          WHERE  month_date >= '{start_date}'::timestamp
                                 and crm_id = '{self.crm_id}'                                 
                                {f'and parent_id = any(ARRAY{parent_ids})' if False else ''}
                          GROUP BY crm_id, parent_id) AS a
                    --          INNER JOIN augmented_data.order_cycles AS "b" ON b.crm_id = a.crm_id AND b.order_id = a.last_order_id
                             INNER JOIN crm_global.orders AS c
                                        ON c.crm_id = a.crm_id AND c.order_id = a.last_order_id AND c.month_date >= '{start_date}'::timestamp
                             {f'''INNER JOIN (SELECT crm_id, order_id FROM crm_global.orders WHERE is_recurring = {is_recurring}) AS d
                                        ON d.crm_id = a.crm_id AND d.order_id = a.parent_id''' if not isinstance(is_recurring, bool) else ''}
                    WHERE a.parent_id <> c.order_id
                      AND a.crm_id = '{self.crm_id}';

                            """
        print(dt.datetime.now())
        df = pd.read_sql(qry, self.engine)
        if parent_ids:
            df = df.loc[df.order_id.isin(parent_ids)]
        print(dt.datetime.now())
        return df

    def get_last_child(self, crm_id, parent_ids=False,  start_date='2018-01-01', is_recurring=False):

        if isinstance(parent_ids, list):

            start_date = self.engine.execute(f"""select month_date from crm_global.orders where order_id = {min(parent_ids)}""").scalar()
        if not isinstance(is_recurring, bool) and is_recurring == 1:
            ir_dt = self.engine.execute(f"""select min(month_date) from crm_global.orders where is_recurring = {is_recurring}""").scalar()
            if isinstance(start_date, str):
                start_date = ir_dt
            elif ir_dt > start_date:
                start_date = ir_dt

        qry = f"""
                SELECT a.crm_id,
                           a.order_id::int,
                           a.last_child,
                           b.time_stamp AS last_retry_date,
                           b.decline_reason,
                           b.gateway_id AS proc_gateway
                    FROM {self.schema}.{self.table}  a
                    INNER JOIN (select order_id ,crm_id, time_stamp, decline_reason, gateway_id from crm_global.orders where month_date >= '{start_date}'::date) b on a.crm_id=b.crm_id 
                                and a.last_child = b.order_id 
                     {f'''INNER JOIN (SELECT crm_id, order_id FROM crm_global.orders WHERE is_recurring = {is_recurring}) AS d
                                        ON d.crm_id = a.crm_id AND d.order_id = a.order_id''' if not isinstance(is_recurring, bool) else ''}                   
                    WHERE 
                       a.crm_id = '{self.crm_id}'
                      AND a.month_date >= '{start_date}'::date
                      
                            """
        print(dt.datetime.now())
        df = pd.read_sql(qry, self.engine)
        if parent_ids:
            df = df.loc[df.order_id.isin(parent_ids)]
        print(dt.datetime.now())
        return df

    def get_last_gen(self, ancestor_ids, crm_ids):
        df = None
        if len(ancestor_ids ) <150:
            qry = f"""
                 select crm_id, ancestor_id,
                  max(order_id)::int as last_gen_order_id, 
                  max(time_stamp) as last_gen_time_stamp,
                  max(bc_inferred)::int as last_gen_billing_cycle  
                  from augmented_data.order_cycles b 
                  
                 where decline_reason is null 
                        and  ancestor_id = Any(ARRAY{ancestor_ids}::int[]) 
                        and crm_id = '{crm_ids[0]}'
                 group by crm_id, ancestor_id 

                                  """
            df = pd.read_sql(qry, self.engine)
        else:
            try:
                sess = Session(self.engine).work_mem('500MB')
                sess.temp_table_from_arrays('t_lc_ids', order_id=ancestor_ids, crm_id=crm_ids)

                qry = f"""
                               select b.crm_id, b.ancestor_id,
                                max(b.order_id)::int as last_gen_order_id, 
                                max(b.time_stamp) as last_gen_time_stamp,
                                max(b.bc_inferred)::int as last_gen_billing_cycle  
                               from t_lc_ids a
                               inner join augmented_data.order_cycles b on b.ancestor_id = a.order_id and b.crm_id = a.crm_id
                               where decline_reason is null 
                               group by b.crm_id, b.ancestor_id 
                               
                        """
                df = pd.read_sql(qry, sess.conn)

            except Exception as e:
                sess.conn.rollback()
                sess.close()
                raise e
        print('last_gen_done')
        return df

    def get_attempt_count(self, parent_ids, crm_ids):

        try:
            sess = Session(self.engine).work_mem('500MB')
            sess.temp_table_from_arrays('t_lc_ids', order_id=parent_ids, crm_id=crm_ids)
            qry = f"""                  
                               SELECT a.crm_id, b.parent_id::int as order_id,  count(*)::int as attempt_count 
                               FROM t_lc_ids a
                               INNER JOIN augmented_data.order_cycles b on a.crm_id = b.crm_id and a.order_id = b.parent_id
                               WHERE b.parent_id != b.order_id 
                               AND b.decline_reason is not null                   
                               GROUP BY a.crm_id, b.parent_id   
                       """  # .format(p=','.join(parent_ids))
            df = None
            df = pd.read_sql(qry, sess.conn)
        except Exception as e:
            sess.conn.rollback()
            sess.close()
            raise e
        print('at done')
        sess.close()
        return df.loc[df.order_id.isin(parent_ids)]

    def decline_model_x(self):
        df = pd.read_sql(
            """
            select decline_reason,
                     sum(approved)                                                  as approved,
                     sum(approved_value)                                            AS approved_value,
                     sum(total)                                                     as total,
                     sum(decline_value)                                             AS total_expenses,
                     CASE
                         WHEN sum(simple_expense_formula) / nullif(sum(approved_value), 0) IS NULL THEN 0
                         ELSE sum(simple_expense_formula) / sum(approved_value) END AS margin


                from (
                       Select split_part(a.decline_reason, 'REFID', 1)                 as decline_reason,
                              a.bc_inferred,
                              case
                                  when a.bc_inferred <> max(a.bc_inferred) over w_anc
                                      and last_value(a.decline_reason) over w_par is null
                                      and a.decline_reason is not NULL
                                      and rank() over w_par = count(a.*) over w_par - 1
                                      THEN 1
                                  else 0 END                                           as approved,
                              case
                                  when bc_inferred <> max(a.bc_inferred) over w_anc
                                      and last_value(a.decline_reason) over w_par is null
                                      and a.decline_reason is not NULL
                                      and rank() over w_par = count(a.*) over w_par - 1
                                      THEN b.order_total -  coalesce(c.chargeback_cost, '35')::real - b.amount_refunded_to_date
                                  else 0 END                                           as approved_value,

                              case
                                  when a.decline_reason is not null then coalesce(c.transaction_cost,'0.30')
                                  else 0 end                                           as decline_value,
                              case when a.decline_reason is not null then 1 else 0 end as total,
                              (case
                                   when bc_inferred <> max(a.bc_inferred) over w_anc
                                       and last_value(a.decline_reason) over w_par is null
                                       and a.decline_reason is not NULL
                                       and rank() over w_par = count(a.*) over w_par - 1
                                       THEN b.order_total -
                                            (b.is_chargeback * coalesce(c.chargeback_cost, '35'))::real - b.amount_refunded_to_date else 0 END - case
                                                    when a.decline_reason is not null then coalesce(c.transaction_cost,'0.30')::real
                                                    else 0 end) AS simple_expense_formula

                       from augmented_data.order_cycles AS a
                                LEFT JOIN temp_data.orders AS b ON b.order_id = a.order_id
                                LEFT JOIN (SELECT DISTINCT ON ( a.gateway_id ) a.gateway_id,
                                                  CASE
                                                      WHEN b.approved_transaction_cost IS NULL THEN '0.30'::real
                                                      ELSE b.approved_transaction_cost END AS "transaction_cost",
                                                  CASE
                                                      WHEN b.chargeback_cost IS NULL THEN '35.00'::real
                                                      ELSE b.chargeback_cost END AS "chargeback_cost"
                                           FROM ui_accx_module.steps AS a
                                                    LEFT JOIN ui_accx_module.mids AS b ON b.mid_id = a.mid_id
                                    WHERE gateway_id IS NOT NULL) AS "c" ON c.gateway_id = b.gateway_id
                       WHERE /*a.acquisition_date::date > '2020-04-01'
                         AND*/ a.bc_inferred > 0 window w_par as (PARTITION BY a.parent_id, a.bc_inferred order by a.time_stamp asc ROWS between unbounded preceding and unbounded following),
                               w_anc as (PARTITION BY a.ancestor_id order by a.time_stamp asc ROWS between unbounded preceding and unbounded following)

                       ORDER BY a.ancestor_id, a.parent_id, a.order_id
                                  )                                                    as a
                       GROUP BY decline_reason
               order by total desc
            """,
            self.engine
        )
        df['approval_rate'] = 0
        mask = df.approved > 0
        df.loc[mask, 'approval_rate'] = df.loc[mask, 'approved'] / df.loc[mask, 'total']
        df.decline_reason = df.decline_reason.str.strip()
        df.margin = df.margin * 100
        return df

    def decline_model_y(self):
        df = pd.read_sql(
            """
            select _first_message as decline_reason ,
                   _optimised_attempts as max_attempt,
                   _new_margin *100 as margin ,
                   _sample_attempt_count as total
            from augmented_data.min_attempt_decline_ignore()
            """,
            self.engine
        )
        df.decline_reason = df.decline_reason.str.strip()
        return df

    def decline_model_local(self, max_attempts):
        result = None
        threads = []
        _lock = threading.Lock()

        def _iter(sdex, edex):

            nonlocal result
            df = pd.read_sql(
                f"""
                select _first_message as decline_reason,
                       _net_value  as net_revenue,
                       _revenue as revenue,
                       _sample_attempt_count as total
                from augmented_data.min_attempt_decline_ignore2({edex},{sdex})
                """,
                self.engine
            )

            df['attempts'] = sdex
            _lock.acquire()
            if result is None:
                result = df
            else:
                result = result.append(df)
            _lock.release()

        for i in range(1, max_attempts + 1):
            threads.append(threading.Thread(target=_iter, args=(i, max_attempts)))
            threads[i - 1].start()
        for i in range(len(threads)):
            threads[i].join()
        result.sort_values(by=['decline_reason', 'attempts'], inplace=True)
        result.set_index(['decline_reason', 'attempts'], inplace=True)

        grp = result.rename(
            columns={'revenue': 'cum_rev', 'net_revenue': 'cum_net'}
        ).groupby(level=0)
        result = result.join(grp[['cum_rev', 'cum_net']].cumsum())
        if not len(result):
            print('no ds result')
            return None
        result['margin'] = result.cum_net / result.cum_rev
        result = result.drop('total', axis=1).join(grp['total'].max()).replace([np.inf, -np.inf], 0)
        result = result.join(result.rename(columns={'cum_net': 'max_net'}).groupby(level=0).max_net.max()).reset_index()
        result = pd.merge(result, result.loc[result.cum_net == result.max_net, ['decline_reason', 'attempts']].rename(
            columns={'attempts': 'max_attempt'}), on='decline_reason')
        #self.engine.execute("delete if exists from int_log.holds_decline_model")
        # result.to_sql('holds_decline_model', self.engine, schema='int_log', index=False, if_exists='append',
        #               method='multi')

        return result.drop(['revenue', 'net_revenue', 'cum_net'], axis=1)

    def decline_model(self, max_attempts):
        result = None
        threads = []
        _lock = threading.Lock()

        result = pd.read_sql(
            f"""
                       select _first_message as decline_reason,
                              _net_value  as net_revenue,
                              _revenue as revenue,
                              _sample_attempt_count as total,
                              attempts
                       from foreign_decline_models.static_decline_ignore
                       """,
            self.engine
        )
        result.sort_values(by=['decline_reason', 'attempts'], inplace=True)
        result.set_index(['decline_reason', 'attempts'], inplace=True)

        grp = result.rename(
            columns={'revenue': 'cum_rev', 'net_revenue': 'cum_net'}
        ).groupby(level=0)
        result = result.join(grp[['cum_rev', 'cum_net']].cumsum())
        if not len(result):
            print('no ds result')
            return None
        result['margin'] = result.cum_net / result.cum_rev
        result = result.drop('total', axis=1).join(grp['total'].max()).replace([np.inf, -np.inf], 0)
        result = result.join(result.rename(columns={'cum_net': 'max_net'}).groupby(level=0).max_net.max()).reset_index()
        result = pd.merge(result, result.loc[result.cum_net == result.max_net, ['decline_reason', 'attempts']].rename(
            columns={'attempts': 'max_attempt'}), on='decline_reason')
        #self.engine.execute("delete if exists from int_log.holds_decline_model")
        # result.to_sql('holds_decline_model', self.engine, schema='int_log', index=False, if_exists='append',
        #               method='multi')

        return result.drop(['revenue', 'net_revenue', 'cum_net'], axis=1)


    def refresh_legacy(self, is_auto_update, customer_ids=False, max_batch_size=50000, min_batch_size=100, max_threads=2):
        if not customer_ids:
            customer_ids = self._get_all_cids()

        batch_size = self._get_batch_size(customer_ids, max_batch_size, min_batch_size, max_threads)
        t_del = math.ceil(batch_size / 10) * 0.001

        def _run(cids):
            print(f'running oc refresh on {len(cids)} customers')
            conn = None
            cur = None
            try:

                conn = self.engine.raw_connection()

                cur = conn.cursor()
                cur.execute("SET LOCAL work_mem = '2GB'")
                cur.execute(f"""
                    CREATE TEMP TABLE customers_to_table on commit drop as (select unnest(ARRAY [{cids}]::numeric[]) as customer_id);
                """)
                # Init Temp cycle full (the main Table to insert)
                cur.execute(f"""
                            CREATE TEMP TABLE temp_cycle_full
                            (
                                crm_id                   text,
                                order_id                 numeric                 not null
                                    constraint temp_cycle_full_pk
                                        primary key,
                                bc_raw                   numeric,
                                bc_inferred              numeric,
                                bc_increment             integer,
                                attempt_increment        integer,
                                attempt_decrement        integer,
                                attempt_count            integer,
                                retry_attempt_count      integer,
                                real_attempt_count       integer,
                                real_retry_attempt_count integer,
                                last_child               numeric,
                                real_last_child          numeric,
                                parent_id                numeric,
                                campaign_id              numeric,
                                customer_id              numeric,
                                insert_time              timestamp default now() not null,
                                decline_reason           text,
                                time_stamp               timestamp,
                                acquisition_date         timestamp,
                                step                     numeric,
                                first_affiliate          text,
                                adv_portfolio            text,
                                existing                 boolean,
                                ancestor_id              numeric
                            )
                                ON COMMIT DROP;
                                """)
                # Init No archive Orders Array (the main temp table to insert)
                cur.execute(f"""
                   CREATE TEMP TABLE orders_array_no_archive ON COMMIT DROP AS (
                    SELECT DISTINCT  ON ( a.order_id ) a.order_id,
                           a.decline_reason,
                           a.gateway_id,
                           a.campaign_id,
                           a.affid,
                           a.affiliate,
                           a.time_stamp,
                           a.acquisition_date,
                           a.customer_id,
                           a.crm_id,
                           a.billing_cycle,
                           coalesce(c.decrement_attempt_count, '0') AS "decrement_attempt_count",
                           c.ancestor_id,
                           main_product_id
                    FROM crm_global.orders AS a
                             {'INNER JOIN customers_to_table AS b ON b.customer_id = a.customer_id' if cids else ''}
                             LEFT JOIN augmented_data.order_cycles AS c
                                       ON c.crm_id = a.crm_id AND c.order_id = a.order_id AND c.month_date = a.month_date
                    WHERE a.crm_id = '{self.crm_id}'
                      AND a.customer_id > '0' AND a.campaign_id <> '1089' AND a.campaign_id <> '1090' /*AND a.customer_id = '223549'*/  /* AND a.month_date > '2020-02-01'*/);
                """)

                # Init archive Orders arraay
                cur.execute(f"""
                    CREATE TEMP TABLE orders_array_archive ON COMMIT DROP AS (
                    SELECT DISTINCT  ON ( a.order_id ) a.order_id,
                           a.decline_reason,
                           a.gateway_id,
                           f.campaign_id,
                           a.affid,
                           a.affiliate,
                           a.time_stamp,
                           a.acquisition_date,
                           a.customer_id,
                           a.crm_id,
                           a.billing_cycle,
                           coalesce(c.decrement_attempt_count, '0') AS "decrement_attempt_count",
                           c.ancestor_id,
                           a.main_product_id
                    FROM crm_global.orders AS a
                            {'INNER JOIN customers_to_table AS b ON b.customer_id = a.customer_id' if cids else ''}
                             LEFT JOIN augmented_data.order_cycles AS c
                                       ON c.crm_id = a.crm_id AND c.order_id = a.order_id AND c.month_date = a.month_date
                             INNER JOIN ui_{self._account_id}_offers.campaigns AS "d" ON d.crm_id = a.crm_id AND d.campaign_id = a.campaign_id AND d.step IS NOT NULL
                             LEFT JOIN (SELECT a.customer_id, a.campaign_id, step, main_product_id
                                        FROM orders_array_no_archive AS "a"
                                                 INNER JOIN (SELECT ancestor_id, max(order_id) AS "order_id"
                                                             FROM orders_array_no_archive
                                                             GROUP BY ancestor_id) AS "b" ON b.order_id = a.order_id
                                                 INNER JOIN ui_{self._account_id}_offers.campaigns AS "c"
                                                            ON c.crm_id = a.crm_id AND c.campaign_id = a.campaign_id AND
                                                               c.step IS NOT NULL) AS "f" ON f.step = d.step AND f.main_product_id = a.main_product_id AND f.customer_id = a.customer_id
                
                    WHERE a.crm_id = '{self.crm_id}'
                      AND a.customer_id > '0'
                      AND (a.campaign_id = '1089' OR a.campaign_id = '1090') /*AND a.customer_id = '223549'*/ /* AND a.month_date > '2020-02-01'*/);
                """)
                # Consolidate the Archived and Unarchived orders arrays into 1 beautiful thing.
                cur.execute(f"""
                CREATE TEMP TABLE orders_array ON COMMIT DROP AS (
                    SELECT a.order_id,
                           a.decline_reason,
                           a.gateway_id,
                           a.campaign_id,
                           a.affid,
                           a.affiliate,
                           a.time_stamp,
                           a.acquisition_date,
                           a.customer_id,
                           a.crm_id,
                           a.billing_cycle,
                           a.decrement_attempt_count AS "decrement_attempt_count"
                    FROM ( SELECT * FROM orders_array_no_archive
                        UNION ALL
                        SELECT * FROM orders_array_archive ) AS "a");
                """)
                # Add Constraints to orders array
                cur.execute(f"""
                                alter table orders_array
                                add constraint orders_array_pkey
                                    primary key (order_id);
                                """)
                # Add the decrement attempt to orders array
                cur.execute(f"""
                            UPDATE orders_array
                            SET decrement_attempt_count = '1'
                            FROM (SELECT decline_reason FROM augmented_data.decline_reason_decrement) AS a
                            WHERE lower(orders_array.decline_reason) = lower(a.decline_reason)
                              AND orders_array.decline_reason IS NOT NULL
                              AND orders_array.decrement_attempt_count = '0';

                                """)
                cur.execute(f"""
                            INSERT INTO temp_cycle_full (crm_id, order_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                             attempt_count,
                             retry_attempt_count, parent_id, campaign_id, customer_id, insert_time,
                             decline_reason,
                             time_stamp, acquisition_date, step, first_affiliate, adv_portfolio, existing,
                             attempt_decrement) (
                            SELECT a.crm_id,
                                   a.order_id,
                                   a.billing_cycle::smallint,
                                   CASE WHEN a.customer_id = '0' THEN '0' ELSE e.b_c END::smallint,
                                   NULL::smallint,
                                   NULL::smallint,
                                   NULL::smallint,
                                   NULL::smallint,
                                   NULL::bigint,
                                   a.campaign_id,
                                   a.customer_id,
                                   a.time_stamp,
                                   a.decline_reason,
                                   a.time_stamp::timestamp with time zone,
                                   e.acquisition_date,
                                   e.step::smallint,
                                   e.affiliate::text,
                                   CASE WHEN e.non_name IS NULL THEN 'undefined' ELSE e.non_name END,
                                   CASE WHEN b.order_id IS NULL THEN FALSE::boolean ELSE TRUE::boolean END,
                                   a.decrement_attempt_count
                            FROM orders_array AS a
                                     LEFT JOIN (SELECT max(order_id) AS order_id
                                                FROM augmented_data.order_cycles
                                                WHERE crm_id = '{self.crm_id}'
                                                GROUP BY order_id) AS b
                                               ON (b.order_id = a.order_id)
                                     LEFT JOIN (SELECT a.customer_id,
                                                       a.step,
                                                       a.order_id,
                                                       a.campaign_id,
                                                       (sum(a.b_c)
                                                        OVER ( PARTITION BY a.customer_id, a.non_name, a.step ORDER BY a.order_id ASC)) AS b_c,
                                                       e.time_stamp_to_acquisition_date                                                 AS acquisition_date,
                                                       e.affiliate,
                                                       a.non_name
                                                FROM (SELECT a.customer_id,
                                                             a.step,
                                                             a.order_id,
                                                             a.campaign_id,
                                                             a.incrementer,
                                                             a.non_name,
                                                             (lag(a.incrementer, '1'::smallint, '0'::smallint)
                                                              OVER ( PARTITION BY a.customer_id, a.non_name, a.step ORDER BY a.order_id ASC)) AS b_c
                                                      FROM (SELECT a.customer_id,
                                                                   a.step,
                                                                   a.order_id,
                                                                   a.campaign_id,
                                                                   b.decline_reason,
                                                                   CASE
                                                                       WHEN b.decline_reason IS NULL THEN '1'::smallint
                                                                       ELSE '0'::smallint END AS incrementer,
                                                                   a.non_name

                                                            FROM ((SELECT DISTINCT ON (a.order_id) a.order_id,
                                                                                                   customer_id,
                                                                                                   a.campaign_id,
                                                                                                   b.step,
                                                                                                   c.non_name
                                                                   FROM orders_array AS a
                                                                            INNER JOIN (SELECT min(a.step) AS step,
                                                                                               a.rebill_campaign
                                                                                        FROM (SELECT a.*,
                                                                                                     b.step,
                                                                                                     a.name AS non_name,
                                                                                                     b.charge_product_id,
                                                                                                     b.rebill_product_id,
                                                                                                     b.rebill_campaign,
                                                                                                     b.saves_campaign,
                                                                                                     c.master_id,
                                                                                                     d.campaign_id,
                                                                                                     d.provider
                                                                                              FROM ui_{self._account_id}_offers.offers as a
                                                                                                       LEFT JOIN (SELECT *
                                                                                                                  FROM ui_{self._account_id}_offers.offer_globals
                                                                                                                  WHERE crm_id = '{self.crm_id}') as b
                                                                                                                 on a.offer_id = b.offer_id
                                                                                                       LEFT JOIN (SELECT *
                                                                                                                  FROM ui_{self._account_id}_offers.master_campaigns
                                                                                                                  WHERE crm_id = '{self.crm_id}') as c
                                                                                                                 on c.offer_id = a.offer_id and b.step = c.step
                                                                                                       LEFT JOIN (SELECT * FROM ui_{self._account_id}_offers.campaigns WHERE crm_id = '{self.crm_id}') as d
                                                                                                                 on d.master_id = c.master_id and d.step = c.step
                                                                                              WHERE b.rebill_campaign IS NOT NULL
                                                                                              ORDER BY b.rebill_campaign) AS a
                                                                                        GROUP BY a.rebill_campaign) AS b
                                                                                       ON (b.rebill_campaign = a.campaign_id)
                                                                            LEFT JOIN (SELECT b.rebill_campaign, a.name AS non_name
                                                                                       FROM ui_{self._account_id}_offers.offers AS a
                                                                                                LEFT JOIN ui_{self._account_id}_offers.offer_globals as b
                                                                                                          on a.offer_id = b.offer_id
                                                                                       WHERE b.crm_id = '{self.crm_id}') AS c
                                                                                      ON (c.rebill_campaign = a.campaign_id)
                                                                   WHERE a.customer_id > '0')
                                                                  UNION ALL
                                                                  (SELECT DISTINCT ON (a.order_id) a.order_id,
                                                                                                   a.customer_id,
                                                                                                   a.campaign_id,
                                                                                                   b.step,
                                                                                                   CASE WHEN b.non_name IS NULL THEN d.name ELSE b.non_name END
                                                                   FROM orders_array AS a
                                                                            INNER JOIN (SELECT a.customer_id,
                                                                                               a.order_id,
                                                                                               a.campaign_id,
                                                                                               a.non_name,
                                                                                               (dense_rank()
                                                                                                OVER ( PARTITION BY a.customer_id, a.non_name ORDER BY a.order_id ASC)) AS step
                                                                                        FROM (SELECT a.order_id,
                                                                                                     a.customer_id,
                                                                                                     a.campaign_id,
                                                                                                     c.non_name,
                                                                                                     (dense_rank()
                                                                                                      OVER ( PARTITION BY a.customer_id, c.non_name, a.campaign_id ORDER BY a.order_id ASC)) AS inter_campaign_order
                                                                                              FROM orders_array AS a
                                                                                                       LEFT JOIN (SELECT min(a.step) AS step,
                                                                                                                         a.rebill_campaign
                                                                                                                  FROM (SELECT a.*,
                                                                                                                               b.step,
                                                                                                                               b.charge_product_id,
                                                                                                                               b.rebill_product_id,
                                                                                                                               b.rebill_campaign,
                                                                                                                               a.name,
                                                                                                                               b.saves_campaign,
                                                                                                                               c.master_id,
                                                                                                                               d.campaign_id,
                                                                                                                               d.provider
                                                                                                                        FROM ui_{self._account_id}_offers.offers as a
                                                                                                                                 LEFT JOIN (SELECT *
                                                                                                                                            FROM ui_{self._account_id}_offers.offer_globals
                                                                                                                                            WHERE crm_id = '{self.crm_id}') as b
                                                                                                                                           on a.offer_id = b.offer_id
                                                                                                                                 LEFT JOIN (SELECT *
                                                                                                                                            FROM ui_{self._account_id}_offers.master_campaigns
                                                                                                                                            WHERE crm_id = '{self.crm_id}') as c
                                                                                                                                           on c.offer_id = a.offer_id and b.step = c.step
                                                                                                                                 LEFT JOIN (SELECT * FROM ui_{self._account_id}_offers.campaigns WHERE crm_id = '{self.crm_id}') as d
                                                                                                                                           on d.master_id = c.master_id and d.step = c.step
                                                                                                                        WHERE b.rebill_campaign IS NOT NULL
                                                                                                                        ORDER BY b.rebill_campaign) AS a
                                                                                                                  GROUP BY a.rebill_campaign) AS b
                                                                                                                 ON (b.rebill_campaign = a.campaign_id)
                                                                                                       LEFT JOIN (SELECT a.*,

                                                                                                                         b.name AS non_name

                                                                                                                  FROM (SELECT * FROM ui_{self._account_id}_offers.campaigns WHERE crm_id = '{self.crm_id}') as a
                                                                                                                           LEFT JOIN ui_{self._account_id}_offers.offers as b
                                                                                                                                     on a.offer_id = b.offer_id


                                                                                                                  ORDER BY a.campaign_id) AS c
                                                                                                                 ON (c.campaign_id = a.campaign_id AND c.crm_id = a.crm_id)
                                                                                              WHERE b.rebill_campaign IS NULL
                                                                                                AND a.customer_id > '0'
                                                                                                AND a.decline_reason IS NULL) AS a
                                                                                        WHERE a.inter_campaign_order = '1'
                                                                                          AND a.customer_id > '0'
                                                                                          AND a.customer_id > '0') AS b
                                                                                       ON (b.customer_id = a.customer_id AND b.campaign_id = a.campaign_id)
                                                                            LEFT JOIN (SELECT a.rebill_campaign
                                                                                       FROM (SELECT a.*,
                                                                                                    b.step,
                                                                                                    b.charge_product_id,
                                                                                                    b.rebill_product_id,
                                                                                                    b.rebill_campaign,
                                                                                                    a.name AS non_name,
                                                                                                    b.saves_campaign,
                                                                                                    c.master_id,
                                                                                                    d.campaign_id,
                                                                                                    d.provider
                                                                                             FROM ui_{self._account_id}_offers.offers as a
                                                                                                      LEFT JOIN (SELECT *
                                                                                                                 FROM ui_{self._account_id}_offers.offer_globals
                                                                                                                 WHERE crm_id = '{self.crm_id}') as b
                                                                                                                on a.offer_id = b.offer_id
                                                                                                      LEFT JOIN (SELECT *
                                                                                                                 FROM ui_{self._account_id}_offers.master_campaigns
                                                                                                                 WHERE crm_id = '{self.crm_id}') as c
                                                                                                                on c.offer_id = a.offer_id and b.step = c.step
                                                                                                      LEFT JOIN (SELECT * FROM ui_{self._account_id}_offers.campaigns WHERE crm_id = '{self.crm_id}') as d
                                                                                                                on d.master_id = c.master_id and d.step = c.step
                                                                                             WHERE b.rebill_campaign IS NOT NULL
                                                                                             ORDER BY b.rebill_campaign) AS a
                                                                                       GROUP BY a.rebill_campaign) AS c
                                                                                      ON (c.rebill_campaign = a.campaign_id)
                                                                            LEFT JOIN (SELECT a.campaign_id, b.name
                                                                                       FROM (SELECT * FROM ui_{self._account_id}_offers.campaigns WHERE crm_id = '{self.crm_id}') as a
                                                                                                LEFT JOIN ui_{self._account_id}_offers.offers AS b
                                                                                                          ON a.offer_id = b.offer_id
                                                                   ) AS d
                                                                                      ON (d.campaign_id = a.campaign_id)
                                                                   WHERE c.rebill_campaign IS NULL
                                                                     AND a.customer_id > '0'
                                                                     AND a.crm_id = '{self.crm_id}'
                                                                  )) AS a
                                                                     LEFT JOIN (SELECT DISTINCT ON (order_id) order_id, decline_reason
                                                                                FROM orders_array) AS b
                                                                               ON (b.order_id = a.order_id)
                                                            ORDER BY a.customer_id, a.step, a.order_id) AS a) AS a
                                                         LEFT JOIN (SELECT a.customer_id,
                                                                           a.affiliate,
                                                                           a.time_stamp AS time_stamp_to_acquisition_date
                                                                    FROM orders_array AS a
                                                                             INNER JOIN (SELECT min(order_id)          AS order_id,
                                                                                                min(orders.time_stamp) AS time_stamp,
                                                                                                customer_id
                                                                                         FROM orders_array AS orders
                                                                                         GROUP BY customer_id) AS b
                                                                                        ON (b.order_id = a.order_id)) AS e
                                                                   ON (e.customer_id = a.customer_id)) AS e
                                               ON (e.order_id = a.order_id));
                                """)
                cur.execute(f"""
                                UPDATE temp_cycle_full
                                SET parent_id = a.parent_id
                                FROM (SELECT a.order_id, CASE WHEN a.bc_inferred = '0' THEN a.order_id ELSE b.order_id END AS parent_id
                                      FROM (SELECT order_id, bc_inferred, customer_id, step, adv_portfolio FROM temp_cycle_full) AS a
                                               LEFT JOIN (SELECT order_id, customer_id, step, adv_portfolio, bc_inferred + '1' AS bc_inferred
                                                          FROM temp_cycle_full
                                                          WHERE decline_reason IS NULL) AS b
                                                         ON (b.customer_id = a.customer_id AND b.step = a.step AND
                                                             b.bc_inferred = a.bc_inferred AND b.adv_portfolio = a.adv_portfolio)
                                     ) AS a
                                WHERE temp_cycle_full.order_id = a.order_id;

                                """)
                cur.execute(f"""
                                UPDATE temp_cycle_full
                                SET ancestor_id = a.ancestor
                                FROM (SELECT customer_id, step, adv_portfolio, min(order_id) AS ancestor
                                      FROM temp_cycle_full
                                      WHERE decline_reason IS NULL
                                      GROUP BY customer_id, step, adv_portfolio) AS a
                                WHERE temp_cycle_full.customer_id = a.customer_id
                                  AND temp_cycle_full.step = a.step
                                  AND temp_cycle_full.adv_portfolio = a.adv_portfolio;
                                """)
                cur.execute(f"""
                            UPDATE temp_cycle_full
                            SET attempt_count      = a.attempt,
                                real_attempt_count = a.non_attempt
                            FROM (SELECT orders.order_id,
                                         CASE
                                             WHEN orders.bc_inferred = '1' THEN
                                                     (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2' -
                                                     (sum(orders.attempt_decrement)
                                                      OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                                             ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1' -
                                                  (sum(orders.attempt_decrement)
                                                   OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                                             END AS attempt,
                                         CASE
                                             WHEN orders.bc_inferred = '1' THEN
                                                     (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2'
                                             ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1'
                                             END AS non_attempt
                                  FROM temp_cycle_full AS orders) AS a
                            WHERE temp_cycle_full.order_id = a.order_id;
                                """)
                cur.execute(f"""
                                UPDATE temp_cycle_full
                                SET real_last_child = a.last_child
                                FROM (SELECT parent_id, max(order_id) AS last_child FROM temp_cycle_full GROUP BY parent_id) AS a
                                WHERE a.parent_id = temp_cycle_full.order_id;

                                """)
                cur.execute(f"""
                            UPDATE temp_cycle_full
                            SET last_child = a.last_child
                            FROM (SELECT parent_id, max(order_id) AS last_child
                                  FROM temp_cycle_full
                                  WHERE attempt_decrement = '0'
                                  GROUP BY parent_id) AS a
                            WHERE a.parent_id = temp_cycle_full.order_id;

                                """)
                cur.execute(f"""
                                UPDATE temp_cycle_full
                                SET retry_attempt_count      = a.retry_attempt_count,
                                    real_retry_attempt_count = a.real_retry_attempt_count
                                FROM (SELECT orders.order_id,
                                             a.attempt_count      AS retry_attempt_count,
                                             a.real_attempt_count AS real_retry_attempt_count

                                      from temp_cycle_full AS orders
                                               LEFT JOIN (SELECT min(parent_id)                                      AS start_id,
                                                                 bc_inferred,
                                                                 adv_portfolio,
                                                                 customer_id,
                                                                 step,
                                                                 count(attempt_count) - '1' - sum(attempt_decrement) AS attempt_count,
                                                                 count(attempt_count) - '1'                          AS real_attempt_count
                                                          FROM temp_cycle_full
                                                          WHERE order_id <> parent_id
                                                          GROUP BY adv_portfolio, customer_id, step, bc_inferred) AS a
                                                         ON (a.customer_id = orders.customer_id AND a.adv_portfolio = orders.adv_portfolio AND
                                                             a.start_id = orders.order_id)
                                      WHERE a.start_id IS NOT NULL) AS a
                                WHERE temp_cycle_full.order_id = a.order_id;
                                """)
                cur.execute(f"""
                            INSERT INTO augmented_data.order_cycles (order_id, crm_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                                         decrement_attempt_count, attempt_count, retry_attempt_count,
                                         real_attempt_count,
                                         real_retry_attempt_count, last_child, real_last_child, parent_id, campaign_id,
                                         customer_id, decline_reason, time_stamp, month_date,
                                         acquisition_date,
                                         step,
                                         first_affiliate, ancestor_id)
                                        (SELECT DISTINCT ON (order_id) order_id,
                                                                       crm_id,
                                                                       bc_raw,
                                                                       bc_inferred,
                                                                       bc_increment,
                                                                       attempt_increment,
                                                                       attempt_decrement,
                                                                       attempt_count,
                                                                       retry_attempt_count,
                                                                       real_attempt_count,
                                                                       real_retry_attempt_count,
                                                                       last_child,
                                                                       real_last_child,
                                                                       parent_id,
                                                                       campaign_id,
                                                                       customer_id,
                                                                       decline_reason,
                                                                       time_stamp,
                                                                       time_stamp::date,
                                                                       acquisition_date,
                                                                       step,
                                                                       first_affiliate,
                                                                       ancestor_id
                                         FROM temp_cycle_full
                                         WHERE existing IS FALSE);

                                """)
                if is_auto_update:
                    cur.execute(f"""
                                UPDATE augmented_data.order_cycles
                                SET crm_id                   = a.crm_id,
                                    order_id                 = a.order_id,
                                    bc_raw                   = a.bc_raw,
                                    bc_inferred              = a.bc_inferred,
                                    bc_increment             = a.bc_increment,
                                    attempt_increment        = a.attempt_increment,
                                    decrement_attempt_count  = a.attempt_decrement,
                                    attempt_count            = a.attempt_count,
                                    retry_attempt_count      = a.retry_attempt_count,
                                    real_attempt_count       = a.real_attempt_count,
                                    real_retry_attempt_count = a.real_retry_attempt_count,
                                    last_child               = a.last_child,
                                    real_last_child          = a.real_last_child,
                                    parent_id                = a.parent_id,
                                    campaign_id              = a.campaign_id,
                                    customer_id              = a.customer_id,
                                    decline_reason           = a.decline_reason,
                                    time_stamp               = a.time_stamp,
                                    acquisition_date         = a.acquisition_date,
                                    step                     = a.step,
                                    first_affiliate          = a.first_affiliate,
                                    ancestor_id              = a.ancestor_id
                                FROM (SELECT crm_id,
                                             order_id,
                                             bc_raw,
                                             bc_inferred,
                                             bc_increment,
                                             attempt_increment,
                                             attempt_decrement,
                                             attempt_count,
                                             retry_attempt_count,
                                             real_attempt_count,
                                             real_retry_attempt_count,
                                             last_child,
                                             real_last_child,
                                             parent_id,
                                             campaign_id,
                                             customer_id,
                                             decline_reason,
                                             time_stamp,
                                             time_stamp::date AS month_date,
                                             acquisition_date,
                                             step,
                                             first_affiliate,
                                             ancestor_id
                                      FROM temp_cycle_full
                                      WHERE existing IS TRUE) AS a
                                WHERE order_cycles.crm_id = a.crm_id
                                  AND order_cycles.order_id = a.order_id
                                  AND order_cycles.month_date = a.month_date;
                                """)
                cur.close()
                conn.commit()
                conn.close()

            except Exception as e:
                print('oc exception', e)
                try:
                    cur.close()
                except:
                    pass
                try:
                    conn.rollback()
                except:
                    pass
                try:
                    conn.close()
                except:
                    pass

        threads = []

        def _join():
            nonlocal threads
            for t in threads:
                try:
                    t.join()
                    print('oc joined')
                except:
                    print('oc thread join exception')
            threads = []

        sdex = 0

        while sdex < len(customer_ids):
            if len(threads):
                sleep(t_del)
            threads.append(Thread(target=_run, args=(customer_ids[sdex:sdex + batch_size],)))
            threads[len(threads) - 1].start()
            sdex += batch_size
            if len(threads) >= max_threads:
                _join()
        _join()

    def refresh(self, is_auto_update, customer_ids=False, max_batch_size=50000, min_batch_size=100, max_threads=2):
        conn = self.engine.raw_connection()
        cur = conn.cursor()

        def _exec(*args):
            nonlocal conn, cur
            print(f'started oc exec at {dt.datetime.now()} on {self.crm_id} {len(customer_ids) if customer_ids else "ALL"} customer_ids')
            for qry in args:
                try:

                   # print(qry)
                    print('Started Executing Query')
                    cur.execute(qry)
                    print('Finished Executing Query')

                except Exception as e:
                    print('oc exception', e)
                    try:
                        cur.close()
                    except:
                        pass
                    try:
                        conn.rollback()
                    except:
                        pass
                    try:
                        conn.close()
                    except:
                        pass

                    return False, f'error: {str(e)}'
            print(f'ended oc exec at {dt.datetime.now()}')
            return True, ''

        if customer_ids:
            cur.execute(f"SET LOCAL work_mem = '{self.get_wm(customer_ids)}'")
            if not isinstance(customer_ids, list):
                customer_ids = [customer_ids]
            _exec(f"""
            CREATE TEMP TABLE customers_to_table on commit drop as (select unnest(ARRAY {customer_ids}::numeric[]) as customer_id)
            """)
            _exec(f"""ALTER TABLE customers_to_table ADD CONSTRAINT ctt_pk PRIMARY KEY (customer_id);""")
        else:
            cur.execute("SET LOCAL work_mem = '4GB'")

        suc, err = _exec(f"""
            CREATE TEMP TABLE temp_cycle_full
            (
            crm_id                   text,
            order_id                 numeric                 not null
                constraint temp_cycle_full_pk
                    primary key,
            bc_raw                   numeric,
            bc_inferred              numeric,
            bc_increment             integer,
            attempt_increment        integer,
            attempt_decrement        integer,
            attempt_count            integer,
            retry_attempt_count      integer,
            real_attempt_count       integer,
            real_retry_attempt_count integer,
            last_child               numeric,
            real_last_child          numeric,
            parent_id                numeric,
            campaign_id              numeric,
            customer_id              numeric,
            insert_time              timestamp default now() not null,
            decline_reason           text,
            time_stamp               timestamp,
            acquisition_date         timestamp,
            step                     numeric,
            first_affiliate          text,
            adv_portfolio            text,
            existing                 boolean,
            ancestor_id              numeric,
            source                   text,
            ignore_in_reporting      boolean
            )
            ON COMMIT DROP
            """,
               f"""
                    CREATE TEMP TABLE orders_offer ON COMMIT DROP AS (
                    SELECT DISTINCT ON ( a.order_id ) a.order_id                    AS "order_id",
                                                      a.customer_id,
                                                      a.time_stamp                  AS "time_stamp",
                                                      a.crm_id                      AS "crm_id",
                                                      a.affid                       AS "affiliate",
                                                      a.decline_reason              AS "decline_reason",
                                                      NULL::integer                 AS "step",
                                                      coalesce(campaign_a.offer_id, campaign_b.offer_id, campaign_c.offer_id,
                                                               campaign_d.offer_id, campaign_e.offer_id,
                                                               campaign_f.offer_id) AS "offer_id",
                                                      a.billing_cycle               AS "billing_cycle",
                                                      a.campaign_id,
                                                      a.main_product_id,
                                                      NULL::integer                 AS "step_1",
                                                      NULL::integer                 AS "step_2"
                    FROM crm_global.orders_{self.crm_id} AS "a"
                             {"INNER JOIN customers_to_table AS x ON x.customer_id = a.customer_id" if customer_ids else ""}
                             /*OFFER*/
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "campaign_a"
                                       ON campaign_a.crm_id = a.crm_id AND campaign_a.provider_campaign = a.campaign_id
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "campaign_b"
                                       ON campaign_b.crm_id = a.crm_id AND campaign_b.prepaid_campaign = a.campaign_id
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "campaign_c"
                                       ON campaign_c.crm_id = a.crm_id AND campaign_c.bin_block_campaign = a.campaign_id
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "campaign_d"
                                       ON campaign_d.crm_id = a.crm_id AND campaign_d.mb_campaign = a.campaign_id
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "campaign_e"
                                       ON campaign_e.crm_id = a.crm_id AND campaign_e.rebill_campaign = a.campaign_id
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "campaign_f"
                                       ON campaign_f.crm_id = a.crm_id AND campaign_f.saves_campaign = a.campaign_id
                    );
                """,
               f"""
                    CREATE TEMP TABLE orders_offer_step ON COMMIT DROP AS (
                    SELECT DISTINCT ON ( a.order_id ) a.order_id            AS "order_id",
                                                      a.customer_id,
                                                      a.time_stamp          AS "time_stamp",
                                                      a.crm_id              AS "crm_id",
                                                      a.affiliate           AS "affiliate",
                                                      a.decline_reason      AS "decline_reason",
                                                      coalesce(step_a.step, step_b.step, /*step_c.step, step_d.step,step_e.step,*/
                                                               step_f.step, /*step_g.step,*/ step_h.step /*,step_i.step,
                                                               step_k.step*/) AS "step",
                                                      a.offer_id            AS "offer_id",
                                                      a.billing_cycle       AS "billing_cycle",
                                                      a.campaign_id,
                                                      a.main_product_id
                    FROM orders_offer AS "a"
                        /*STEP*/
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_a"
                                       ON step_a.crm_id = a.crm_id AND step_a.offer_id = a.offer_id AND
                                          step_a.main_product_id::text = a.main_product_id
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_b"
                                       ON step_b.crm_id = a.crm_id AND step_b.offer_id = a.offer_id AND
                                          step_b.charge_product_id::text = a.main_product_id/*
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_c"
                                       ON step_c.crm_id = a.crm_id AND step_c.offer_id = a.offer_id AND
                                          step_c.expedited_shipping_product_id::text = a.main_product_id*//*
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_d"
                                       ON step_d.crm_id = a.crm_id AND step_d.offer_id = a.offer_id AND
                                          step_d.warranty_product_id::text = a.main_product_id*/
                             /*LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_e"
                                       ON step_e.crm_id = a.crm_id AND step_e.offer_id = a.offer_id AND
                                          step_e.charge_product_id::text = a.main_product_id*/
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_f"
                                       ON step_f.crm_id = a.crm_id AND step_f.offer_id = a.offer_id AND
                                          step_f.rebill_product_id::text = a.main_product_id
                             /*LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_g"
                                       ON step_g.crm_id = a.crm_id AND step_g.offer_id = a.offer_id AND
                                          step_g.rebill_product_id::text = a.main_product_id*/
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_h"
                                       ON step_h.crm_id = a.crm_id AND step_h.offer_id = a.offer_id AND
                                          step_h.trial_product_id::text = a.main_product_id
                             /*LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_i"
                                       ON step_i.crm_id = a.crm_id AND step_i.offer_id = a.offer_id AND
                                          step_i.initial_product_id::text = a.main_product_id*/
                             /*LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_k"
                                       ON step_k.crm_id = a.crm_id AND step_k.offer_id = a.offer_id AND
                                          step_k.trial_shipping_id::text = a.main_product_id*/
                    --end changed product id field
                    );
                    """,
               f"""
                    CREATE TEMP TABLE orders_array ON COMMIT DROP AS (
                    SELECT DISTINCT ON ( a.order_id ) a.order_id                               AS "order_id",
                                                      a.customer_id,
                                                      a.time_stamp                             AS "time_stamp",
                                                      a.crm_id                                 AS "crm_id",
                                                      a.affiliate                              AS "affiliate",
                                                      a.decline_reason                         AS "decline_reason",
                                                      a.step                                   AS "step",
                                                      a.offer_id                               AS "offer_id",
                                                      a.billing_cycle                          AS "billing_cycle",
                                                      a.campaign_id,
                                                      a.main_product_id,
                                                      coalesce(e.decrement_attempt_count, '0') AS "decrement_attempt_count",
                                                      is_rebill AS "next_cycle"
                    FROM orders_offer_step AS "a"
                             LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "b"
                                       ON b.crm_id = a.crm_id AND b.offer_id = a.offer_id AND b.step = a.step
                             LEFT JOIN augmented_data.order_cycles AS e
                                       ON e.crm_id = a.crm_id AND e.order_id = a.order_id );
                    """,
               f"""
                    alter table orders_array
                    add constraint orders_array_pkey
                        primary key (order_id);
                    """,
               f"""
                    UPDATE orders_array
                    SET decrement_attempt_count = '1'
                    FROM (SELECT decline_reason FROM augmented_data.decline_reason_decrement) AS a
                    WHERE lower(orders_array.decline_reason) = lower(a.decline_reason)
                    AND orders_array.decline_reason IS NOT NULL
                    AND orders_array.decrement_attempt_count IS NOT NULL;
                    """,
               f"""
                    INSERT INTO temp_cycle_full (crm_id, order_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                                             attempt_count,
                                             retry_attempt_count, parent_id, campaign_id, customer_id, insert_time,
                                             decline_reason,
                                             time_stamp, acquisition_date, step, first_affiliate, adv_portfolio, existing,
                                             attempt_decrement) (
                    SELECT a.crm_id,
                           a.order_id,
                           CASE WHEN a.next_cycle IS TRUE THEN  a.billing_cycle::smallint ELSE '0'::smallint END AS "billing_cycle",
                           CASE WHEN a.customer_id = '0' THEN '0' ELSE e.b_c END::smallint,
                           NULL::smallint,
                           NULL::smallint,
                           NULL::smallint,
                           NULL::smallint,
                           NULL::bigint,
                           a.campaign_id,
                           a.customer_id,
                           a.time_stamp,
                           a.decline_reason,
                           a.time_stamp::timestamp with time zone,
                           e.acquisition_date,
                           e.step::smallint,
                           e.affiliate::text,
                           CASE WHEN e.offer_id IS NULL THEN 'undefined'::text ELSE e.offer_id::text END,
                           CASE WHEN b.order_id IS NULL THEN FALSE::boolean ELSE TRUE::boolean END,
                           a.decrement_attempt_count
                    FROM orders_array AS a
                             LEFT JOIN (SELECT max(order_id) AS order_id
                                        FROM augmented_data.order_cycles
                                        WHERE crm_id = '{self.crm_id}'
                                        GROUP BY order_id) AS b
                                       ON (b.order_id = a.order_id)
                             LEFT JOIN (SELECT a.customer_id,
                                               a.step,
                                               a.order_id,
                                               (sum(a.b_c)
                                                OVER ( PARTITION BY a.customer_id, a.offer_id, a.step ORDER BY a.time_stamp ASC)) AS b_c,
                                               e.time_stamp_to_acquisition_date                                                   AS acquisition_date,
                                               e.affiliate,
                                               a.offer_id
                                        FROM (SELECT a.customer_id,
                                                     a.step,
                                                     a.order_id,
                                                     a.incrementer,
                                                     a.offer_id,
                                                     a.campaign_id,
                                                     (lag(a.incrementer, '1'::smallint, '0'::smallint)
                                                      OVER ( PARTITION BY a.customer_id, a.offer_id, a.step ORDER BY a.time_stamp ASC)) AS b_c,
                                                     a.time_stamp
                                              FROM (SELECT a.customer_id,
                                                           a.step,
                                                           a.order_id,
                                                           b.decline_reason,
                                                           CASE
                                                               WHEN b.decline_reason IS NULL THEN '1'::smallint
                                                               ELSE '0'::smallint END AS incrementer,
                                                           a.offer_id,
                                                           a.time_stamp,
                                                           a.campaign_id
        
                                                    FROM orders_array AS a
                                                             LEFT JOIN (SELECT DISTINCT ON (order_id) order_id, decline_reason
                                                                        FROM orders_array) AS b
                                                                       ON (b.order_id = a.order_id)
                                                    ORDER BY a.customer_id, a.step, a.order_id) AS a) AS a
                                                 LEFT JOIN (SELECT a.customer_id,
                                                                   a.order_id,
                                                                   a.affiliate,
                                                                   a.time_stamp AS time_stamp_to_acquisition_date
                                                            FROM orders_array AS a
                                                                     INNER JOIN (SELECT DISTINCT ON ( orders.order_id, orders.customer_id ) orders.order_id,
                                                                                                                                            orders.customer_id
                                                                                 FROM orders_array AS orders
                                                                                          INNER JOIN (SELECT customer_id, min(order_id) AS "order_id"
                                                                                                      FROM orders_array
                                                                                                      WHERE decline_reason IS NULL
                                                                                                      GROUP BY customer_id)
                                                                                     AS "b"
                                                                                                     on b.customer_id = orders.customer_id and b.order_id = orders.order_id
                                                            ) AS b
                                                                                ON (b.order_id = a.order_id)) AS e
                                                           ON (e.customer_id = a.customer_id)) AS e
                                       ON (e.order_id = a.order_id)
                );
                    """,
               f"""
                    UPDATE temp_cycle_full
                    SET parent_id = a.parent_id
                    FROM (SELECT a.order_id, CASE WHEN a.bc_inferred = '0' THEN a.order_id ELSE b.order_id END AS parent_id
                      FROM (SELECT order_id, bc_inferred, customer_id, step, campaign_id, adv_portfolio FROM temp_cycle_full) AS a
                               LEFT JOIN (SELECT order_id,
                                                 customer_id,
                                                 step,
                                                 adv_portfolio,
                                                 campaign_id,
                                                 bc_inferred + '1' AS bc_inferred
                                          FROM temp_cycle_full
                                          WHERE decline_reason IS NULL) AS b
                                         ON (b.customer_id = a.customer_id AND b.step = a.step AND
                                             b.bc_inferred = a.bc_inferred AND b.adv_portfolio = a.adv_portfolio /*AND
                                                             b.campaign_id = a.campaign_id*/)
                     ) AS a
                    WHERE temp_cycle_full.order_id = a.order_id;
                    """,
               f"""
                    UPDATE temp_cycle_full
                    SET parent_id = a.parent_id
                    FROM (SELECT a.order_id, CASE WHEN a.bc_inferred = '0' THEN a.order_id ELSE b.order_id END AS parent_id
                      FROM (SELECT order_id, bc_inferred, customer_id, step, campaign_id, adv_portfolio FROM temp_cycle_full) AS a
                               LEFT JOIN (SELECT order_id,
                                                 customer_id,
                                                 step,
                                                 adv_portfolio,
                                                 campaign_id,
                                                 bc_inferred + '1' AS bc_inferred
                                          FROM temp_cycle_full
                                          WHERE decline_reason IS NULL) AS b
                                         ON (b.customer_id = a.customer_id AND b.step = a.step AND
                                             b.bc_inferred = a.bc_inferred AND b.adv_portfolio = a.adv_portfolio /*AND
                                                             b.campaign_id = a.campaign_id*/)
                     ) AS a
                    WHERE temp_cycle_full.order_id = a.order_id;
                    """,
               f"""
                    UPDATE temp_cycle_full
                    SET ancestor_id = a.ancestor
                    FROM (SELECT customer_id, step, adv_portfolio, min(order_id) AS ancestor
                      FROM temp_cycle_full
                      WHERE decline_reason IS NULL
                      GROUP BY customer_id, step, adv_portfolio) AS a
                    WHERE temp_cycle_full.customer_id = a.customer_id
                    AND temp_cycle_full.step = a.step
                    AND temp_cycle_full.adv_portfolio = a.adv_portfolio;
                    """,
               f"""
                    UPDATE temp_cycle_full
                    SET attempt_count      = a.attempt,
                    real_attempt_count = a.non_attempt
                    FROM (SELECT orders.order_id,
                             CASE
                                 WHEN orders.bc_inferred = '1' THEN
                                         (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2' -
                                         (sum(orders.attempt_decrement)
                                          OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                                 ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1' -
                                      (sum(orders.attempt_decrement)
                                       OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                                 END AS attempt,
                             CASE
                                 WHEN orders.bc_inferred = '1' THEN
                                         (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2'
                                 ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1'
                                 END AS non_attempt
                      FROM temp_cycle_full AS orders) AS a
                    WHERE temp_cycle_full.order_id = a.order_id;
                    """,
               f"""
                    UPDATE temp_cycle_full
                    SET attempt_count = '0'
                    WHERE attempt_count < '0';
                    """,
               f"""
                    UPDATE temp_cycle_full
                    SET real_last_child = a.last_child
                    FROM (SELECT parent_id, max(order_id) AS last_child FROM temp_cycle_full GROUP BY parent_id) AS a
                    WHERE a.parent_id = temp_cycle_full.order_id;
                    """,
               f"""
                    UPDATE temp_cycle_full
                    SET last_child = a.last_child
                    FROM (SELECT parent_id, max(order_id) AS last_child
                      FROM temp_cycle_full
                      WHERE attempt_decrement = '0'
                      GROUP BY parent_id) AS a
                    WHERE a.parent_id = temp_cycle_full.order_id;
                    """,
               f"""
                    UPDATE temp_cycle_full
                    SET retry_attempt_count = a.retry_attempt_count
                    FROM (SELECT orders.order_id,
                             a.attempt_count      AS retry_attempt_count,
                             a.real_attempt_count AS real_retry_attempt_count
        
                      from temp_cycle_full AS orders
                               LEFT JOIN (SELECT min(parent_id)                                      AS start_id,
                                                 bc_inferred,
                                                 adv_portfolio,
                                                 customer_id,
                                                 step,
                                                 count(attempt_count) - '1' - sum(attempt_decrement) AS attempt_count,
                                                 count(attempt_count) - '1'                          AS real_attempt_count
                                          FROM temp_cycle_full
                                          WHERE order_id <> parent_id
                                          GROUP BY adv_portfolio, customer_id, step, bc_inferred) AS a
                                         ON (a.customer_id = orders.customer_id AND a.adv_portfolio = orders.adv_portfolio AND
                                             a.start_id = orders.order_id)
                      WHERE a.start_id IS NOT NULL) AS a
                    WHERE temp_cycle_full.order_id = a.order_id;
                    """,
               f"""
                    INSERT INTO augmented_data.order_cycles (order_id, crm_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                                                         decrement_attempt_count, attempt_count, retry_attempt_count,
                                                         real_attempt_count,
                                                         real_retry_attempt_count, last_child, real_last_child, parent_id, campaign_id,
                                                         customer_id, decline_reason, time_stamp, month_date,
                                                         acquisition_date,
                                                         step,
                                                         first_affiliate, ancestor_id)
                    (SELECT DISTINCT ON (order_id) order_id,
                                                   crm_id,
                                                   bc_raw,
                                                   bc_inferred,
                                                   bc_increment,
                                                   attempt_increment,
                                                   attempt_decrement,
                                                   attempt_count,
                                                   retry_attempt_count,
                                                   real_attempt_count,
                                                   real_retry_attempt_count,
                                                   last_child,
                                                   real_last_child,
                                                   parent_id,
                                                   campaign_id,
                                                   customer_id,
                                                   decline_reason,
                                                   time_stamp,
                                                   time_stamp::date,
                                                   acquisition_date,
                                                   step,
                                                   first_affiliate,
                                                   ancestor_id
                     FROM temp_cycle_full
                     WHERE existing IS FALSE);
                    """,
               f"""
                    UPDATE augmented_data.order_cycles
                    SET crm_id                   = a.crm_id,
                    order_id                 = a.order_id,
                    bc_raw                   = a.bc_raw,
                    bc_inferred              = a.bc_inferred,
                    bc_increment             = a.bc_increment,
                    attempt_increment        = a.attempt_increment,
                    decrement_attempt_count  = a.attempt_decrement,
                    attempt_count            = a.attempt_count,
                    retry_attempt_count      = a.retry_attempt_count,
                    real_attempt_count       = a.real_attempt_count,
                    real_retry_attempt_count = a.real_retry_attempt_count,
                    last_child               = a.last_child,
                    real_last_child          = a.real_last_child,
                    parent_id                = a.parent_id,
                    campaign_id              = a.campaign_id,
                    customer_id              = a.customer_id,
                    decline_reason           = a.decline_reason,
                    time_stamp               = a.time_stamp,
                    acquisition_date         = a.acquisition_date,
                    step                     = a.step,
                    first_affiliate          = a.first_affiliate,
                    ancestor_id              = a.ancestor_id
                    FROM (SELECT crm_id,
                             order_id,
                             bc_raw,
                             bc_inferred,
                             bc_increment,
                             attempt_increment,
                             attempt_decrement,
                             attempt_count,
                             retry_attempt_count,
                             real_attempt_count,
                             real_retry_attempt_count,
                             last_child,
                             real_last_child,
                             parent_id,
                             campaign_id,
                             customer_id,
                             decline_reason,
                             time_stamp,
                             time_stamp::date as month_date,
                             acquisition_date,
                             step,
                             first_affiliate,
                             ancestor_id
                      FROM temp_cycle_full
                      WHERE existing IS TRUE) AS a
                    WHERE order_cycles.crm_id = a.crm_id
                    AND order_cycles.order_id = a.order_id
                    AND order_cycles.month_date = a.month_date;
                    """)
        if suc:
            conn.commit()
            cur.close()
            conn.close()
        return suc, err

    def kk_refresh_x(self, customer_ids=False, max_batch_size=50000, min_batch_size=100, max_threads=4, mydb=False):
        print('Doing Order Cycles')
        conn = self.engine.raw_connection()
        cur = conn.cursor()

        try:
            cur.execute("""SET LOCAL WORK_MEM = '4GB';""")
            # THIS IS WHERE THE CUSTOMERS TO TABLE THING IS CREATED TO JOIN OFF IRRELEVANT CUSTOMERS TO THE UPDATE
            if customer_ids:
                cur.execute(
                    f"""CREATE TEMP TABLE customers_to_table on commit drop as (select unnest(ARRAY{customer_ids}::numeric[]) as customer_id);""")

            cur.execute(f"""CREATE TEMP TABLE temp_cycle_full
            (
                crm_id                   text,
                order_id                 numeric                 not null
                    constraint temp_cycle_full_pk
                        primary key,
                bc_raw                   numeric,
                bc_inferred              numeric,
                bc_increment             integer,
                attempt_increment        integer,
                attempt_decrement        integer,
                attempt_count            integer,
                retry_attempt_count      integer,
                real_attempt_count       integer,
                real_retry_attempt_count integer,
                last_child               numeric,
                real_last_child          numeric,
                parent_id                numeric,
                campaign_id              numeric,
                customer_id              numeric,
                insert_time              timestamp default now() not null,
                decline_reason           text,
                time_stamp               timestamp,
                acquisition_date         timestamp,
                step                     numeric,
                first_affiliate          text,
                adv_portfolio            text,
                existing                 boolean,
                ancestor_id              numeric,
                source                   text,
                ignore_in_reporting      boolean
            )
                ON COMMIT DROP;""")

            cur.execute(f"""CREATE TEMP TABLE orders_array ON COMMIT DROP AS (
                SELECT DISTINCT ON ( a.transaction_id ) a.transaction_id                             AS "order_id",
                                                        a.customer_id,
                                                        a.date_created                               AS "time_stamp",

                                                        '{self.crm_id}'                                   AS "crm_id",
                                                        a.source_value1                              AS "affiliate",
                                                        CASE
                                                            WHEN a.response_type = 'SUCCESS' AND a.order_type = 'NEW_SALE' THEN NULL::text
                                                            ELSE a.response_text END                 AS "decline_reason",
                                                        coalesce(step_1.step, step_1_1.step)         AS "step",
                                                        coalesce(step_1.offer_id, step_1_1.offer_id) AS "offer_id",
                                                        a.billing_cycle_number                       AS "billing_cycle",
                                                        b.campaign_id,
                                                        c.product_id,
                                                        d.campaign_product_id,
                                                        step_1.step                                  AS "step_1",
                                                        step_1_1.step                                AS "step_2",
                                                        coalesce(e.decrement_attempt_count, '0')     AS "decrement_attempt_count"
                FROM {self.crm_id}.transactions AS "a"
                         {'INNER JOIN customers_to_table AS x ON x.customer_id = a.customer_id' if customer_ids else ''}
                         INNER JOIN {self.crm_id}.orders AS "b" ON b.order_id = a.order_id
                         INNER JOIN {self.crm_id}.transaction_items AS "c" ON c.transaction_id = a.transaction_id
                          INNER JOIN ((SELECT DISTINCT ON ( a.campaign_product_id ) a.campaign_product_id, campaign_id, product_id
                          FROM {self.crm_id}.products AS "a"
                                   LEFT JOIN (SELECT campaign_product_id
                                              FROM {self.crm_id}.products
                                              GROUP BY campaign_product_id
                                              HAVING count(1) > '1') AS "b"
                                             ON b.campaign_product_id = a.campaign_product_id
                                   LEFT JOIN (SELECT DISTINCT main_product_id
                                              FROM ui_{self._account_id}_offers.offer_globals) AS "c"
                                             ON c.main_product_id = a.product_id AND b.campaign_product_id IS NOT NULL
                          WHERE b.campaign_product_id IS NULL
                             OR (b.campaign_product_id IS NOT NULL AND c.main_product_id IS NOT NULL))
                         UNION ALL
                         (SELECT DISTINCT ON ( a.campaign_product_id ) a.campaign_product_id,
                                                                       a.campaign_id,
                                                                       a.product_id
                          FROM {self.crm_id}.products AS "a"
                                   LEFT JOIN (SELECT DISTINCT ON ( a.campaign_product_id ) a.campaign_product_id,
                                                                                           campaign_id,
                                                                                           product_id
                                              FROM {self.crm_id}.products AS "a"
                                                       LEFT JOIN (SELECT campaign_product_id
                                                                  FROM {self.crm_id}.products
                                                                  GROUP BY campaign_product_id
                                                                  HAVING count(1) > '1') AS "b"
                                                                 ON b.campaign_product_id = a.campaign_product_id
                                                       LEFT JOIN (SELECT DISTINCT main_product_id
                                                                  FROM ui_{self._account_id}_offers.offer_globals) AS "c"
                                                                 ON c.main_product_id = a.product_id AND b.campaign_product_id IS NOT NULL
                                              WHERE b.campaign_product_id IS NULL
                                                 OR (b.campaign_product_id IS NOT NULL AND c.main_product_id IS NOT NULL)) AS "b"
                                             On b.campaign_product_id = a.campaign_product_id
                          WHERE b.campaign_product_id IS NULL)) AS "d"
                        ON d.campaign_product_id = c.product_id
                         LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_1"
                                   ON step_1.crm_id = '{self.crm_id}' AND step_1.main_product_id = d.product_id
                         LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_1_1"
                                   ON step_1_1.crm_id = '{self.crm_id}' AND step_1_1.main_product_id = d.product_id
                         LEFT JOIN augmented_data.order_cycles AS e
                                   ON e.crm_id = '{self.crm_id}' AND e.order_id = a.transaction_id
                WHERE a.txn_type = 'SALE'
                  AND a.card_type <> 'TESTCARD');""")

            cur.execute("""alter table orders_array
                add constraint orders_array_pkey
                    primary key (order_id);""")

            cur.execute("""UPDATE orders_array
                SET decrement_attempt_count = '1'
                FROM (SELECT decline_reason FROM augmented_data.decline_reason_decrement) AS a
                WHERE lower(orders_array.decline_reason) = lower(a.decline_reason)
                  AND orders_array.decline_reason IS NOT NULL
                  AND orders_array.decrement_attempt_count = '0';""")

            cur.execute(f"""INSERT INTO temp_cycle_full (crm_id, order_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                                         attempt_count,
                                         retry_attempt_count, parent_id, campaign_id, customer_id, insert_time,
                                         decline_reason,
                                         time_stamp, acquisition_date, step, first_affiliate, adv_portfolio, existing,
                                         attempt_decrement) (
                SELECT a.crm_id,
                       a.order_id,
                       a.billing_cycle::smallint,
                       CASE WHEN a.customer_id = '0' THEN '0' ELSE e.b_c END::smallint,
                       NULL::smallint,
                       NULL::smallint,
                       NULL::smallint,
                       NULL::smallint,
                       NULL::bigint,
                       a.campaign_id,
                       a.customer_id,
                       a.time_stamp,
                       a.decline_reason,
                       a.time_stamp::timestamp with time zone,
                       e.acquisition_date,
                       e.step::smallint,
                       e.affiliate::text,
                       CASE WHEN e.offer_id IS NULL THEN 'undefined'::text ELSE e.offer_id::text END,
                       CASE WHEN b.order_id IS NULL THEN FALSE::boolean ELSE TRUE::boolean END,
                       a.decrement_attempt_count
                FROM orders_array AS a
                         LEFT JOIN (SELECT max(order_id) AS order_id
                                    FROM augmented_data.order_cycles
                                    WHERE crm_id = '{self.crm_id}'
                                    GROUP BY order_id) AS b
                                   ON (b.order_id = a.order_id)
                         LEFT JOIN (SELECT a.customer_id,
                                           a.step,
                                           a.order_id,
                                           (sum(a.b_c)
                                            OVER ( PARTITION BY a.customer_id, a.offer_id, a.step ORDER BY a.time_stamp ASC)) AS b_c,
                                           e.time_stamp_to_acquisition_date                                                   AS acquisition_date,
                                           e.affiliate,
                                           a.offer_id
                                    FROM (SELECT a.customer_id,
                                                 a.step,
                                                 a.order_id,
                                                 a.incrementer,
                                                 a.offer_id,
                                                 a.campaign_id,
                                                 (lag(a.incrementer, '1'::smallint, '0'::smallint)
                                                  OVER ( PARTITION BY a.customer_id, a.offer_id, a.step ORDER BY a.time_stamp ASC)) AS b_c,
                                                 a.time_stamp
                                          FROM (SELECT a.customer_id,
                                                       a.step,
                                                       a.order_id,
                                                       b.decline_reason,
                                                       CASE
                                                           WHEN b.decline_reason IS NULL THEN '1'::smallint
                                                           ELSE '0'::smallint END AS incrementer,
                                                       a.offer_id,
                                                       a.time_stamp,
                                                       a.campaign_id

                                                FROM orders_array AS a
                                                         LEFT JOIN (SELECT DISTINCT ON (order_id) order_id, decline_reason
                                                                    FROM orders_array) AS b
                                                                   ON (b.order_id = a.order_id)
                                                ORDER BY a.customer_id, a.step, a.order_id) AS a) AS a
                                             LEFT JOIN (SELECT a.customer_id,
                                                               a.order_id,
                                                               a.affiliate,
                                                               a.time_stamp AS time_stamp_to_acquisition_date
                                                        FROM orders_array AS a
                                                                 INNER JOIN (SELECT DISTINCT ON ( orders.order_id, orders.customer_id ) orders.order_id,
                                                                                                                                        orders.customer_id
                                                                             FROM orders_array AS orders
                                                                                      INNER JOIN (SELECT customer_id, min(order_id) AS "order_id"
                                                                                                  FROM orders_array
                                                                                                  WHERE decline_reason IS NULL
                                                                                                  GROUP BY customer_id)
                                                                                 AS "b"
                                                                                                 on b.customer_id = orders.customer_id and b.order_id = orders.order_id
                                                        ) AS b
                                                                            ON (b.order_id = a.order_id)) AS e
                                                       ON (e.customer_id = a.customer_id)) AS e
                                   ON (e.order_id = a.order_id)
            );""")

            cur.execute("""UPDATE temp_cycle_full
            SET parent_id = a.parent_id
            FROM (SELECT a.order_id, CASE WHEN a.bc_inferred = '0' THEN a.order_id ELSE b.order_id END AS parent_id
                  FROM (SELECT order_id, bc_inferred, customer_id, step, campaign_id, adv_portfolio FROM temp_cycle_full) AS a
                           LEFT JOIN (SELECT order_id,
                                             customer_id,
                                             step,
                                             adv_portfolio,
                                             campaign_id,
                                             bc_inferred + '1' AS bc_inferred
                                      FROM temp_cycle_full
                                      WHERE decline_reason IS NULL) AS b
                                     ON (b.customer_id = a.customer_id AND b.step = a.step AND
                                         b.bc_inferred = a.bc_inferred AND b.adv_portfolio = a.adv_portfolio /*AND
                                                         b.campaign_id = a.campaign_id*/)
                 ) AS a
            WHERE temp_cycle_full.order_id = a.order_id;""")

            cur.execute("""UPDATE temp_cycle_full
            SET ancestor_id = a.ancestor
            FROM (SELECT customer_id, step, adv_portfolio, min(order_id) AS ancestor
                  FROM temp_cycle_full
                  WHERE decline_reason IS NULL
                  GROUP BY customer_id, step, adv_portfolio) AS a
            WHERE temp_cycle_full.customer_id = a.customer_id
              AND temp_cycle_full.step = a.step
              AND temp_cycle_full.adv_portfolio = a.adv_portfolio;""")

            cur.execute("""UPDATE temp_cycle_full
            SET attempt_count      = a.attempt,
                real_attempt_count = a.non_attempt
            FROM (SELECT orders.order_id,
                         CASE
                             WHEN orders.bc_inferred = '1' THEN
                                     (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2' -
                                     (sum(orders.attempt_decrement)
                                      OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                             ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1' -
                                  (sum(orders.attempt_decrement)
                                   OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                             END AS attempt,
                         CASE
                             WHEN orders.bc_inferred = '1' THEN
                                     (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2'
                             ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1'
                             END AS non_attempt
                  FROM temp_cycle_full AS orders) AS a
            WHERE temp_cycle_full.order_id = a.order_id;""")

            cur.execute("""UPDATE temp_cycle_full
            SET attempt_count = '0'
            WHERE attempt_count < '0';""")

            cur.execute("""UPDATE temp_cycle_full
            SET real_last_child = a.last_child
            FROM (SELECT parent_id, max(order_id) AS last_child FROM temp_cycle_full GROUP BY parent_id) AS a
            WHERE a.parent_id = temp_cycle_full.order_id;""")

            cur.execute("""UPDATE temp_cycle_full
            SET last_child = a.last_child
            FROM (SELECT parent_id, max(order_id) AS last_child
                  FROM temp_cycle_full
                  WHERE attempt_decrement = '0'
                  GROUP BY parent_id) AS a
            WHERE a.parent_id = temp_cycle_full.order_id;""")

            cur.execute("""UPDATE temp_cycle_full
            SET retry_attempt_count = a.retry_attempt_count
            FROM (SELECT orders.order_id,
                         a.attempt_count      AS retry_attempt_count,
                         a.real_attempt_count AS real_retry_attempt_count

                  from temp_cycle_full AS orders
                           LEFT JOIN (SELECT min(parent_id)                                      AS start_id,
                                             bc_inferred,
                                             adv_portfolio,
                                             customer_id,
                                             step,
                                             count(attempt_count) - '1' - sum(attempt_decrement) AS attempt_count,
                                             count(attempt_count) - '1'                          AS real_attempt_count
                                      FROM temp_cycle_full
                                      WHERE order_id <> parent_id
                                      GROUP BY adv_portfolio, customer_id, step, bc_inferred) AS a
                                     ON (a.customer_id = orders.customer_id AND a.adv_portfolio = orders.adv_portfolio AND
                                         a.start_id = orders.order_id)
                  WHERE a.start_id IS NOT NULL) AS a
            WHERE temp_cycle_full.order_id = a.order_id;""")

            # #cur.execute("""SELECT *
            # FROM temp_cycle_full WHERE bc_inferred > '0'
            # ORDER BY customer_id;""")

            # cur.execute("""SELECT a.order_id, a.bc_inferred, b.bc_inferred FROM temp_cycle_full AS "a" LEFT JOIN augmented_data.order_cycles_{self.crm_id} AS "b" ON b.crm_id = a.crm_id AND b.order_id = a.order_id WHERE b.bc_inferred <> a.bc_inferred  ;""")

            cur.execute("""INSERT INTO augmented_data.order_cycles (order_id, crm_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                                                     decrement_attempt_count, attempt_count, retry_attempt_count,
                                                     real_attempt_count,
                                                     real_retry_attempt_count, last_child, real_last_child, parent_id, campaign_id,
                                                     customer_id, decline_reason, time_stamp, month_date,
                                                     acquisition_date,
                                                     step,
                                                     first_affiliate, ancestor_id)
                (SELECT DISTINCT ON (order_id) order_id,
                                               crm_id,
                                               bc_raw,
                                               bc_inferred,
                                               bc_increment,
                                               attempt_increment,
                                               attempt_decrement,
                                               attempt_count,
                                               retry_attempt_count,
                                               real_attempt_count,
                                               real_retry_attempt_count,
                                               last_child,
                                               real_last_child,
                                               parent_id,
                                               campaign_id,
                                               customer_id,
                                               decline_reason,
                                               time_stamp,
                                               time_stamp::date,
                                               acquisition_date,
                                               step,
                                               first_affiliate,
                                               ancestor_id
                 FROM temp_cycle_full
                 WHERE existing IS FALSE);""")

            cur.execute("""UPDATE augmented_data.order_cycles
            SET crm_id                   = a.crm_id,
                order_id                 = a.order_id,
                bc_raw                   = a.bc_raw,
                bc_inferred              = a.bc_inferred,
                bc_increment             = a.bc_increment,
                attempt_increment        = a.attempt_increment,
                decrement_attempt_count  = a.attempt_decrement,
                attempt_count            = a.attempt_count,
                retry_attempt_count      = a.retry_attempt_count,
                real_attempt_count       = a.real_attempt_count,
                real_retry_attempt_count = a.real_retry_attempt_count,
                last_child               = a.last_child,
                real_last_child          = a.real_last_child,
                parent_id                = a.parent_id,
                campaign_id              = a.campaign_id,
                customer_id              = a.customer_id,
                decline_reason           = a.decline_reason,
                time_stamp               = a.time_stamp,
                acquisition_date         = a.acquisition_date,
                step                     = a.step,
                first_affiliate          = a.first_affiliate,
                ancestor_id              = a.ancestor_id
            FROM (SELECT crm_id,
                         order_id,
                         bc_raw,
                         bc_inferred,
                         bc_increment,
                         attempt_increment,
                         attempt_decrement,
                         attempt_count,
                         retry_attempt_count,
                         real_attempt_count,
                         real_retry_attempt_count,
                         last_child,
                         real_last_child,
                         parent_id,
                         campaign_id,
                         customer_id,
                         decline_reason,
                         time_stamp,
                         time_stamp::date as month_date,
                         acquisition_date,
                         step,
                         first_affiliate,
                         ancestor_id
                  FROM temp_cycle_full
                  WHERE existing IS TRUE) AS a
            WHERE order_cycles.crm_id = a.crm_id
              AND order_cycles.order_id = a.order_id
              AND order_cycles.month_date = a.month_date;""")

            conn.commit()
        except Exception as e:
            conn.rollback()
            cur.close()
            conn.close()
            raise e
        cur.close()
        conn.close()

        print('oc _done ')

    @staticmethod
    def get_wm(ids, multiplier=0.1):
        wm = len(ids) * multiplier
        if wm < 4:
            wm = 4
        elif wm > 10000:
            wm = 10000
        return f"{str(int(wm))}MB"

    def kk_refresh(self, customer_ids=False, max_batch_size=50000, min_batch_size=100, max_threads=4, mydb=False):
        print('Doing Order Cycles')
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        print('OC conn made')
        wm = '35GB'
        if customer_ids:
            wm = self.get_wm(customer_ids, 0.5)
        try:
            cur.execute(f"""SET LOCAL WORK_MEM = '{wm}';""")
            # THIS IS WHERE THE CUSTOMERS TO TABLE THING IS CREATED TO JOIN OFF IRRELEVANT CUSTOMERS TO THE UPDATE
            if customer_ids:
                cur.execute(
                    f"""CREATE TEMP TABLE customers_to_table on commit drop as (select unnest(ARRAY{customer_ids}::numeric[]) as customer_id);""")
                cur.execute(
                    f"""ALTER TABLE customers_to_table ADD CONSTRAINT ctt_pk PRIMARY KEY (customer_id);""")
            cur.execute(f"""CREATE TEMP TABLE temp_cycle_full
               (
                   crm_id                   text,
                   order_id                 numeric                 not null
                       constraint temp_cycle_full_pk
                           primary key,
                   bc_raw                   numeric,
                   bc_inferred              numeric,
                   bc_increment             integer,
                   attempt_increment        integer,
                   attempt_decrement        integer,
                   attempt_count            integer,
                   retry_attempt_count      integer,
                   real_attempt_count       integer,
                   real_retry_attempt_count integer,
                   last_child               numeric,
                   real_last_child          numeric,
                   parent_id                numeric,
                   campaign_id              numeric,
                   customer_id              numeric,
                   insert_time              timestamp default now() not null,
                   decline_reason           text,
                   time_stamp               timestamp,
                   acquisition_date         timestamp,
                   step                     numeric,
                   first_affiliate          text,
                   adv_portfolio            text,
                   existing                 boolean,
                   ancestor_id              numeric,
                   source                   text,
                   ignore_in_reporting      boolean
               )
                   ON COMMIT DROP;""")

            cur.execute(f"""CREATE TEMP TABLE orders_array ON COMMIT DROP AS (
                            SELECT DISTINCT ON ( a.order_id ) a.order_id                             AS "order_id",
                                                                    a.customer_id,
                                                                    f.time_stamp                               AS "time_stamp",
                        
                                                                    a.crm_id                                   AS "crm_id",
                                                                    a.affiliate                              AS "affiliate",
                                                                    a.decline_reason                 AS "decline_reason",
                                                                    coalesce(step_1.step, step_1_1.step)         AS "step",
                                                                    coalesce(step_1.offer_id, step_1_1.offer_id) AS "offer_id",
                                                                    a.billing_cycle                       AS "billing_cycle",
                                                                    a.campaign_id,
                                                                    a.main_product_id,
                                                                    step_1.step                                  AS "step_1",
                                                                    step_1_1.step                                AS "step_2",
                                                                    coalesce(e.decrement_attempt_count, '0')     AS "decrement_attempt_count"
                            FROM crm_global.orders_{self.crm_id} AS "a"
                                    {'INNER JOIN customers_to_table AS x ON x.customer_id = a.customer_id' if customer_ids else ''}
                                     LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_1"
                                               ON step_1.crm_id = a.crm_id AND step_1.main_product_id::text = a.main_product_id 
                                               AND a.campaign_id = ANY(ARRAY[step_1.prepaid_campaign,
                                                                            step_1.bin_block_campaign,
                                                                            step_1.saves_campaign,
                                                                            step_1.rebill_campaign,
                                                                            step_1.mb_campaign,
                                                                            step_1.provider_campaign
                                                                        ])
                        
                                     LEFT JOIN ui_{self._account_id}_offers.offer_globals AS "step_1_1"
                                               ON step_1_1.crm_id = a.crm_id AND step_1_1.main_product_id::text = a.main_product_id
                                               AND a.campaign_id = ANY(ARRAY[step_1_1.prepaid_campaign,
                                                                            step_1_1.bin_block_campaign,
                                                                            step_1_1.saves_campaign,
                                                                            step_1_1.rebill_campaign,
                                                                            step_1_1.mb_campaign,
                                                                            step_1_1.provider_campaign
                                                                        ])
                                --end changed product id field
                                     LEFT JOIN augmented_data.order_cycles_{self.crm_id} AS e
                                               ON e.crm_id = a.crm_id AND e.order_id = a.order_id
                                    LEFT JOIN ( SELECT  transaction_id, min( date_created ) AS "time_stamp" FROM {self.crm_id}.transactions GROUP BY transaction_id) AS "f" ON f.transaction_id = a.order_id
                            WHERE a.cc_type <> 'TESTCARD'
                        );""")

            cur.execute("""UPDATE orders_array
                   SET decrement_attempt_count = '1'
                   FROM (SELECT decline_reason FROM augmented_data.decline_reason_decrement) AS a
                   WHERE lower(orders_array.decline_reason) = lower(a.decline_reason)
                     AND orders_array.decline_reason IS NOT NULL
                     AND orders_array.decrement_attempt_count = '0';""")

            cur.execute(f"""INSERT INTO temp_cycle_full (crm_id, order_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                                            attempt_count,
                                            retry_attempt_count, parent_id, campaign_id, customer_id, insert_time,
                                            decline_reason,
                                            time_stamp, acquisition_date, step, first_affiliate, adv_portfolio, existing,
                                            attempt_decrement) (
                   SELECT a.crm_id,
                          a.order_id,
                          a.billing_cycle::smallint,
                          CASE WHEN a.customer_id = '0' THEN '0' ELSE e.b_c END::smallint,
                          NULL::smallint,
                          NULL::smallint,
                          NULL::smallint,
                          NULL::smallint,
                          NULL::bigint,
                          a.campaign_id,
                          a.customer_id,
                          a.time_stamp,
                          a.decline_reason,
                          a.time_stamp::timestamp with time zone,
                          e.acquisition_date,
                          e.step::smallint,
                          e.affiliate::text,
                          CASE WHEN e.offer_id IS NULL THEN 'undefined'::text ELSE e.offer_id::text END,
                          CASE WHEN b.order_id IS NULL THEN FALSE::boolean ELSE TRUE::boolean END,
                          a.decrement_attempt_count
                   FROM orders_array AS a
                            LEFT JOIN (SELECT max(order_id) AS order_id
                                       FROM augmented_data.order_cycles
                                       WHERE crm_id = '{self.crm_id}'
                                       GROUP BY order_id) AS b
                                      ON (b.order_id = a.order_id)
                            LEFT JOIN (SELECT a.customer_id,
                                              a.step,
                                              a.order_id,
                                              (sum(a.b_c)
                                               OVER ( PARTITION BY a.customer_id, a.offer_id, a.step ORDER BY a.time_stamp ASC)) AS b_c,
                                              e.time_stamp_to_acquisition_date                                                   AS acquisition_date,
                                              e.affiliate,
                                              a.offer_id
                                       FROM (SELECT a.customer_id,
                                                    a.step,
                                                    a.order_id,
                                                    a.incrementer,
                                                    a.offer_id,
                                                    a.campaign_id,
                                                    (lag(a.incrementer, '1'::smallint, '0'::smallint)
                                                     OVER ( PARTITION BY a.customer_id, a.offer_id, a.step ORDER BY a.time_stamp ASC)) AS b_c,
                                                    a.time_stamp
                                             FROM (SELECT a.customer_id,
                                                          a.step,
                                                          a.order_id,
                                                          b.decline_reason,
                                                          CASE
                                                              WHEN b.decline_reason IS NULL THEN '1'::smallint
                                                              ELSE '0'::smallint END AS incrementer,
                                                          a.offer_id,
                                                          a.time_stamp,
                                                          a.campaign_id

                                                   FROM orders_array AS a
                                                            LEFT JOIN (SELECT DISTINCT ON (order_id) order_id, decline_reason
                                                                       FROM orders_array) AS b
                                                                      ON (b.order_id = a.order_id)
                                                   ORDER BY a.customer_id, a.step, a.order_id) AS a) AS a
                                                LEFT JOIN (SELECT a.customer_id,
                                                                  a.order_id,
                                                                  a.affiliate,
                                                                  a.time_stamp AS time_stamp_to_acquisition_date
                                                           FROM orders_array AS a
                                                                    INNER JOIN (SELECT DISTINCT ON ( orders.order_id, orders.customer_id ) orders.order_id,
                                                                                                                                           orders.customer_id
                                                                                FROM orders_array AS orders
                                                                                         INNER JOIN (SELECT customer_id, min(order_id) AS "order_id"
                                                                                                     FROM orders_array
                                                                                                     WHERE decline_reason IS NULL
                                                                                                     GROUP BY customer_id)
                                                                                    AS "b"
                                                                                                    on b.customer_id = orders.customer_id and b.order_id = orders.order_id
                                                           ) AS b
                                                                               ON (b.order_id = a.order_id)) AS e
                                                          ON (e.customer_id = a.customer_id)) AS e
                                      ON (e.order_id = a.order_id)
               );""")

            cur.execute("""UPDATE temp_cycle_full
               SET parent_id = a.parent_id
               FROM (SELECT a.order_id, CASE WHEN a.bc_inferred = '0' THEN a.order_id ELSE b.order_id END AS parent_id
                     FROM (SELECT order_id, bc_inferred, customer_id, step, campaign_id, adv_portfolio FROM temp_cycle_full) AS a
                              LEFT JOIN (SELECT order_id,
                                                customer_id,
                                                step,
                                                adv_portfolio,
                                                campaign_id,
                                                bc_inferred + '1' AS bc_inferred
                                         FROM temp_cycle_full
                                         WHERE decline_reason IS NULL) AS b
                                        ON (b.customer_id = a.customer_id AND b.step = a.step AND
                                            b.bc_inferred = a.bc_inferred AND b.adv_portfolio = a.adv_portfolio /*AND
                                                            b.campaign_id = a.campaign_id*/)
                    ) AS a
               WHERE temp_cycle_full.order_id = a.order_id;""")

            cur.execute("""UPDATE temp_cycle_full
               SET ancestor_id = a.ancestor
               FROM (SELECT customer_id, step, adv_portfolio, min(order_id) AS ancestor
                     FROM temp_cycle_full
                     WHERE decline_reason IS NULL
                     GROUP BY customer_id, step, adv_portfolio) AS a
               WHERE temp_cycle_full.customer_id = a.customer_id
                 AND temp_cycle_full.step = a.step
                 AND temp_cycle_full.adv_portfolio = a.adv_portfolio;""")

            cur.execute("""UPDATE temp_cycle_full
               SET attempt_count      = a.attempt,
                   real_attempt_count = a.non_attempt
               FROM (SELECT orders.order_id,
                            CASE
                                WHEN orders.bc_inferred = '1' THEN
                                        (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2' -
                                        (sum(orders.attempt_decrement)
                                         OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                                ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1' -
                                     (sum(orders.attempt_decrement)
                                      OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                                END AS attempt,
                            CASE
                                WHEN orders.bc_inferred = '1' THEN
                                        (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2'
                                ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1'
                                END AS non_attempt
                     FROM temp_cycle_full AS orders) AS a
               WHERE temp_cycle_full.order_id = a.order_id;""")

            cur.execute("""UPDATE temp_cycle_full
               SET attempt_count = '0'
               WHERE attempt_count < '0';""")

            cur.execute("""UPDATE temp_cycle_full
               SET real_last_child = a.last_child
               FROM (SELECT parent_id, max(order_id) AS last_child FROM temp_cycle_full GROUP BY parent_id) AS a
               WHERE a.parent_id = temp_cycle_full.order_id;""")

            cur.execute("""UPDATE temp_cycle_full
               SET last_child = a.last_child
               FROM (SELECT parent_id, max(order_id) AS last_child
                     FROM temp_cycle_full
                     WHERE attempt_decrement = '0'
                     GROUP BY parent_id) AS a
               WHERE a.parent_id = temp_cycle_full.order_id;""")

            cur.execute("""UPDATE temp_cycle_full
               SET retry_attempt_count = a.retry_attempt_count
               FROM (SELECT orders.order_id,
                            a.attempt_count      AS retry_attempt_count,
                            a.real_attempt_count AS real_retry_attempt_count

                     from temp_cycle_full AS orders
                              LEFT JOIN (SELECT min(parent_id)                                      AS start_id,
                                                bc_inferred,
                                                adv_portfolio,
                                                customer_id,
                                                step,
                                                count(attempt_count) - '1' - sum(attempt_decrement) AS attempt_count,
                                                count(attempt_count) - '1'                          AS real_attempt_count
                                         FROM temp_cycle_full
                                         WHERE order_id <> parent_id
                                         GROUP BY adv_portfolio, customer_id, step, bc_inferred) AS a
                                        ON (a.customer_id = orders.customer_id AND a.adv_portfolio = orders.adv_portfolio AND
                                            a.start_id = orders.order_id)
                     WHERE a.start_id IS NOT NULL) AS a
               WHERE temp_cycle_full.order_id = a.order_id;""")

            # #cur.execute("""SELECT *
            # FROM temp_cycle_full WHERE bc_inferred > '0'
            # ORDER BY customer_id;""")

            # cur.execute("""SELECT a.order_id, a.bc_inferred, b.bc_inferred FROM temp_cycle_full AS "a" LEFT JOIN augmented_data.order_cycles_{self.crm_id} AS "b" ON b.crm_id = a.crm_id AND b.order_id = a.order_id WHERE b.bc_inferred <> a.bc_inferred  ;""")

            cur.execute("""INSERT INTO augmented_data.order_cycles (order_id, crm_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                                                        decrement_attempt_count, attempt_count, retry_attempt_count,
                                                        real_attempt_count,
                                                        real_retry_attempt_count, last_child, real_last_child, parent_id, campaign_id,
                                                        customer_id, decline_reason, time_stamp, month_date,
                                                        acquisition_date,
                                                        step,
                                                        first_affiliate, ancestor_id)
                   (SELECT DISTINCT ON (order_id) order_id,
                                                  crm_id,
                                                  bc_raw,
                                                  bc_inferred,
                                                  bc_increment,
                                                  attempt_increment,
                                                  attempt_decrement,
                                                  attempt_count,
                                                  retry_attempt_count,
                                                  real_attempt_count,
                                                  real_retry_attempt_count,
                                                  last_child,
                                                  real_last_child,
                                                  parent_id,
                                                  campaign_id,
                                                  customer_id,
                                                  decline_reason,
                                                  time_stamp,
                                                  time_stamp::date,
                                                  acquisition_date,
                                                  step,
                                                  first_affiliate,
                                                  ancestor_id
                    FROM temp_cycle_full
                    WHERE existing IS FALSE);""")

            cur.execute("""UPDATE augmented_data.order_cycles
               SET crm_id                   = a.crm_id,
                   order_id                 = a.order_id,
                   bc_raw                   = a.bc_raw,
                   bc_inferred              = a.bc_inferred,
                   bc_increment             = a.bc_increment,
                   attempt_increment        = a.attempt_increment,
                   decrement_attempt_count  = a.attempt_decrement,
                   attempt_count            = a.attempt_count,
                   retry_attempt_count      = a.retry_attempt_count,
                   real_attempt_count       = a.real_attempt_count,
                   real_retry_attempt_count = a.real_retry_attempt_count,
                   last_child               = a.last_child,
                   real_last_child          = a.real_last_child,
                   parent_id                = a.parent_id,
                   campaign_id              = a.campaign_id,
                   customer_id              = a.customer_id,
                   decline_reason           = a.decline_reason,
                   time_stamp               = a.time_stamp,
                   acquisition_date         = a.acquisition_date,
                   step                     = a.step,
                   first_affiliate          = a.first_affiliate,
                   ancestor_id              = a.ancestor_id
               FROM (SELECT crm_id,
                            order_id,
                            bc_raw,
                            bc_inferred,
                            bc_increment,
                            attempt_increment,
                            attempt_decrement,
                            attempt_count,
                            retry_attempt_count,
                            real_attempt_count,
                            real_retry_attempt_count,
                            last_child,
                            real_last_child,
                            parent_id,
                            campaign_id,
                            customer_id,
                            decline_reason,
                            time_stamp,
                            time_stamp::date as month_date,
                            acquisition_date,
                            step,
                            first_affiliate,
                            ancestor_id
                     FROM temp_cycle_full
                     WHERE existing IS TRUE) AS a
               WHERE order_cycles.crm_id = a.crm_id
                 AND order_cycles.order_id = a.order_id
                 AND order_cycles.month_date = a.month_date;""")

            conn.commit()
        except Exception as e:
            conn.rollback()
            cur.close()
            conn.close()
            return False, f"oc update error {self.crm_id}: {str(e)}"
        cur.close()
        conn.close()

        print('oc _done ')
        return True, ""

    def kk_update_recurring(self, my_df, update=True, check=True):
        df = None
        conn = self.engine.raw_connection()
        cur = conn.cursor()
        cur.execute("Set local work_mem = '4GB'")
        # cur.execute("DROP TABLE IF EXISTS tmp_rec_update")
        min_dt = my_df.order_dt.min()

        def update_recurring_true(cur=False, conn=False):
            if cur:
                print(dt.datetime.now())
                cur.execute(f"""update crm_global.orders
                        set is_recurring = dump.is_recurring,
                            on_hold = dump.on_hold,
                            --is_paused = case when dump.is_recurring >0 then 0 end,
                            extended_date = dump.extended_date
                                from (  select b.order_id,b.crm_id, c.step, 
                                       case when a.due_dt is null then 0 else 1 end as is_recurring,
                                       case when a.due_dt is null then 1 else 0 end as on_hold,
                                       case when b.is_extended > 0 then a.due_dt else null end as extended_date    
                                       from 
                                       tmp_rec_update as a                                          
                                       right join 
                                       (select                                
                                        crm_id, order_id, native_order_id, is_extended, decline_reason, month_date from crm_global.orders
                                        where month_date >= '{min_dt}'::date
                                        and crm_id = '{self._crm_id}'
                                        and decline_reason is null

                                       ) as b 
                                       on a.crm_id = b.crm_id and a.order_id = b.native_order_id 
                                       inner join (select crm_id, order_id, step 
                                                    from augmented_data.order_cycles 
                                                    where crm_id = '{self._crm_id}'
                                                    and  month_date >= '{min_dt}'::date
                                                    and decline_reason is null
                                                    ) as c on b.order_id = c.order_id and b.crm_id = c.crm_id) as dump
                            where dump.crm_id = crm_global.orders.crm_id
                            and dump.order_id = crm_global.orders.order_id
                            and crm_global.orders.month_date >= '{min_dt}'::date
                    """)
            print(dt.datetime.now())

            if conn:
                df = pd.read_sql(f""" 
                                 select b.order_id,b.crm_id,b.native_order_id,c.step, b.is_extended, b.decline_reason, b.month_date,
                                    a.due_dt,
                                   case when a.due_dt is null then 0 else 1 end as is_recurring,
                                   case when a.due_dt is null then 1 else 0 end as on_hold,
                                   case when b.is_extended > 0 then a.due_dt else null end as extended_date    
                                   from 
                                   tmp_rec_update as a                                          
                                   right join 
                                   (select                                
                                    crm_id, order_id, native_order_id, is_extended, decline_reason, month_date from crm_global.orders
                                    where month_date >= '{min_dt}'::date
                                    and crm_id = '{self._crm_id}'
                                    and decline_reason is null

                                   ) as b 
                                   on a.crm_id = b.crm_id and a.order_id = b.native_order_id 
                                   inner join (select crm_id, order_id, step 
                                                from augmented_data.order_cycles 
                                                where crm_id = '{self._crm_id}'
                                                and  month_date >= '{min_dt}'::date
                                                and decline_reason is null
                                                )
                                   c on b.order_id = c.order_id and b.crm_id = c.crm_id 

                                   """, conn)

        def update_recurring_false(cur):
            cur.execute(
                f"""UPDATE crm_global.orders set is_recurring =0, on_hold=0 where decline_reason is not null and crm_id='{self.crm_id}'""")

        def check_orders(conn):
            df = pd.read_sql(f"""
                select a.order_id as f_ord,a.step as f_step, a.order_dt,
                b.crm_id,b.order_id,b.native_order_id,b.is_recurring,b.decline_reason,
                c.campaign_name,c.campaign_id, c.step from tmp_rec_update as a
                left join crm_global.orders b on b.crm_id = a.crm_id and b.native_order_id = a.order_id               
                left join ui_{self._account_id}_offers.campaigns c on b.campaign_id = c.campaign_id and b.crm_id = c.crm_id 

            """, conn)
            checker = df.loc[df.order_id.isna()]
            print(
                f' kk recurring update | {len(checker)} | missing recurring orders | min order {checker.order_dt.min()}')
            checker = df.loc[df.step.isna()]
            print(
                f' kk recurring update | {len(checker)} | missing recurring orders due to null steps | campaign_id | {checker.campaign_id.unique().tolist()}')

        my_df['crm_id'] = self._crm_id
        print('mydflen', len(my_df))
        print('1')
        cur.execute(f"""CREATE TEMP TABLE tmp_rec_update as  (select unnest(ARRAY{my_df.order_id.tolist()}::text[]) order_id, 
                             unnest(ARRAY{my_df.step.tolist()}::smallint[]) step,
                             unnest(ARRAY{my_df.crm_id.tolist()}::text[]) crm_id,
                             unnest(ARRAY{pd.to_datetime(my_df.order_dt).astype(str).tolist()}::timestamp[]) order_dt,
                             unnest(ARRAY{pd.to_datetime(my_df.due_dt).astype(str).tolist()}::timestamp[]) due_dt)""")
        print('2')
        cur.execute(f"""CREATE INDEX trex_idx On tmp_rec_update (order_id)""")
        print('idx')
        try:
            if update:
                update_recurring_true(conn=False, cur=cur)
                print("3")
                update_recurring_false(cur)
                conn.commit()
                print('4')
            if check:
                check_orders(conn)
                print('5')
            cur.execute("DROP TABLE tmp_rec_update")
            print('6')
            conn.commit()
            cur.close()
            conn.close()

        except Exception as e:
            conn.rollback()
            cur.close()
            conn.close()
            raise e

        return







