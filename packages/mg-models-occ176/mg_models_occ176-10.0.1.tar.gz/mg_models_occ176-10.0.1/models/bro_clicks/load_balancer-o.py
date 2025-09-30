import random
from models.db import Db, pd
from models.bro_clicks.initial_routes import InitialRoutes, ForeignInitialRoutes
from calendar import monthrange
import datetime as dt
from models import config
from threading import Thread, Lock
from copy import deepcopy

class LoadBalancer(Db):
    _max_decline_attempts = 5
    def __init__(self, db, db_p, account_id='54407332', **kw):
        Db.__init__(self, db, f"bro_clicks", 'load_balancer_2')
        self.set_constraint('load_balancer_2_pk', ['date', 'crm_id', 'gateway_id', 'router_id'])
        self.db_p = db_p
        self._account_id = account_id

    @staticmethod
    def set_max_decline_attempts(attempts):
        LoadBalancer._max_decline_attempts = int(attempts)
        print(f'max decline attempts set to {attempts}', flush=True)

    @staticmethod
    def now():
        return dt.datetime.now() - dt.timedelta(hours=config.timeOffset)

    @staticmethod
    def today():
        return LoadBalancer.now().date()

    @staticmethod
    def get_first_om():
        now = LoadBalancer.now()
        return dt.datetime(year=now.year, month=now.month, day=1)

    @staticmethod
    def get_last_dom(now=False):
        now = now if now else LoadBalancer.now()
        weekday_of, last_day = monthrange(now.year, now.month)
        return last_day

    @staticmethod
    def get_drim():
        now = LoadBalancer.now()
        return LoadBalancer.get_last_dom() - now.day + 1

    def get_processing_for_month(self, crm_id):
        qry = f"""
                select b.gateway_id, count(a.order_id)::int  initial_count_mtd from  augmented_data.order_cycles a 
                inner join crm_global.orders  b on  a.order_id  = b.order_id and a.crm_id  =  b.crm_id   and a.crm_id = '{crm_id}'
                where a.time_stamp  > '{self.get_first_om()}' and a.time_stamp < '{self.today()}'::timestamp
                      and a.bc_inferred  = 0
                      and a.decline_reason is null
                      and b.is_test_cc::int <> '1'                                            
                group by b.gateway_id
        """

        # print(qry)
        return pd.read_sql(qry, self.db_p.engine).fillna(0)

    def init_date(self, date, crm_id, reset_cap_count=True):
        sk = f'ui_{self._account_id}_clients'
        real_cap_space = self.get_processing_for_month(crm_id) if reset_cap_count else None

        qry = f"""
                SELECT '{date}'::date as date,  b.crm_id, a.mid_id,   b.gateway_id, b.step, a.processor,                  
                                                coalesce(e.approved, 0)  approved,  coalesce(e.approved,0) initial_count, c.dly_initial_cap,  b.minimum_price, coalesce(e.declined, 0) declined, 
                                                d.approval_rate,  c.dly_min_approval_rate, array_to_string(c.pr_exclude_cc_types,  ',') exclude_cc_types , 
                                                c.date_added, c.enable_tds, array_to_string(c.tds_exclude_cc_types, ',') tds_exclude_cc_types,  c.enabled, c.enable_initials, c.monthly_initial_cap, c.priority, c.router_id,  d.router_id as cur_router_id,                                                
                                                d.soft_cap_alerted, d.initial_count_mtd  as  prev_mtd                      

                FROM {sk}.mids a 
                LEFT JOIN {sk}.steps b on b.mid_id = a.mid_id 
                LEFT JOIN {sk}.gateway_settings c on c.gateway_id = b.gateway_id and c.crm_id = b.crm_id
                LEFT JOIN {self.schema}.{self.table} d on c.gateway_id =d.gateway_id and c.crm_id = d.crm_id and  b.step = d.step and '{date}'::date =d.date
                LEFT JOIN (select  crm_id, gateway_id, coalesce(sum(declined),  0) declined,   coalesce(sum(approved), 0) approved 
                            from {self.schema}.conversions where  coalesce(test, 0) <>  1 and time_stamp::date =  '{date}'::date group by crm_id, gateway_id
                            ) e on  e.gateway_id =c.gateway_id and e.crm_id=c.crm_id
                where (b.close_date is  null or b.close_date >'{self.today()}')
                    and b.crm_id = '{crm_id}' 
                    and b.gateway_id is not null
                    and a.processor not ilike '%%virtual%%'
                    and b.gateway_id::int <> 1
                    and a.processor != 'FlexCharge'                    

            """

        try:

            # if crm_id != 'crm_ll_2':
            #

            # print(qry)
            #     print('break')
            up = pd.read_sql(qry, self.engine)

            up = up.sort_values('step').drop_duplicates(['gateway_id', 'cur_router_id'], keep='first')
            up = up.loc[~up.router_id.isna()]
            up = up.explode('router_id')

            # delete  changes to routers
            del_gt_msk = (up.router_id != up.cur_router_id) & (
                up.gateway_id.isin(up.loc[~up.cur_router_id.isna()].gateway_id.unique()))
            del_gtys = up.loc[del_gt_msk].gateway_id.tolist()

            up = up.loc[(~up.gateway_id.isin(del_gtys)) | (~up.cur_router_id.isna())]

            # delete  changes to routers
            del_gt_msk = (up.router_id != up.cur_router_id)
            del_gtys = up.loc[del_gt_msk].gateway_id.tolist()
            self.engine.execute(
                f"delete from {self.schema}.{self.table} where gateway_id::int = ANY(ARRAY{del_gtys}::int[]) and  crm_id='{crm_id}'")
            up = up.drop(columns='cur_router_id')
        except Exception as e:
            raise e
        if reset_cap_count:
            try:
                up = up.merge(real_cap_space, on=['gateway_id'], how='left')
                up.initial_count_mtd = up.initial_count_mtd.fillna(0)
                up.initial_count_mtd += up.initial_count

            except:
                up['initial_count_mtd'] = up.prev_mtd.fillna(0)
                up.initial_count_mtd = up.initial_count_mtd.fillna(0)

            drim = float(self.get_drim())
            up.dly_initial_cap = pd.np.floor((up.monthly_initial_cap - up.initial_count_mtd) / drim)
            up.loc[up.dly_initial_cap < 0, 'dly_initial_cap'] = 0

        up.dly_initial_cap = up.dly_initial_cap.fillna(11)
        up.dly_min_approval_rate = up.dly_min_approval_rate.fillna(30)
        up.declined = up.declined.fillna(0)
        up.approval_rate = up.approval_rate.fillna(0)
        up.soft_cap_alerted = up.soft_cap_alerted.fillna(False)
        up.drop('prev_mtd', axis=1, errors='ignore', inplace=True)
        up = up.drop_duplicates(['gateway_id', 'router_id'])
        # self.engine.execute(f'truncate {self.schema}.{self.table}')
        self.upsert(up.dropna())

    def _increment_conversion(self, date, gateway_id, crm_id, approved, recurs_attempt=0, **kwargs):
        inc_p = '(initial_count +1)'
        m_inc_p = '(initial_count_mtd +1)'
        dnc_p = '(declined + 1)'
        inc = 'initial_count'
        m_inc = 'initial_count_mtd'
        dnc = 'declined'
        try:
            qry = f"""
                UPDATE {self.schema}.{self.table} 
                set   {f"{inc} ={inc_p},  approval_rate = ({inc_p}::numeric / ({dnc}+{inc_p}::numeric))*100, {m_inc} = {m_inc_p}" if approved
            else f"{dnc} ={dnc_p}, approval_rate = case when {inc}>0 then ({inc} / ({dnc_p}+{inc}))*100 else 0 end "
            }
                where crm_id = '{crm_id}' and date = '{date}'::date and gateway_id='{gateway_id}'                
                returning gateway_id  
            """

            if self.engine.execute(qry).scalar() is None and not recurs_attempt:
                self.init_date(date, crm_id)
                if not recurs_attempt:
                    return self._increment_conversion(date, gateway_id, crm_id, approved, recurs_attempt + 1)

        except Exception as e:
            print(e)
            return False
        return True

    def increment_conversion(self, date, gateway_id, crm_id, approved, **kwargs):
        return self._increment_conversion(date, gateway_id, crm_id, approved, recurs_attempt=0, **kwargs)

    def set_soft_cap_alerted(self, crm_id):
        self.engine.execute(
            f"""Update {self.schema}.{self.table} set  soft_cap_alerted=true where crm_id= '{crm_id}'""")

    def disable(self, crm_id, gateway_id):
        self.engine.execute(
            f"""Update {self.schema}.{self.table} set enable_initials=false where crm_id= '{crm_id}' and gateway_id = '{int(gateway_id)}'""")
        self.db_p.engine.execute(
            f"update ui_54407332_clients.gateway_settings set enable_initials=false where crm_id='{crm_id}' and gateway_id='{gateway_id}'")


