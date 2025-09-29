import random
from random import randint
from math import ceil
import pandas as pd, numpy as np
import math
from threading import Thread
from models import discount_stats
from models.gateways import GatewaySteps
import decimal

from models.db import Db
from copy import deepcopy

class Discounter:
    def __init__(self, anchor=20, pct_inc=5, l_devs=2, h_devs=2,  deviate=True):
        self.disc_map = [anchor - (pct_inc * (l_devs - i)) for i in range(l_devs)] + [20] + [anchor + (pct_inc * (h_devs - i)) for i in range(h_devs)]
        self.anchor = anchor
        self.deviate = deviate

    def get_pct(self):
        if not self.deviate:
            return self.anchor

        return self.disc_map[random.randint(0, len(self.disc_map)-1)]

    def batch_pct(self, df, col_key='discount_pct', price_key='order_total', new_price_key='dynamic_product_price'):
        if not len(df):
            return pd.DataFrame()
        d = df.copy()
        if col_key not in d.columns:
            d[col_key] = np.nan
        d[col_key] = d[col_key].apply(lambda x: self.disc_map[random.randint(0, len(self.disc_map)-1)])
        if price_key and price_key in d.columns and new_price_key:
            d[new_price_key] = np.round(d[price_key] * d[col_key] / 100, 2)
        return d

    def attempt_sample(self, decs, pct=0.4, force_order_key='enforce'):
        d_dec = decs.copy()
        nd_dec = pd.DataFrame()
        for attempt in d_dec.attempt.unique().tolist():
            a_dec = d_dec.loc[d_dec.attempt == attempt]
            idx = math.ceil(len(a_dec) * pct)
            an_dec = pd.DataFrame()
            if force_order_key and force_order_key in d_dec.columns:
                an_dec = self.batch_pct(
                    a_dec.loc[a_dec[force_order_key] > 0].sort_values('enforce')[:idx],
                    'rebill_discount_percent',
                    new_price_key=False
                )
                if len(an_dec):
                    a_dec = a_dec.loc[~a_dec.order_id.isin(an_dec.order_id)]
                    idx = idx - len(an_dec)
            if idx > 0:
                an_dec = an_dec.append(self.batch_pct(
                        a_dec.sample(frac=1)[:idx],
                        'rebill_discount_percent',
                        new_price_key=False
                ))
            nd_dec = nd_dec.append(an_dec)
        return nd_dec


class DiscountOptimizer:
    def __init__(self, db, crm_id, account_id='54407332', max_price=89.95,  opt_pct={'default': 0.1}, test_pct={'default': 0.5}, flexible_price_pct=0.05,  min_price=31.97, **kwargs):
        self._db = db
        self._crm_id = crm_id
        self._account_id = account_id

        self.model = None
        self._gty = None
        self._price_key = 'prc_bin'
        self._price_matrix = None
        self._test_matrix = None
        self._opt_pct = opt_pct
        self._test_pct = test_pct
        self.bin_use = 1
        self.bin_check = 1
        self.flex_price_pct = flexible_price_pct
        self.max_price = max_price
        self.min_price =min_price
        self._t_set_mod = Thread(target=self._set_mod)
        self._t_set_mod.start()

    def __del__(self):
        self._join(self._t_set_mod)

    @staticmethod
    def _join(t):
        if t:
            try:
                t.join()
                t = None
            except Exception as e:
                print(str(e))

    def _set_mod(self):
        self.model = discount_stats.ds_discount_model(self._db,  self.max_price,  self._crm_id)
        self._gty = GatewaySteps(self._db, self._account_id).get(
            ['crm_id', 'gateway_id', 'step', 'price', 'is_price_flexible'],
            where=f" where crm_id ='{self._crm_id}'")

    @staticmethod
    def _get_test_node(attempt, test_node):
        if attempt in test_node:
            return test_node[attempt]
        return test_node['default']

    @staticmethod
    def _get_pct_inc(attempt, dev_inc):
        if dev_inc:
            try:
                if attempt in dev_inc:
                    return dev_inc[attempt]
                return dev_inc['default']
            except KeyError:
                return 5
        return 5

    @staticmethod
    def _get_devs(attempt, dev_inc):
        if dev_inc:
            try:
                if attempt in dev_inc:
                    obj = dev_inc[attempt]
                else:
                    obj = dev_inc['default']
                if isinstance(obj, dict):
                    return obj

            except KeyError:
                pass
        return dict(l_devs=5, h_devs=5)

    def _set_test_matrix(self, inc_amt=10, dec_amt=0, test_node=False, test_dev_inc=False, test_devs=False, **kwargs):
        mod = []
        for s in self.model.step.unique():
            s_use = self.bin_use.loc[self.bin_use.step == s]
            att = s_use.discount_attempt.unique().tolist()
            att.append(s_use.discount_attempt.max() + 1)
            for i in att:
                last_prc = self._get_test_node(i, test_node) if test_node else self.best_bin(i, s) * 100
                if last_prc:
                    mod.append({'step': s,
                                'attempt': i,
                                'bin': last_prc,
                                'discounter': Discounter(
                                    anchor=last_prc + (inc_amt-dec_amt) if not test_node else last_prc,
                                    pct_inc=self._get_pct_inc(i, test_dev_inc),
                                    **self._get_devs(i, test_devs),

                                )})
        self._test_matrix = pd.DataFrame(mod)
        return self

    def _set_price_matrix(self, **kwargs):
        mod = []
        for s in self.model.step.unique():
            for i in self.bin_use.loc[self.bin_use.step == s].discount_attempt.unique():
                prc = self.best_bin(i, s) * 100
                mod.append({'step': s, 'attempt': i, 'bin': prc,
                            'discounter': Discounter(anchor=prc, pct_inc=2.5, l_devs=2, h_devs=2,  deviate=False)
                            }
                           )
        self._price_matrix = pd.DataFrame(mod)
        return self

    def set_model(self, group_key):
        try:
            grp = self.model.copy()[
                ['step', 'discount_attempt', group_key, 'approved', 'declined', 'revenue']
            ].reset_index(drop=True).groupby(['step', 'discount_attempt', group_key])
            _mod = grp.sum()[['approved', 'declined', 'revenue']]
            _mod['total'] = grp.count()['approved']
            _mod['avg_rev'] = _mod.revenue/_mod.total
            _mod['approval_rate'] = _mod.approved/_mod.total
            _mod[['r_score', 't_score']] = _mod.groupby(level=[0, 1])[['avg_rev', 'total']].rank('max',  ascending=False).astype(int)
            _mod[['ts_mean',  'rs_mean']] = _mod.groupby(level=[0, 1])[['t_score', 'r_score']].mean()
            return _mod
        except Exception  as  e:
            print('set discount  model  failed   in  discounter  attr  set_model', str(e))
            return None


    @staticmethod
    def filter_model(_mod, score_key, number_of_results, min_samp_key='total', min_samp_amt=200):


        return _mod.loc[
            ~((_mod.avg_rev == 0) & (_mod.approval_rate > 0)) & (_mod[score_key] < number_of_results) & (
                        _mod[min_samp_key] > min_samp_amt),
            ['total', 'avg_rev',
             'approval_rate',
             't_score', 'r_score',
             'ts_mean',
             'rs_mean']].reset_index().sort_values(['step', 'discount_attempt', 'avg_rev']).reset_index(
            drop='True').copy()

    def _set_mod_as_pct(self):
        self._join(self._t_set_mod)
        self._price_key = 'pct_bin'
        # Here we have the filterable price models by score
        pct_mod = self.set_model('discount_pct')
        pct_bin = self.set_model('pct_bin')
        # filter the models (settings params may be added to func)
        self.bin_use = self.filter_model(pct_bin, 'r_score', 6,  min_samp_amt=100)
        self.bin_check = self.filter_model(pct_bin, 'r_score', 6, min_samp_amt=25)
        return self

    def _set_mod_as_prc(self):
        self._join(self._t_set_mod)
        # Here we have the filterable price models by score
        self.price_key = 'prc_bin'

        prc_mod = self.set_model('order_total')
        prc_bin = self.set_model(f'prc_bin')
        # filter the models (settings params may be added to func)
        self.bin_use = self.filter_model(prc_bin, 'r_score', 6)
        self.bin_check = self.filter_model(prc_bin, 'r_score', 6, min_samp_amt=0)
        return self

    def best_bin(self, attempt, step, gateway_id=False):
        df = self.bin_use.loc[(self.bin_use.discount_attempt == attempt) &
                                (self.bin_use.step == step)]
        if len(df):
            d = df.loc[df.r_score == df.r_score.min()]
            return float(d.iloc[0][self._price_key])
        else:
            return 0

    def focus_test_price(self, attempt,  step,  gateway_id=False):
        d = self.bin_check.loc[(self.bin_check.discount_attempt == attempt) &
                                (self.bin_check.step == step) &
                                (self.bin_check.r_score == 1)]
        if len(d):
            return float(d[self._price_key])

    @staticmethod
    def find_nearest(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - decimal.Decimal(value))).argmin()
        n = array[idx]
        return n

    def gateway_price(self, price, gateway_id, ignore_flexible=False):
        gty = self._gty.loc[self._gty.gateway_id == gateway_id].iloc[0]
        msk = self._opt_counter.gateway_id == gateway_id
        if not ignore_flexible and gty.is_price_flexible:
            chk = self._opt_counter.loc[msk].iloc[0]
            if chk.flex_assigned < chk.flex_quota:
                self._opt_counter.loc[msk, ['assigned',  'flex_assigned']] += pd.Series([1, 1]).values
                return round(price, 2)
        prc = gty.price
        if len(prc):
            self._opt_counter.loc[msk, ['assigned']] += 1
            return str(round(self.find_nearest(prc, price), 2))
        return np.nan

    def get_price(self, attempt, step, gateway_id, is_test_set, ignore_flexible=False):
        prc = self.max_price
        _get_dm = lambda x:  x.loc[(x.step == step) & (x.attempt == attempt)]
        if is_test_set  or self._price_matrix is None or not len(self._price_matrix):
            disc_model = _get_dm(self._test_matrix)
        else:
            disc_model = _get_dm(self._price_matrix)
            if not len(disc_model):
                disc_model = _get_dm(self._test_matrix)
        if not len(disc_model):
            return np.nan
        prc = round(prc - (prc * disc_model.iloc[0].discounter.get_pct() / 100), 2)
        if prc > self.max_price:
            return str(round(self.max_price,  2))
        if prc < self.min_price:
            return str(round(self.min_price, 2))

        return self.gateway_price(prc, gateway_id, ignore_flexible)

    def _set_opt_counter(self, df, gty_key):
        self._opt_counter = df[[gty_key, 'order_id']].rename({
            'order_id': 'total'}, axis=1
        ).groupby(gty_key).count().reset_index().rename({gty_key: 'gateway_id'}, axis=1)
        self._opt_counter['flex_quota'] = self._opt_counter.total * self.flex_price_pct
        self._opt_counter['flex_assigned'] = 0
        self._opt_counter['assigned'] = 0

    def set_discount_attempt(self,  df):
        grp = self.model[['customer_id', 'step', 'discount_attempt']].reset_index(drop=True).groupby(['customer_id', 'step']).max().reset_index()
        grp.discount_attempt += 1
        df = df.merge(grp, on=['customer_id',  'step'], how='left')
        df.discount_attempt = df.discount_attempt.fillna(0)
        return df

    def _get_opt_count(self, df_len, attempt):
        try:
            return int(df_len*self._opt_pct[attempt])
        except KeyError:
            return int(df_len * self._opt_pct['default'])

    def _get_test_count(self, df_len, attempt):
        try:
            return int(df_len * self._test_pct[attempt])
        except KeyError:
            return int(df_len * self._test_pct['default'])

    def batch_model(self, df, gty_key='destination_gateway'):
        # Just need  to set this now, be  sure to get the discount  attempts.
        d_dis = self.set_discount_attempt(df.copy())
        self._set_opt_counter(d_dis, gty_key)
        nd_dec = pd.DataFrame()
        d_dis.sort_values('discount_attempt', ascending=False,inplace=True)
        for att in d_dis.discount_attempt.unique():
            msk = d_dis.discount_attempt == att
            tot = len(d_dis.loc[msk])
            o_dex = self._get_opt_count(tot, att)
            t_dex = self._get_test_count(tot,  att)
            o_df = d_dis.loc[msk].sample(frac=1).reset_index(drop=True)[:o_dex].copy()
            t_df = d_dis.loc[(msk) & (~d_dis.order_id.isin(o_df.order_id))
                             ].sample(frac=1).reset_index(drop=True)[:t_dex].copy()
            if len(t_df):
                t_df['dynamic_product_price'] = t_df.apply(
                    lambda x: self.get_price(att, x.step, x[gty_key], True), axis=1)
                nd_dec = nd_dec.append(t_df)
            if len(o_df):
                o_df['dynamic_product_price'] = o_df.apply(
                    lambda x: self.get_price(att, x.step, x[gty_key], False), axis=1)
                nd_dec = nd_dec.append(o_df)
        return nd_dec

    @classmethod
    def pct_mod(cls, db, crm_id, max_price=87.99, **attempt_logic):
        return cls(db, crm_id, max_price=max_price, **attempt_logic)._set_mod_as_pct()._set_price_matrix(**attempt_logic)._set_test_matrix(**attempt_logic)

    @classmethod
    def prc_mod(cls, db, crm_id, **attempt_logic):
        return cls(db, crm_id)._set_mod_as_prc()._set_price_matrix(**attempt_logic)._set_test_matrix(**attempt_logic)

    @staticmethod
    def _check_dist(dists):
        if dists:
            if not isinstance(dists, list):
                raise TypeError('dists must be of type list')
            # if len(dists) != len(prices):
            #     raise AttributeError('dists must be of equal length to prices')


    @staticmethod
    def static_prices(_df, prices, msk=None, key='dynamic_product_price', enforce_even=True, drop_index=True, dists=False):
        if not isinstance(prices, list):
            prices = [prices]
        DiscountOptimizer._check_dist(dists)

        df = _df.copy()
        if msk is not None:
            df = df.loc[msk(df)]
        df = df.sample(frac=1)
        inc = math.ceil(len(df)/len(prices))
        count = 0
        sdex = 0
        for p in prices:
            if dists:
                inc = math.ceil(len(df) * dists[count])
            df[sdex:sdex+inc][key] = str(round(float(p), 2))
            sdex += inc
            count += 1
        if msk is not None:
            return _df.loc[~msk(_df)].append(df).reset_index(drop=drop_index)
        return df

    @staticmethod
    def chained_static_prices(_df, prices, msk=None, key='dynamic_product_price', enforce_even=True, drop_index=True, dists=False):
        DiscountOptimizer._check_dist(dists)
        keys = list(prices.keys())
        df = _df.copy()
        if msk is not None:
            df = _df.loc[msk].copy()
        df = df.loc[df.step.astype(int).isin(keys)].sample(frac=1)
        cids = df.customer_id.unique().tolist()
        inc = math.ceil(len(cids)/len(prices[keys[0]]))
        count = 0
        sdex = 0
        p_dex = pd.DataFrame.from_dict(prices,  orient='index').reset_index().rename(columns={'index': 'step'})
        _ddf  = pd.DataFrame()

        for i in range(len(prices[keys[0]])):
            if dists:
                inc = math.ceil(len(cids) * dists[count])
            _nd = df.loc[df.customer_id.isin(cids[sdex:sdex+inc])].copy()
            _nd = _nd.drop(key, errors='ignore',axis=1).merge(
                p_dex[['step', i]].rename({i: key},  axis=1), on='step')
            sdex += inc
            count += 1
            _ddf = _ddf.append(_nd).reset_index(drop=True)
        df = _ddf
        df[key] = df[key].round(2).astype(str)
        return _df.loc[~_df.order_id.isin(df.order_id)].append(df).reset_index(drop=True)