class LoadBalancerV2(LoadBalancer):
    def __init__(self, db, db_p, account_id='54407332', alert_call_back=False, **kwargs):
        LoadBalancer.__init__(self, db, db_p, account_id=account_id)
        self.alert_cb = alert_call_back

        self.sort_map = {
            # No optimization
            4: {'by': ['priority', 'date_added', 'fill_pct', 'approval_rate', 'initial_count'],
                'ascending': [False, False, True, False, True]}
        }

    def gty_qry(self, crm_id, date, step, processor, cc_type=False, decs='', proc_excl=[], is_tds=None, is_decline_salvage=False, **kw):
        p_ex = ''
        if proc_excl and len(proc_excl) and not processor:
            p_ex = f"and a.processor not ilike all(ARRAY{[f'%%{p}%%' for p in proc_excl]}::text[])"

        return f""" --LEFT HERE NEED TO GET MCC!
                     select a.gateway_id::int,  a.fill_pct,a.dly_initial_cap,priority,initial_count,  a.approval_rate, a.date_added, a.processor, a.mid_id, a.monthly_initial_cap, a.soft_cap_alerted, initial_count_mtd,b.mcc from {self.schema}.{self.table} a
                     inner join (select crm_id,  gateway_id,  mcc from ui_54407332_clients.steps ) b  on b.crm_id =  a.crm_id and  b.gateway_id=a.gateway_id
                      {"inner join (select crm_id, gateway_id where enable_decline_salvage) ds on ds.crm_id = a.crm_id and ds.gateway_id::int = a.gateway_id::int" if is_decline_salvage else "" }
                     inner join processing.cap c on a.mid_id = c.mid_id and a.step=c.step and a.processor=c.processor   and c.monthly_available > 200
                      {f"left join processing.cap_cc_type d on a.mid_id = d.mid_id and a.step= d.step  and a.processor = d.processor and d.cc_type = '{cc_type}' " if cc_type else ''}

                     where date = '{date}'::date and a.crm_id = '{crm_id}' and router_id = '{step if step in [1, 11] else 2}' and enabled and enable_initials
                                  {f"and a.processor = '{processor}'" if processor else ""}
                                   {f"and (exclude_cc_types is null or  exclude_cc_types::text  not ilike '%%{cc_type.lower()}%%')" if cc_type else ''}
                                   and (approval_rate > dly_min_approval_rate or(declined+initial_count<110))
                                   {'and (d.available_tc is null or d.available_tc >50)' if cc_type else ''}
                                   {decs}
                                   {p_ex}
                                   {f"and enable_tds = {bool(is_tds)}" if is_tds else ""}
                                   {f"and (tds_exclude_cc_types is null or tds_exclude_cc_types not ilike '%%{cc_type}%%')" if cc_type and is_tds else ""}
                                   --and fill_pct < 1                         
                     --order by date_added desc, approval_rate desc, fill_pct asc limit 1
                       order by priority desc, date_added  desc, fill_pct, approval_rate desc, initial_count

                 """

    def exclude_list(self, crm_id, step, click_id, alias=''):
        decs = pd.read_sql(f"""SELECT  gateway_id, processor, approved  from {self.schema}.conversions 
                                where crm_id = '{crm_id}'  and click_id  = '{click_id}' and decline_reason not ilike 'prepaid%%' """,
                           self.engine)

        whd = ""
        if len(decs):
            decs.gateway_id = decs.gateway_id.fillna(-1)
            decs.processor = decs.processor.fillna('')
            processors = decs.loc[decs.approved == 0].processor.astype(str).tolist()
            if len(processors) > self._max_decline_attempts:
                raise Exception('declined due to too many attempts')
            p_break = []
            for p in processors:
                p_break.extend(p.split(' '))

            whd = f"""and {alias}gateway_id != all(ARRAY{decs.gateway_id.astype(int).tolist()}) 
                                 {f"and {alias}processor not ilike all(ARRAY{[f'%%{p}%%' for p in p_break]})" if len(p_break) else ""}"""

        return whd

    def next_gateway(self, crm_id, date, step, click_id='', processor=False, cc_type=None, recurse=0, decs=False,
                     proc_excl=[], is_tds=None,
                     **kwargs):
        try:
            decs = self.exclude_list(crm_id, step, click_id, alias='a.') if not decs else decs
        except Exception as e:
            return str(e)

        qry = self.gty_qry(crm_id, date, step, processor, cc_type, decs, proc_excl, is_tds=is_tds, **kwargs)
        # print(qry)
        res = None
        try:
            res = pd.read_sql(qry, self.engine)
        except Exception as e:
            print(str(e))
        if res is None or not len(res):
            if not decs:
                if not recurse and is_tds is not None:
                    return self.next_gateway(crm_id, date, step, click_id, processor, cc_type, recurse=recurse + 1,
                                             is_tds=not is_tds)
                elif recurse == 1:
                    self.init_date(date, crm_id)
                    return self.next_gateway(crm_id, date, step, click_id, processor, cc_type, recurse=recurse + 1,
                                             is_tds=is_tds)
                elif recurse == 2 and is_tds is not None:
                    return self.next_gateway(crm_id, date, step, click_id, processor, cc_type, recurse=recurse + 1,
                                             is_tds=None)

                return 'out of processing'
            else:
                return 'declined due to too many attempts'
        r = res.loc[res.fill_pct < 1]

        #  HARD CAP
        if not len(r):
            res = res.sort_values(['dly_initial_cap'], ascending=False).sort_values(['fill_pct'])

            def _get_aft_sc():
                nonlocal res
                if not len(res):
                    return 'out of processing'
                r2 = res.to_dict(orient='records')[0]
                if r2['initial_count_mtd'] >= r2['monthly_initial_cap']:
                    self.alert_cb('hard_cap_alert', crm_id=crm_id, gateway_id=r2['gateway_id'])
                    self.disable(crm_id=crm_id, gateway_id=r2['gateway_id'])
                    res = res.loc[res.gateway_id != r2['gateway_id']]
                    return _get_aft_sc()
                r2['is_tds'] = is_tds
                return r2

            if ~res.soft_cap_alerted.any():
                cnt = self.engine.execute(
                    f"""select count(*) from  {self.schema}.{self.table}  where date = '{date}'::date and crm_id = '{crm_id}' and router_id = '{step if step == 1 else 2}' and enabled and enable_initials and fill_pct<1""").scalar()
                if cnt == 0 or cnt is None:
                    self.alert_cb('soft_cap_alert', crm_id=crm_id)
                    self.set_soft_cap_alerted(crm_id)
            return _get_aft_sc()
        r = r.to_dict(orient='records')[0]
        r['is_tds'] = is_tds
        return r

    def increment_conversion(self, date, gateway_id, crm_id, approved, **kwargs):

        return self._increment_conversion(date, gateway_id, crm_id, approved, recurs_attempt=0, **kwargs)