class PriceModel(Db):
    def __init__(self, db, crm_id, group=['internal_product_id',  'cc_type'], rand_pct=.1, ds_rand_mod={},
                 fr_rand_mod={}, max_attempt=7, product_in_key='internal_product_id'):
        Db.__init__(self, db, 'model_data', 'assigned_prices')
        self.set_constraint('assigned_prices_pk', ['crm_id', 'parent_id'])
        self.db = db
        self.model = None
        self.crm_id = crm_id
        self.group = group
        self.ds_rand_mod = ds_rand_mod
        self.fr_rand_mod = fr_rand_mod
        self.rand_pct = rand_pct
        self.max_attempt= max_attempt
        self.product_in_key = product_in_key
        if self.product_in_key and self.product_in_key not in self.group:
            self.group.append(product_in_key)
        self.test_sets = {}

    def set_random_price_array(self):
        return [self.db.engine.execute("""select prices """)]

    def _arr_pos_builder(self, pos, label='gross_net', alias='a.'):
        st_runner = ""
        st = """"""
        for i in range(1, pos + 1):
            if st_runner:
                st_runner += ' + '
            lbl = f"array_position_{i}_{label}"
            st_runner += f"coalesce({alias}{lbl}, '0')"
            st += f" {st_runner} AS {lbl} {',' if i < pos else ''}"

        return st

    def _sub_sel_pos_builder(self, pos):
        st_runner = ""
        st = """"""
        for i in range(1, pos + 1):
            q_raw = f"""
           sum(COALESCE(revenue[{i}], '0'::numeric)) -
           sum(COALESCE(expense[{i}], '0'::numeric))                                        AS array_position_{i}_gross_net,
           sum(model_data.parent_id_pre_segmentation.decline_integer[{i}])                             AS array_position_{i}_approved_count,
           count(1) FILTER (WHERE model_data.parent_id_pre_segmentation.decline_integer[{i}] IS NOT NULL)       AS array_position_{i}_attempt_count,
            """
            st += q_raw
        return st

    def get_price_model(self, max_attempt=7, cap=5000, min_sample=200):
        group = deepcopy(self.group)
        group.append('price_string_forward')
        qry = f"""
                   SELECT a.*, coalesce(nullif(a.cb_count, 0) / nullif( a.array_position_1_approved_count, 0)::numeric,0) cb_pct
                       --({cap} / ( a.cb_count / ( a.array_position_6_approved_count ) )) * a.gross_attempt cap_attempt_thingy
                        FROM ( SELECT a.{',a.'.join(group)},
                                  {self._arr_pos_builder(6, 'gross_net')},
                                  {self._arr_pos_builder(6, 'approved_count')},
                                  {self._arr_pos_builder(6, 'attempt_count')},
                                  total_gross_net,
                                  coalesce(nullif(total_gross_net,0) / nullif(array_position_1_attempt_count,0)::numeric, 0) AS "gross_attempt",
                                  cb_count
                                   FROM (SELECT {','.join(group)},
                                            {self._sub_sel_pos_builder(6)}
                                           sum(total_revenue) -sum(total_expense)    AS total_gross_net,
                                           count(1)                                  AS array_count,
                                           sum(is_cb)                                AS cb_count
                                        FROM model_data.parent_id_pre_segmentation 
                                        WHERE crm_id = '{self.crm_id}' 
                                        GROUP BY  {','.join(group)}) a
                                   ORDER BY coalesce(nullif(total_gross_net, 0)::numeric / nullif(array_position_1_attempt_count, 0)::numeric , 0 ) DESC) AS "a"
                                   WHERE a.array_position_1_attempt_count > '{int(min_sample)}' 

                                   --AND cb_count / ( array_position_6_approved_count + array_position_1_attempt_count ) < '0.05'

                                   ORDER BY gross_attempt DESC;
               """
        # print(qry)
        df = pd.read_sql(qry, self.engine)
        df.columns = df.columns.str.replace('array_position', 'ap')
        #  Add additional data points
        for i in range(max_attempt):
            idx = i + 1
            key = f'ap_{idx}_'
            try:
                df[key + 'attempt_net'] = df[key + 'gross_net'] / df[key + 'attempt_count']
            except KeyError as e:
                print(e)
        self.model = df
        self.model['prices'] = self.model.price_string_forward.str.split(',')
        return self

    def get_chained_model(self, max_attempt=7, cap=5000, min_sample=200):
        group = deepcopy(self.group)
        group.append('price_string_forward')
        qry = f"""
                      SELECT a.*, a.cb_count / ( a.array_position_6_approved_count + array_position_1_attempt_count ) cb_pct
                          --({cap} / ( a.cb_count / ( a.array_position_6_approved_count ) )) * a.gross_attempt cap_attempt_thingy
                           FROM ( SELECT a.{',a.'.join(group)},
                                     {self._arr_pos_builder(6, 'gross_net')},
                                     {self._arr_pos_builder(6, 'approved_count')},
                                     {self._arr_pos_builder(6, 'attempt_count')},                
                                     total_gross_net,
                                     total_gross_net / array_position_1_attempt_count AS "gross_attempt",
                                     cb_count
                                      FROM (SELECT {','.join(group)},
                                               {self._sub_sel_pos_builder(6)}
                                              sum(total_revenue) -sum(total_expense)    AS total_gross_net,
                                              count(1)                                  AS array_count,
                                              sum(is_cb)                                AS cb_count
                                           FROM model_data.parent_id_pre_segmentation 
                                           --WHERE crm_id = '{self.crm_id}' 
                                           GROUP BY  {','.join(group)}) a
                                      ORDER BY total_gross_net / array_position_1_attempt_count DESC ) AS "a"
                                      WHERE a.array_position_6_attempt_count - a.array_position_1_attempt_count > '{int(min_sample)}' 

                                      --AND cb_count / ( array_position_6_approved_count + array_position_1_attempt_count ) < '0.05'

                                      ORDER BY gross_attempt DESC;
                  """
        df = pd.read_sql(qry, self.engine)
        df.columns = df.columns.str.replace('array_position', 'ap')
        #  Add additional data points
        for i in range(max_attempt):
            idx = i + 1
            key = f'ap_{idx}_'
            try:
                df[key + 'attempt_net'] = df[key + 'gross_net'] / df[key + 'attempt_count']
            except KeyError as e:
                print(e)
        self.model = df
        self.model['prices'] = self.model.price_string_forward.str.split(',')
        return self

    def attach_prev_attempts(self, df):
        con = self.engine.raw_connection()
        cur = con.cursor()
        d=None
        exc = None
        try:
            qry=f"""
                create temp table tmp_ords on commit drop as 
                (select unnest(ARRAY{df.crm_id.tolist()}) crm_id, 
                        unnest(ARRAY{df.order_id.tolist()}) order_id
                );
            """
           #print(qry)
            cur.execute(qry)
            qry = f"""
                select b.crm_id, b.order_id, a.price_string 
                from model_data.parent_id_pre_segmentation as a
                inner join tmp_ords b on b.crm_id=a.crm_id and a.parent_id::int= b.order_id::int
            """

            d = pd.read_sql(qry, con)
            con.commit()
        except Exception as e:
            exc = e
            print(e)
            con.rollback()
        finally:
            cur.close()
            con.close()
        if exc:
            raise exc
        if d is not None:
            d = d.merge(df, on=['crm_id', 'order_id'], how='left')
            d = d.rename({'price_string': 'ps_back'}, axis=1)
            d['prices_bk'] = d.ps_back.str.split(',')
            return d

    def get_random(self, df, gateway_id):
        pass

    def get_random_price_string(self):
        pass

    def get_best_price_string(self, **kwargs):
        return str(self.model[((self.model[k] == kwargs[k]) for k in self.group)].sort_values('gross_attempt', ascending=False).iloc[0].price_string_forward)

    def get_attempt_price(self, attempt, opt='rev'):
        key = f'ap_{attempt + 1}_'
        return self.model.sort_values(f'{key}attempt_net', ascending=False).iloc[0].prices[attempt]

    def get_test_settings_from_df(self, product_id, df_tests, test_type, reset=False):
        if product_id not in self.test_sets:
            reset = True
        if reset:
            self.test_sets[product_id] = {}
            _tsts = df_tests.loc[(df_tests.product_id.astype(int) == int(product_id)) & (df_tests.test_type == test_type)]
            if not len(_tsts):
                return None
            top_set = _tsts.iloc[0]
            self.test_sets[product_id][test_type] = dict(
                random_pct=round(float(top_set.random_pct), 2),
                active=top_set.active,
                prices=_tsts.price.astype(float).round(2).tolist(),
                dists=(_tsts.pct/100).round(2).tolist()
            )
        return self.test_sets[product_id][test_type]

    def set_price_test_settings_from_df(self, df_tests, test_type):
        for p in df_tests.product_id.unique():
            self.get_test_settings_from_df(p, df_tests, test_type, reset=True)

    def set_price_tests_by_test_type(self, df, test_type, product_key='destination_product'):
        new_df = pd.DataFrame()
        for p in df[product_key].unique():
            _set = self.test_sets[p][test_type]
            s_df = df.loc[df[product_key].astype(int) == int(p)]
            if len(s_df) and _set is not None:
                s_df = s_df.copy()
                s_df = self.batch_set_price_strings(s_df, **_set)
                new_df = pd.concat([new_df, s_df], ignore_index=True).reset_index(drop=True)
        return new_df

    def set_all_price_tests_df(self, df, df_tests=None, product_key='destination_product'):
        new_df = pd.DataFrame()
        for p in df_tests.product_id.unique():
            _tdf = df.loc[df[product_key].astype(int) == int(p)]

            # GET TEST SETS
            ds_tst_set = self.get_test_settings_from_df(p, df_tests, 'ds_attempt', reset=True)
            ds_pp_tst_set = self.get_test_settings_from_df(p, df_tests, 'ds_prepaid', reset=True)
            nat_tst_set = self.get_test_settings_from_df(p, df_tests, 'natural_attempt', reset=True)

            # DF FILTERS
            is_ds_msk = (~_tdf.retry_date.isna())
            ds_df = _tdf.loc[is_ds_msk].copy()
            nat_df = _tdf.loc[_tdf.retry_date.isna()].copy()
            pp_df = None
            if ds_pp_tst_set is not None and len(ds_tst_set):
                not_pp_msk = (_tdf['class'].isin(['saves', 'provider']))
                pp_df = _tdf.loc[is_ds_msk & (~not_pp_msk)].copy()
                ds_df = _tdf.loc[is_ds_msk & not_pp_msk]

            # SET TESTS
            if pp_df is not None and len(pp_df):
                pp_df = self.batch_set_price_strings(pp_df, **ds_tst_set)
            ds_df = self.batch_set_price_strings(ds_df, **ds_tst_set)
            nat_df = self.batch_set_price_strings(nat_df, **nat_tst_set)
            new_df = pd.concat([new_df, ds_df, nat_df] + ([pp_df] if pp_df is not None else []), ignore_index=True).reset_index(drop=True)
        if len(new_df.loc[new_df.dynamic_product_price.isna()]):
            print('missing prices from test')
        return new_df

    @classmethod
    def attempt_prices_chains(cls, db,
                              crm_id,
                              group=['crm_id', 'internal_product_id', 'cc_type'],
                              rand_pct=.1,
                              max_attempt=7,
                              min_sample=200,
                             ):

        return cls(db,
                   crm_id,
                   group,
                   rand_pct=rand_pct,
                   max_attempt=max_attempt,
                   ).get_price_model(
                    max_attempt=max_attempt,
                    min_sample=min_sample
                  )

    def batch_set_price_strings(self, df, prices, dists, ds_dists=None, msk=None, price_key='dynamic_product_price',  product_out_key='destination_product', random_pct=False, **kw):
        rand_pct = random_pct if random_pct else self.rand_pct
        mod_cols = self.group+['price_string', 'prices', 'gross_attempt']
        df_exi = self.get(['parent_id order_id', 'price_string'], where=f" where crm_id = '{self.crm_id}'")
        exi_oids = df_exi.order_id.unique().tolist()
        if msk is not None:
            _df = df.loc[msk(df)]
        else:
            _df = df
        _df['campaign_class'] = _df['class']
        # if product_out_key != self.product_in_key:
        #     _df = _df.drop('main_product_id', errors='ignore')
        _dfn = _df.copy().loc[(_df.retry_date.isna()) | (~_df.order_id.isin(exi_oids))] #.rename({product_out_key: 'main_product_id'}, axis=1)
        _df = _df.copy().merge(df_exi, on='order_id') #.rename({product_out_key: 'main_product_id'}, axis=1)
        del df_exi
        df_exi = None
        mod = self.model.rename({'price_string_forward': 'price_string'}, axis=1).dropna()
        mod = mod.sort_values('gross_attempt', ascending=False).drop_duplicates(
                             subset=self.group, keep='first')[mod_cols]
        if 'main_product_id' in mod.columns:
            mod.main_product_id = mod.main_product_id.astype(float)
        if 'internal_product_id' in mod.columns:
            mod.internal_product_id = mod.internal_product_id.astype(float)
        if _dfn is not None and len(_dfn):
            _dfn = _dfn.merge(mod, on=self.group, how='left')

            na_msk = _dfn.price_string.isna()
            na_dex = len(_dfn.loc[na_msk])
            new_dex = len(_dfn)
            ran_dex = math.ceil(float(new_dex*rand_pct/100)) - na_dex
            rand_dex = 0 if na_dex < 0 else ran_dex
            df_rand = _dfn.loc[~na_msk].sample(frac=1)[:ran_dex].append(_dfn.loc[na_msk])
            # random_price thing needs to efficiently get random prices based on attempt perhaps iteritively.
            df_rand = self.batch_randomize_price_strings(df_rand, 7, prices, dists, ds_dists, erase=True)
            df_rand.prices = df_rand.price_string.str.split(',')
            df_rand['is_random'] = 1
            _dfn['is_random'] = 0
            _dfn = _dfn.loc[~_dfn.order_id.isin(df_rand.order_id)].append(df_rand).reset_index(drop=True)
            _dfn['p_size'] = _dfn.prices.str.len()

            # here you need to utilize the random price functions again based on the delta between p_size and max attempt
            for p in _dfn.p_size.fillna(0).unique():
                edex = self.max_attempt - p
                if edex < 1:
                    continue
                if edex >= 5:
                    print('>=5')
                _nd = self.batch_randomize_price_strings(_dfn.loc[_dfn.p_size == p], edex, prices, dists, erase=False)
                _dfn = _dfn.loc[~_dfn.order_id.isin(_nd.order_id)].append(_nd)
            _dfn['segmentation'] = ','.join(self.group)
            mod_cols += ['is_random', 'segmentation']
            self.upsert(_dfn.drop(
                'main_product_id', axis=1, errors='ignore').rename(
                columns={'order_id': 'parent_id', product_out_key: 'main_product_id'}
            )[list(set(['crm_id', 'parent_id', 'main_product_id'] + mod_cols))])

        if _df is not None and len(_df):
            if _dfn is not None and len(_dfn):
                _dfn = _dfn.append(_df).drop_duplicates('order_id')
            else:
                _dfn = _df
        _dfn = _dfn.reset_index(drop=True)

        def get_index(_prices, attempt):
            le = len(_prices)
            if not le:
                print('prices are null')
                return prices[random.randint(len(prices))]
            elif le-1 < attempt:
                print('price attempt mismatch', attempt, prices)
                return le-1
            else:
                return _prices[attempt]
        if len(_dfn):
            _dfn['prices'] = _dfn.price_string.str.split(',')
            _dfn[price_key] = _dfn[['prices', 'attempt']].apply(lambda x: get_index(x.prices, int(x.attempt)), axis=1)
            _dfn = _dfn.drop(['p_size', 'price_string', 'prices', 'gross_attempt'], errors='ignore',
                             axis=1)  # .rename({'main_product_id': product_key}, axis=1)
        else:
            print('no dfn len')
        return df.loc[~df.order_id.isin(_dfn.order_id)].append(_dfn).drop_duplicates('order_id').reset_index(drop=True)

    @staticmethod
    def batch_randomize_price_strings(df, edex, prices, dists,  msk=None, price_key='price_string', erase=True):
        _df = df.copy()
        _df['t_price'] = np.nan
        if erase:
            _df[price_key] = ''
        else:
            _df[price_key] = _df[price_key].fillna('')
        for i in range(edex):
            _df.loc[~_df[price_key].replace({'': np.nan}).isna(), price_key] += ','
            _df[price_key] += PriceModel.static_prices(_df, prices, msk=msk, key='t_price', dists=dists).t_price.fillna('').astype(str)
        return _df.drop('t_price', axis=1)

    @staticmethod
    def static_prices(_df, prices,  msk=None, key='dynamic_product_price', enforce_even=True, drop_index=True,
                      dists=False, ds_dists=False):

        if not isinstance(prices, list):
            prices = [prices]
        PriceModel._check_dist(dists)
        PriceModel._check_dist(ds_dists)

        df = _df.copy()
        if msk is not None:
            df = df.loc[msk(df)]
        df = df.sample(frac=1)
        df = df.drop('index', errors='ignore', axis=1).reset_index(drop=False)
        inc = math.ceil(len(df) / len(prices))
        count = 0
        sdex = 0
        # ds_msk = df.retry_date.replace({'': np.nan}).isna()
        # ds_df = df.loc[ds_msk]
        #fr_df =
        for p in prices:
            if dists:
                inc = math.ceil(len(df) * dists[count])
            df.loc[sdex:sdex + inc, key] = str(round(float(p), 2))
            sdex += inc
            count += 1
        if msk is not None:
            return _df.loc[~msk(_df)].append(df).set_index(drop=drop_index)
        return df.set_index('index', drop=drop_index)

    @staticmethod
    def chained_static_prices(_df, prices, msk=None, key='dynamic_product_price', enforce_even=True, drop_index=True,
                              dists=False):
        DiscountOptimizer._check_dist(dists)
        keys = list(prices.keys())
        df = _df.copy()
        if msk is not None:
            df = _df.loc[msk].copy()
        df = df.loc[df.step.astype(int).isin(keys)].sample(frac=1)
        cids = df.customer_id.unique().tolist()
        inc = math.ceil(len(cids) / len(prices[keys[0]]))
        count = 0
        sdex = 0
        p_dex = pd.DataFrame.from_dict(prices, orient='index').reset_index().rename(columns={'index': 'step'})
        _ddf = pd.DataFrame()

        for i in range(len(prices[keys[0]])):
            if dists:
                inc = math.ceil(len(cids) * dists[count])
            _nd = df.loc[df.customer_id.isin(cids[sdex:sdex + inc])].copy()
            _nd = _nd.drop(key, errors='ignore', axis=1).merge(
                p_dex[['step', i]].rename({i: key}, axis=1), on='step')
            sdex += inc
            count += 1
            _ddf = _ddf.append(_nd).reset_index(drop=True)
        df = _ddf
        df[key] = df[key].round(2).astype(str)
        return _df.loc[~_df.order_id.isin(df.order_id)].append(df).reset_index(drop=True)

    @staticmethod
    def _check_dist(dists):
        if dists:
            if not isinstance(dists, list):
                raise TypeError('dists must be of type list')



if __name__ == '__main__':
    from DataFactory import sqlinterface as sqli
    import config
    DB = sqli.Db(connstr=config.conn_select('primary'))
    pm = PriceModel.attempt_prices_chains(DB,'crm_ll_6', min_sample=25)

    print(pm.get_attempt_price(0))