class LoadBalancerV3(LoadBalancerV2):
    routes = None
    _lock_static = Lock()
    _lock_static_route_get = Lock()
    _lock_model_replace = Lock()
    _last_updated = False
    _max_stale_seconds = random.randint(600, 1200)
    _route_schema = 'initial_route'

    def __init__(self, db, db_p, account_id='54407332', alert_call_back=False,
                 min_sample_count=500, optimise_pct=0.1,
                 randomise_pct=0.1, opt_type=4,
                 route_methods=['bank_conversion',
                                'cc_first_6_conversion',
                                'cc_type_conversion',
                                'cc_type_mcc_conversion',
                                'cc_type_cc_level_conversion',
                                ],
                 rewrite_route=True,
                 iin_schema='bro_clicks',

                 **kwargs):
        if rewrite_route:
            LoadBalancerV3._route_schema = 'initial_route'
        self._iin_schema = iin_schema
        self._model_class = InitialRoutes
        LoadBalancerV2.__init__(self, db, db_p, account_id=account_id, alert_call_back=alert_call_back, **kwargs)
        self._opt_arr = self._rand_arr(100, opt_type, {'key': 1, 'pct': randomise_pct}, {'key': 2, 'pct': optimise_pct})
        self._route_methods = route_methods
        self._opt_val = self.get_opt_type()
        print('opt val', self._opt_val, 'opt_type', opt_type)
        self._min_sample_count = min_sample_count
        self._t_get_bin = False
        self.iin_info = None
        self.is_iin_data = False
        self._t_get_route = False
        self.sort_map = {
            # Random
            1: {'by': ['fill_pct', 'initial_count'], 'ascending': [True, True]},
            # Pure conversion rate
            2: {'by': ['conversion_rate', 'initial_count'], 'ascending': [False, True]},
            # Hybrid optimization
            3: {'by': ['priority', 'conversion_rate', 'date_added', 'fill_pct', 'approval_rate', 'initial_count'],
                'ascending': [False, False, False, True, False, True]},
            # No optimization
            4: {'by': ['priority', 'date_added', 'fill_pct', 'approval_rate', 'initial_count'],
                'ascending': [False, False, True, False, True]}
        }
        self._join_on_del = False
        self.init_static(db_p, route_methods=route_methods)

    def __del__(self):
        self._joiner(self._t_get_bin)
        # self._join_lb()

    @staticmethod
    def _rand_arr(length, default_val, *settings):
        a = []
        for s in settings:
            a += [s['key'] for i in range(int(length * s['pct']))]
        a += [default_val for i in range(length - len(a))]
        return a

    @staticmethod
    def _rand_val(arr):
        try:
            return arr[random.randint(0, 100)]
        except Exception as e:
            print(str(e))
        return 1

    def get_opt_type(self):
        return self._rand_val(self._opt_arr)

    @staticmethod
    def _joiner(*threads):
        for t in threads:
            try:
                t.join()
            except:
                pass

    def set_bin_info(self, cc_first_6):
        def _exec():
            nonlocal cc_first_6
            self.iin_info = pd.read_sql(f"select * from {self._iin_schema}.iin_data where bin='{cc_first_6}'",
                                        self.db_p.engine).astype(str).applymap(str.lower).replace({'none': None})
            if len(self.iin_info):
                self.is_iin_data = True
                self.iin_info = self.iin_info.to_dict(orient='records')[0]
                if self.iin_info['bank_map'] is not None:
                    self.iin_info['bank'] = self.iin_info['bank_map']
                if 'level' not in self.iin_info:
                    self.iin_info['level'] = None
            else:
                self.iin_info = {}
            self.iin_info['cc_first_6'] = cc_first_6

        self._t_get_bin = Thread(target=_exec)
        self._t_get_bin.start()

    @staticmethod
    def get_auto_routes(db, route_methods=[
        'bank_conversion',
        'cc_first_6_conversion',
        'cc_type_conversion',
        'cc_type_mcc_conversion',
        'cc_type_cc_level_conversion'
    ]):
        threads = []
        print('LBV3 get auto routes')
        if LoadBalancerV3._lock_static_route_get.acquire(timeout=0.001):
            rts = pd.DataFrame()
            _lock_rt = Lock()

            def _getter(table, where=''):
                nonlocal _lock_rt, rts
                _rt = pd.read_sql(f"""select * from {LoadBalancerV3._route_schema}.{table} {where}""", db.engine)
                _rt['mod_type'] = table
                _lock_rt.acquire()
                rts = rts.append(_rt)
                _lock_rt.release()

            for r in route_methods:
                threads.append(Thread(target=_getter, args=(r,)))
                threads[len(threads) - 1].start()
            LoadBalancerV3._joiner(*threads)
            LoadBalancerV3._lock_model_replace.acquire()
            LoadBalancerV3.routes = rts.replace({'none': pd.np.nan})
            LoadBalancerV3._lock_model_replace.release()
            print('LBV3 get auto routes done')
            LoadBalancerV3._lock_static_route_get.release()
        else:
            print('LBV3 get auto routes static lock already acquired')

    def _join_lb(self):
        print('join lb')
        self._joiner(self._t_get_route)

    @staticmethod
    def async_del(lb):
        print('async del')
        lb._join_lb()

    @staticmethod
    def last_update_diff():
        lst = LoadBalancerV3._last_updated
        diff = (dt.datetime.now() - lst).total_seconds()
        return 50000 if lst is None else (dt.datetime.now() - lst).total_seconds()

    @staticmethod
    def check_stale_data():
        return LoadBalancerV3._max_stale_seconds < LoadBalancerV3.last_update_diff()

    def init_static(self, db, route_methods=['bank_conversion',
                                             'cc_first_6_conversion',
                                             'cc_type_conversion',
                                             'cc_type_mcc_conversion',
                                             'cc_type_cc_level_conversion'],
                    **kwargs):

        if LoadBalancerV3._lock_static.acquire(timeout=0.001):

            lb = LoadBalancerV3
            try:
                if not lb._last_updated or lb.routes is None or not len(lb.routes) or LoadBalancerV3.check_stale_data():
                    print('init_static')
                    LoadBalancerV3._last_updated = dt.datetime.now()

                    self._t_get_route = Thread(target=lb.get_auto_routes, args=(db, route_methods))
                    self._t_get_route.start()
                else:
                    print('LBV3 cache is up to date')
            except Exception as e:
                print('LBV3 static init exception', str(e))

            LoadBalancerV3._lock_static.release()
        else:
            print('LBV3 init static lock already aquired')
        return LoadBalancerV3

    @staticmethod
    def update_static(cc_type, cc_first_6, processor, mcc, bank, level, mod_types=False):
        try:
            LoadBalancerV3._lock_static.acquire()
            if not mod_types:
                mod_types = list(LoadBalancerV3.routes.unique())
            if 'cc_first_6_conversion' in mod_types:
                pass
        except Exception as e:
            print(f'LB update static failed: {str(e)}')
        LoadBalancerV3._lock_static.release()

    def set_iin(self, **kwargs):

        if self.iin_info is None or not len(self.iin_info):
            self.iin_info = kwargs
        else:
            self.iin_info = {**self.iin_info, **kwargs}
        if 'approved' in self.iin_info:
            self.iin_info.pop('approved')
        if 'declined' in self.iin_info:
            self.iin_info.pop('declined')
        if 'conversion_rate' in self.iin_info:
            self.iin_info.pop('conversion_rate')
        if 'level' not in self.iin_info:
            self.iin_info['level'] = None

    def next_gateway(self, crm_id, date, step, click_id='', processor=False, cc_type=None, cc_first_6=False, recurse=0,
                     decs=False, ignore_user_exclusions=None,
                     proc_excl=[], is_tds=None, **kwargs):
        # opt vals 1 = random gateway constrained only by cap,  2 = optimised gateway constrained only by cap, 3 = Hybrid approach not ignoring settings, 4 = over cap (over-rides to that if needed)

        if ignore_user_exclusions is None:
            ignore_user_exclusions = self._opt_val < 2
        if cc_first_6:
            self.set_bin_info(cc_first_6)
        try:
            decs = self.exclude_list(crm_id, step, click_id, 'a.') if not decs else decs
        except Exception as e:
            return str(e)
        self._joiner(self._t_get_bin)

        try:
            qry = self.gty_qry(crm_id, date, step, processor, cc_type, decs, proc_excl=proc_excl, is_tds=is_tds, **kwargs)
            res = pd.read_sql(qry, self.engine)
            cc_type = cc_type.lower()
            if 'master' in cc_type:
                cc_type = 'master'
            if self._opt_val > 1 and self._opt_val < 4 and self.routes is not None:

                self._lock_model_replace.acquire()
                mod = self.routes if self.is_iin_data else self.routes.loc[
                    self.routes.mod_type.isin(['cc_type_conversion', 'cc_type_mcc_conversion'])]
                self._lock_model_replace.release()
                mod = mod.loc[(mod.approved + mod.declined >= self._min_sample_count)
                              & (mod.conversion_rate != 1)  # take out dummy gateways
                              & ((mod.cc_first_6 == cc_first_6) | (mod.cc_first_6.isna()))
                              & (((mod.cc_type == cc_type) | mod.cc_type.isna()) if 'cc_type' in mod.columns else (
                    True))
                              & (((mod.cc_level == str(self.iin_info['level'])) | (
                    mod.cc_level.isna())) if self.is_iin_data and 'level' in self.iin_info else (True))
                              & (((mod.bank == str(self.iin_info['bank'])) | (
                    mod.bank.isna())) if self.is_iin_data and 'bank' in self.iin_info else (True))
                              ]

                df_opt = mod.copy().sort_values('conversion_rate', ascending=False).reset_index(drop=True)
                df_opt['r_rank'] = df_opt.index + 1

                # Optimization Filters

                res = res.merge(df_opt.loc[df_opt.mod_type.isin(
                    ['cc_type_mcc_conversion', 'bank_conversion', 'cc_first_6_conversion'])],
                                on=['processor', 'mcc'],
                                how='left').append(res.merge(
                    df_opt.loc[df_opt.mod_type.isin(['cc_type_cc_level_conversion', 'cc_type_conversion'])].drop('mcc',
                                                                                                                 axis=1),
                    on=['processor'],
                    how='left')).drop_duplicates()
                # r_rank is Highest to lowest in terms of strength same as priority
                res.mod_type = res.mod_type.fillna('undefined').replace({'nan': 'undefined', '': 'undefined'})
                res.conversion_rate = res.conversion_rate.fillna(0)
            else:
                res['conversion_rate'] = 0
            res = res.sort_values(**self.sort_map[self._opt_val]).drop_duplicates('gateway_id', keep='first')
            res['cc_type'] = cc_type
            res['cc_first_6'] = cc_first_6
            self.set_iin(cc_first_6=cc_first_6, cc_type=cc_type)
        except Exception as e:
            print('LBV3 error', str(e))
            raise e

        if res is None or not len(res):
            if not decs:
                if not recurse and is_tds is not None:
                    return self.next_gateway(crm_id, date, step, click_id, processor, cc_type, recurse=recurse + 1,
                                             is_tds=not is_tds)
                elif recurse == 1:
                    self.init_date(date, crm_id)
                    return self.next_gateway(crm_id, date, step, click_id, processor, cc_type, recurse=recurse + 1,
                                             is_tds=is_tds)
                elif recurse == 2 and is_tds is not None:
                    return self.next_gateway(crm_id, date, step, click_id, processor, cc_type, recurse=recurse + 1,
                                             is_tds=not is_tds)
                return 'out of processing'
            else:
                return 'declined due to too many attempts'

        r = res.loc[res.fill_pct < 1]
        if 'conversion_rate' not in res:
            res['conversion_rate'] = 0
        #  HARD CAP
        if not len(r):

            res = res.sort_values(['dly_initial_cap', 'conversion_rate'], ascending=[True, False]).sort_values(
                ['fill_pct'])

            def _get_aft_sc():
                nonlocal res
                if not len(res):
                    return 'out of processing'
                r2 = res.to_dict(orient='records')[0]
                if r2['initial_count_mtd'] >= r2['monthly_initial_cap']:
                    self.alert_cb('hard_cap_alert', crm_id=crm_id, gateway_id=r2['gateway_id'])
                    self.disable(crm_id=crm_id, gateway_id=r2['gateway_id'])
                    res = res.loc[res.gateway_id != r2['gateway_id']]
                    return _get_aft_sc()
                self.set_iin(**r2)
                r2['is_tds'] = is_tds
                return r2

            # SOFT CAP
            if ~res.soft_cap_alerted.any():
                cnt = self.engine.execute(
                    f"""select count(*) from  {self.schema}.{self.table}  
                    where date = '{date}'::date and crm_id = '{crm_id}' 
                    and router_id = '{step if step == 1 else 2}' 
                    and enabled and enable_initials and fill_pct<1
                    """).scalar()
                if cnt == 0 or cnt is None:
                    self.alert_cb('soft_cap_alert', crm_id=crm_id)
                    self.set_soft_cap_alerted(crm_id)
            return _get_aft_sc()
        r = r.to_dict(orient='records')[0]
        if cc_type:
            r['cc_type'] = cc_type
        if cc_first_6:
            r['cc_first_6'] = cc_first_6

        self.set_iin(**r)
        r['is_tds'] = is_tds
        return r

    def update_models(self, approved, test=0, **kwargs):

        if self.routes is None:
            return

        if not int(test):
            self._lock_model_replace.acquire()
            r = self.routes.mod_type.unique()
            self._lock_model_replace.release()
            for k in r:
                _in = deepcopy(self.iin_info)
                self.iin_info.pop('response_code',None)
                getattr(self._model_class, k)(self.db_p).increment_conversion(approved, list(self.routes.columns),
                                                                              **{**_in, **kwargs})

    def add_test_result(self, crm_id, order_id, approved, optimised, test=0, **kwargs):
        try:
            self._model_class.optimised_orders(self.db_p).upsert(
                pd.DataFrame([{**self.iin_info, **{'crm_id': crm_id, 'order_id': order_id, 'is_optimised': optimised,
                                                   'is_test_cc': int(test), 'approved': int(approved)}}]))
        except Exception as e:
            # raise e
            print('LB ADD TEST RESULT ERROR', str(e))

    def increment_conversion(self, date, gateway_id, crm_id, approved, order_id, **kwargs):
        self.update_models(approved, **kwargs)
        self.add_test_result(crm_id, order_id, approved, self._opt_val, **kwargs)
        return self._increment_conversion(date, gateway_id, crm_id, approved, recurs_attempt=0, **kwargs)


class LoadBalancerV4(LoadBalancerV3):
    LoadBalancerV3._route_schema = 'foreign_initial_route'

    def __init__(self, *args, **kw):
        LoadBalancerV3.__init__(self, *args, rewrite_route=False, **kw)
        self._model_class = ForeignInitialRoutes
        self._iin_schema = 'foreign_bins'

    def next_gateway(self, crm_id, date, step, click_id='', processor=False, cc_type=None, cc_first_6=False, recurse=0,
                     decs=False, ignore_user_exclusions=None,
                     proc_excl=[], is_tds=None, is_prepaid=True, **kwargs):
        # opt vals 1 = random gateway constrained only by cap,  2 = optimised gateway constrained only by cap, 3 = Hybrid approach not ignoring settings, 4 = over cap (over-rides to that if needed)
        if is_prepaid is None:
            raise TypeError('is_prepaid value must be pass as a boolean got NoneType')

        if is_prepaid:
            pp_campaign_class = 'prepaid'
        else:
            pp_campaign_class = 'post_paid'
        if ignore_user_exclusions is None:
            ignore_user_exclusions = self._opt_val < 2
        if cc_first_6:
            self.set_bin_info(cc_first_6)
        try:
            decs = self.exclude_list(crm_id, step, click_id, 'a.') if not decs else decs
        except Exception as e:
            return str(e)
        self._joiner(self._t_get_bin)

        try:
            qry = self.gty_qry(crm_id, date, step, processor, cc_type, decs, proc_excl=proc_excl, is_tds=is_tds,
                               is_prepaid=is_prepaid, **kwargs)
            res = pd.read_sql(qry, self.engine)
            cc_type = cc_type.lower()
            if 'master' in cc_type:
                cc_type = 'master'
            if self._opt_val > 1 and self._opt_val < 4 and self.routes is not None:

                self._lock_model_replace.acquire()
                mod = self.routes if self.is_iin_data else self.routes.loc[
                    self.routes.mod_type.isin(['cc_type_conversion', 'cc_type_mcc_conversion'])]
                self._lock_model_replace.release()
                mod = mod.loc[(mod.approved + mod.declined >= self._min_sample_count)
                              # & (mod.conversion_rate != 1)  # take out dummy gateways
                              & ((mod.cc_first_6 == cc_first_6) | (mod.cc_first_6.isna()))
                              & (mod.campaign_class == pp_campaign_class)
                              & (((mod.cc_type == cc_type) | mod.cc_type.isna()) if 'cc_type' in mod.columns else (
                    True))
                              & (((mod.cc_level == str(self.iin_info['level'])) | (
                    mod.cc_level.isna())) if self.is_iin_data and 'level' in self.iin_info else (True))
                              & (((mod.bank == str(self.iin_info['bank'])) | (
                    mod.bank.isna())) if self.is_iin_data and 'bank' in self.iin_info else (True))
                              ]

                df_opt = mod.copy().sort_values('conversion_rate', ascending=False).reset_index(drop=True)
                df_opt['r_rank'] = df_opt.index + 1

                # Optimization Filters

                res = res.merge(df_opt.loc[df_opt.mod_type.isin(
                    ['cc_type_mcc_conversion', 'bank_conversion', 'cc_first_6_conversion'])],
                                on=['processor', 'mcc'],
                                how='left').append(res.merge(
                    df_opt.loc[df_opt.mod_type.isin(['cc_type_cc_level_conversion', 'cc_type_conversion'])].drop('mcc',
                                                                                                                 axis=1),
                    on=['processor'],
                    how='left')).drop_duplicates()
                # r_rank is Highest to lowest in terms of strength same as priority
                res.mod_type = res.mod_type.fillna('undefined').replace({'nan': 'undefined', '': 'undefined'})
                res.conversion_rate = res.conversion_rate.fillna(0)
            else:
                res['conversion_rate'] = 0
            res = res.sort_values(**self.sort_map[self._opt_val]).drop_duplicates('gateway_id', keep='first')
            res['cc_type'] = cc_type
            res['cc_first_6'] = cc_first_6
            self.set_iin(cc_first_6=cc_first_6, cc_type=cc_type)
        except Exception as e:
            print('LBV4 error', str(e))
            raise e

        if res is None or not len(res):
            if not decs:
                if not recurse and is_tds is not None:
                    return self.next_gateway(crm_id, date, step, click_id, processor, cc_type, recurse=recurse + 1,
                                             is_tds=not is_tds, is_prepaid=is_prepaid)
                elif recurse == 1:
                    self.init_date(date, crm_id)
                    return self.next_gateway(crm_id, date, step, click_id, processor, cc_type, recurse=recurse + 1,
                                             is_tds=is_tds, is_prepaid=is_prepaid)
                elif recurse == 2 and is_tds is not None:
                    return self.next_gateway(crm_id, date, step, click_id, processor, cc_type, recurse=recurse + 1,
                                             is_tds=not is_tds, is_prepaid=is_prepaid)
                return 'out of processing'
            else:
                # if len(decs) < 4:
                #     return 'out of processing'
                return 'declined due to too many attempts'
        r = res.loc[res.fill_pct < 1]
        if 'conversion_rate' not in res:
            res['conversion_rate'] = 0
        #  HARD CAP
        if not len(r):

            res = res.sort_values(['dly_initial_cap', 'conversion_rate'], ascending=[True, False]).sort_values(
                ['fill_pct'])

            def _get_aft_sc():
                nonlocal res
                if not len(res):
                    return 'out of processing'
                r2 = res.to_dict(orient='records')[0]
                if r2['initial_count_mtd'] >= r2['monthly_initial_cap']:
                    self.alert_cb('hard_cap_alert', crm_id=crm_id, gateway_id=r2['gateway_id'])
                    self.disable(crm_id=crm_id, gateway_id=r2['gateway_id'])
                    res = res.loc[res.gateway_id != r2['gateway_id']]
                    return _get_aft_sc()
                self.set_iin(**r2)
                r2['is_tds'] = is_tds
                return r2

            # SOFT CAP
            if ~res.soft_cap_alerted.any():
                cnt = self.engine.execute(
                    f"""select count(*) from  {self.schema}.{self.table}  
                    where date = '{date}'::date and crm_id = '{crm_id}' 
                    and router_id = '{step if step == 1 else 2}' 
                    and enabled and enable_initials and fill_pct<1
                    """).scalar()
                if cnt == 0 or cnt is None:
                    self.alert_cb('soft_cap_alert', crm_id=crm_id)
                    self.set_soft_cap_alerted(crm_id)
            return _get_aft_sc()
        r = r.to_dict(orient='records')[0]
        if cc_type:
            r['cc_type'] = cc_type
        if cc_first_6:
            r['cc_first_6'] = cc_first_6

        self.set_iin(**r)
        r['is_tds'] = is_tds
        return r


class LoadBalancerV5(LoadBalancerV4):
    def __init__(self, *args, **kw):
        LoadBalancerV4.__init__(self, *args, **kw)
        self._model_class = ForeignInitialRoutes
        self._iin_schema = 'foreign_bins'

    def init_date(self, date, crm_id, reset_cap_count=True):
        sk = f'ui_{self._account_id}_clients'
        real_cap_space = self.get_processing_for_month(crm_id) if reset_cap_count else None

        qry = f"""
                SELECT '{date}'::date as date,  b.crm_id, a.mid_id,   b.gateway_id, b.step, a.processor,                  
                                                coalesce(e.approved, 0)  approved,  coalesce(e.approved,0) initial_count, c.dly_initial_cap,  b.minimum_price, coalesce(e.declined, 0) declined, 
                                                d.approval_rate,  c.dly_min_approval_rate, array_to_string(c.pr_exclude_cc_types,  ',') exclude_cc_types , 
                                                c.date_added, c.enable_tds, array_to_string(c.tds_exclude_cc_types, ',') tds_exclude_cc_types,  c.enabled, c.enable_initials, c.monthly_initial_cap, c.priority, c.router_id,  d.router_id as cur_router_id,                                                
                                                c.allow_prepaid, c.allow_non_prepaid,
                                                d.soft_cap_alerted, d.initial_count_mtd  as  prev_mtd                      

                FROM {sk}.mids a 
                LEFT JOIN {sk}.steps b on b.mid_id = a.mid_id 
                LEFT JOIN {sk}.gateway_settings c on c.gateway_id = b.gateway_id and c.crm_id = b.crm_id
                LEFT JOIN {self.schema}.{self.table} d on c.gateway_id =d.gateway_id and c.crm_id = d.crm_id and  b.step = d.step and '{date}'::date =d.date
                LEFT JOIN (select  crm_id, gateway_id, coalesce(sum(declined),  0) declined,   coalesce(sum(approved), 0) approved 
                            from {self.schema}.conversions where  coalesce(test, 0) <>  1 and time_stamp::date =  '{date}'::date group by crm_id, gateway_id
                            ) e on  e.gateway_id =c.gateway_id and e.crm_id=c.crm_id
                where (b.close_date is  null or b.close_date >'{self.today()}')
                    and b.crm_id = '{crm_id}'
                    and b.gateway_id is not null
                    and a.processor not ilike '%%virtual%%'
                    and b.gateway_id::int <> 1
                    and a.processor != 'FlexCharge'                    

            """

        try:

            # if crm_id != 'crm_ll_2':
            #

            # print(qry)
            #     print('break')
            up = pd.read_sql(qry, self.engine)

            up = up.sort_values('step').drop_duplicates(['gateway_id', 'cur_router_id'], keep='first')
            up = up.loc[~up.router_id.isna()]
            up = up.explode('router_id')

            # delete  changes to routers
            del_gt_msk = (up.router_id != up.cur_router_id) & (
                up.gateway_id.isin(up.loc[~up.cur_router_id.isna()].gateway_id.unique()))
            del_gtys = up.loc[del_gt_msk].gateway_id.tolist()

            up = up.loc[(~up.gateway_id.isin(del_gtys)) | (~up.cur_router_id.isna())]

            # delete  changes to routers
            del_gt_msk = (up.router_id != up.cur_router_id)
            del_gtys = up.loc[del_gt_msk].gateway_id.tolist()
            self.engine.execute(
                f"delete from {self.schema}.{self.table} where gateway_id::int = ANY(ARRAY{del_gtys}::int[]) and  crm_id='{crm_id}'")
            up = up.drop(columns='cur_router_id')
        except Exception as e:
            raise e
        if reset_cap_count:
            try:
                up = up.merge(real_cap_space, on=['gateway_id'], how='left')
                up.initial_count_mtd = up.initial_count_mtd.fillna(0)
                up.initial_count_mtd += up.initial_count

            except:
                up['initial_count_mtd'] = up.prev_mtd.fillna(0)
                up.initial_count_mtd = up.initial_count_mtd.fillna(0)

            drim = float(self.get_drim())
            up.dly_initial_cap = pd.np.floor((up.monthly_initial_cap - up.initial_count_mtd) / drim)
            up.loc[up.dly_initial_cap < 0, 'dly_initial_cap'] = 0

        up.dly_initial_cap = up.dly_initial_cap.fillna(11)
        up.dly_min_approval_rate = up.dly_min_approval_rate.fillna(30)
        up.declined = up.declined.fillna(0)
        up.approval_rate = up.approval_rate.fillna(0)
        up.soft_cap_alerted = up.soft_cap_alerted.fillna(False)
        up.drop('prev_mtd', axis=1, errors='ignore', inplace=True)
        up = up.drop_duplicates(['gateway_id', 'router_id'])
        # self.engine.execute(f'truncate {self.schema}.{self.table}')
        self.upsert(up.dropna())

    def gty_qry(self, crm_id, date, step, processor, cc_type=False, decs='', proc_excl=[], is_tds=None,
                is_prepaid=False, is_decline_salvage=False, **kw):
        p_ex = ''
        if proc_excl and len(proc_excl) and not processor:
            p_ex = f"and a.processor not ilike all(ARRAY{[f'%%{p}%%' for p in proc_excl]}::text[])"

        return f""" --LEFT HERE NEED TO GET MCC!
                     select a.gateway_id::int,  a.fill_pct,a.dly_initial_cap,priority,initial_count,  a.approval_rate, a.date_added, a.processor, a.mid_id, a.monthly_initial_cap, a.soft_cap_alerted, initial_count_mtd,b.mcc from {self.schema}.{self.table} a
                     inner join (select crm_id,  gateway_id,  mcc from ui_54407332_clients.steps ) b  on b.crm_id =  a.crm_id and  b.gateway_id=a.gateway_id
                     {"inner join (select crm_id, gateway_id where enable_decline_salvage) ds on ds.crm_id = a.crm_id and ds.gateway_id::int = a.gateway_id::int" if is_decline_salvage else "" }
                     inner join processing.cap c on a.mid_id = c.mid_id and a.step=c.step and a.processor=c.processor and c.monthly_available > 50
                      {f"left join processing.cap_cc_type d on a.mid_id = d.mid_id and a.step= d.step  and a.processor = d.processor and d.cc_type = '{cc_type}' " if cc_type else ''}

                     where date = '{date}'::date and a.crm_id = '{crm_id}' and router_id = '{step if step in [1, 11] else 2}' and enabled and enable_initials
                                  {f"and a.processor = '{processor}'" if processor else ""}
                                   {f"and (exclude_cc_types is null or  exclude_cc_types::text  not ilike '%%{cc_type.lower()}%%')" if cc_type else ''}
                                   and (approval_rate > dly_min_approval_rate or(declined+initial_count<110))
                                   {'and (d.available_tc is null or d.available_tc >50)' if cc_type else ''}
                                   {decs}
                                   {p_ex}
                                   {f"and enable_tds = {bool(is_tds)}" if is_tds else ""}
                                   {f"and (tds_exclude_cc_types is null or tds_exclude_cc_types not ilike '%%{cc_type}%%')" if cc_type and is_tds else ""}
                                   {f"and allow_prepaid" if is_prepaid else ""}
                                   {f"and allow_non_prepaid" if not is_prepaid else ""}
                                   --and fill_pct < 1                         

                     --order by date_added desc, approval_rate desc, fill_pct asc limit 1
                       order by priority desc, date_added  desc, fill_pct, approval_rate desc, initial_count

                 """






