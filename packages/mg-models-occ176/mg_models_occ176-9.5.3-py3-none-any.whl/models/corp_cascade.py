from models.db import ClientStructure, pd
from threading import Thread


class CorpCascade(ClientStructure):
    def __init__(self, db, account_id, granularity=4,
                 return_type='filtered', crm_id=False, cascade_all=False, exclusions=[], naturals='declines'):
        ClientStructure.__init__(self, db, 'clients', account_id)
        #self.set_constraint('cascade_log_pk', ['order_id', 'insert_date'])
        self._crm_id = crm_id
        self._naturals = naturals
        self._df_pr = None
        self._df_cm = None
        self._cm_raw = None
        self._gran = granularity
        self._exclusions = exclusions
        self.return_type = return_type
        self._result = None
        self._account_id = account_id
        self._cascade_all = cascade_all
        self._t1 = None
        self._t1 = Thread(target=self.get_processor_relationships)
        self._t2 = Thread(target=self.get_cascade_model)
        self._t2.start()
        self._t1.start()
        self.configure(granularity, cascade_all, exclusions, naturals, defer=True)

    @staticmethod
    def _joiner(t):
        try:
            t.join()
        except:
            pass

    def __del__(self):
        self._joiner(self._t1)
        self._joiner(self._t2)

    def _set_exclusions(self, exclusions):
        if isinstance(exclusions, (dict, list)):
            if isinstance(exclusions, list):
                if len(exclusions) and not isinstance(exclusions[0], dict):
                    raise AttributeError(f'list of exclusions must contain dicts. Got {str(type(exclusions[0]))}')
            else:
                exclusions = [exclusions]
            self._exclusions = exclusions
            return True
        elif exclusions is not None:
            raise TypeError(f'exclusions must be of type list, dict. Got {str(type(exclusions))}')
        return False

    def _set_gran(self, gran):
        if isinstance(gran, (int, float)):
            self._granularity = 1 if int(gran) < 1 else int(gran)
            return True
        return False

    def _set_nat(self, naturals):
        if isinstance(naturals, str):
            opt = ['declines', 'naturals', 'both']
            if naturals not in opt:
                raise AttributeError(f"naturals must specify one of {','.join(opt)}. Got {naturals}")
            self._naturals = naturals
            return True
        elif naturals is not None:
            raise TypeError(f'naturals must be of type str. Got {str(type(naturals))}')
        return False

    def configure(self, gran=False, cascade_all=None, exclusions=None, naturals=None, defer=False):
        if isinstance(cascade_all, bool):
            self._cascade_all = cascade_all

        conf = False
        conf = self._set_nat(naturals) or conf
        conf = self._set_exclusions(exclusions) or conf
        conf = self._set_gran(gran) or conf

        if self._t2 and conf and not defer:
            self._joiner(self._t2)
            self._configure_cas_mod()
        return self

    def get_current_processor(self, df, as_='parent_processor'):
        return df.merge(pd.read_sql(f"""Select crm_id, gateway_id::int as parent_gateway, b.processor as {as_} from {self.schema}.steps a
                                        inner join {self.schema}.mids b on b.mid_id = a.mid_id   
                                        """, self.engine,),
                        on=['crm_id', 'parent_gateway'],
                        how='inner')

    def get_processor_relationships(self):
        self._df_pr = pd.read_sql(f"""
            SELECT c.crm_id, a.client_id, b.corp_id::int,b.mid_id::int, b.processor,
            c.minimum_price, c.step::smallint as c_step, c.gateway_id::int, c.close_date,
            d.enabled 
            from {self.schema}.corps as a
            LEFT JOIN {self.schema}.mids as b on b.corp_id = a.corp_id
            LEFT JOIN {self.schema}.steps as c on c.mid_id = b.mid_id
            LEFT JOIN {self.schema}.gateway_settings d on d.gateway_id = c.gateway_id and d.crm_id = c.crm_id 
            WHERE c.gateway_id is not null 
            --and c.close_date is null
            {f" AND c.crm_id = '{self._crm_id}' " if self._crm_id else ''}             
            ORDER BY corp_id,step,mid_id,gateway_id
        """, self.engine)
        # remove duplicated gateways where they are on 2 different mids
        grp = pd.DataFrame(self._df_pr[['gateway_id', 'mid_id']].groupby('gateway_id').mid_id.count())
        self._df_pr = self._df_pr.loc[self._df_pr.gateway_id.isin(grp.loc[grp.mid_id < 2].index)]
        return self._df_pr

    def get_cascade_model(self):

        self._cm_raw = pd.read_sql(
            f"""
               SELECT _originating_state as state, 
                _originating_processor as c_proc, 
                _cc_type as cc_type, 
                _originating_count::int as o_count, 
                _originating_conversion::numeric * 100 as o_conv, 
                _destination_processor as d_proc, 
                _destination_count::int as d_count,
                _destination_conversion::numeric * 100 as d_conv,
                _is_natural as is_natural 
                FROM  -- processing.processor_stats_table_cross 
                processing.processor_stats_cross() 
                --processing.processor_stats_cross_max() 
                --processing.processor_stats_table_cross_test --
            
               """, self.engine)
        self._configure_cas_mod()

    def _configure_cas_mod(self):
        gran = self._gran
        df = self._cm_raw

        # exclude routes
        for filt in self._exclusions:
            qry = ' & '.join([f"{k}.str.contains('{v}', na=False, case=False)" for k, v in filt.items()])
            msk = df.eval(qry)
            df = df.loc[~msk]

        df = df.merge(
            df[['state', 'cc_type', 'is_natural', 'd_conv', 'd_count']].rename({
                'd_conv': 'max_conv',
                'd_count': 'max_count',

            }, axis=1).groupby(['state', 'cc_type', 'is_natural']).max().reset_index(),
            on=['cc_type', 'state', 'is_natural']
        )
        df = df.loc[df.max_conv == df.d_conv]
        #df = df.loc[df.d_count == df.max_count]
        df.drop(['max_count', 'max_conv'], axis=1, inplace=True)
        if self._naturals != 'both':
            df = df.loc[(~df.is_natural if self._naturals == 'declines' else df.is_natural)]
        df['conv_dif'] = df.d_conv - df.o_conv
        df = df.set_index(['cc_type', 'c_proc', 'd_proc', 'is_natural', 'conv_dif'], drop=False).sort_index(
            ascending=False).droplevel(3)
        _grp = lambda x: x.groupby(level=[0, 1, 2, 3])
        _grp2 = lambda x: x.groupby(level=[0, 1, 2, 3, 4])
        df['o_rank'] = _grp(df).state.cumcount() + 1
        df['max_rank'] = _grp(df).o_rank.max()
        df['bucket'] = int()
        for i in range(gran):
            g = gran - i
            df.loc[(df.o_rank / df.max_rank <= g / gran), 'bucket'] = g
        df = df.set_index(['cc_type', 'c_proc', 'd_proc', 'is_natural', 'bucket'], drop=False).sort_index(ascending=True)
        d_cols = ['o_count', 'd_count', 'o_conv', 'd_conv']
        df[d_cols] = _grp2(df)[d_cols].sum()
        df['b_size'] = _grp2(df).bucket.count()
        df.o_conv = df.o_conv / df['b_size']
        df.d_conv = df.d_conv / df['b_size']
        self._df_cm = df.drop(['conv_dif', 'o_rank', 'max_rank', 'bucket', 'b_size'], axis=1).reset_index(drop=True)

    def set(self, df, return_type=False, join_level=['client_id', 'crm_id'], sources=False, destination_reset=False):
        # helpers
        LEN = len(df.order_id.unique())
        if not return_type:
            return_type = self.return_type

        _gwy_grp = lambda x, y, z: pd.DataFrame(
            x[['gateway_id', 'order_id']].rename({'order_id': y}, axis=1).groupby('gateway_id', as_index=False).agg(z))

        # Start the sql calls t2 will take longer so t1 model can be prepared while it waits.
        self._joiner(self._t1)

        # Copy the initial data frame with it's gateway count
        n_df = df.drop('is_manual_cascade', errors='ignore', axis=1).copy().rename(columns={'parent_gateway': 'gateway_id'})
        if 'client_id' not in n_df.columns:
           # print(df.columns)
            n_df = n_df.rename({'parent_client': 'client_id'}, axis=1)
        LEN = len(n_df.order_id.unique())
        if not destination_reset:
            n_df = n_df.loc[n_df.destination_gateway == n_df.gateway_id]
        LEN = len(n_df.order_id.unique())
        n_df = n_df.merge(_gwy_grp(n_df, 'gt_count', 'count'), on='gateway_id')
        n_df.order_id = n_df.order_id.astype(int)

        # Join the appropriate corp sql models using t1 result.
        n_df = pd.merge(
            n_df,
            self._df_pr.drop(['enabled', 'close_date'], axis=1).rename(columns={'processor': 'c_proc'}),
            on=join_level+['gateway_id'])
        LEN = len(n_df.order_id.unique())
      #  tgy = ~df.loc[df.gateway_id.isin(n_df.gateway_id.unique())]
        n_df = pd.merge(n_df, self._df_pr.loc[
            ((self._df_pr.close_date.isna()) | (self._df_pr.close_date == ''))
            & (self._df_pr.enabled)
            ].drop(['enabled', 'close_date'], axis=1).rename(
            columns={'processor': 'n_proc', 'c_step': 'step', 'gateway_id': 'n_gateway', 'corp_id': 'n_corp'}),
            on=join_level+['step'],
            how='inner'

        )[['crm_id', 'campaign_id', 'state', 'order_id', 'client_id', 'corp_id', 'n_corp', 'step', 'c_step',
              'order_total', 'gateway_id', 'n_gateway',  'c_proc',
             'n_proc',  'cc_type', 'gt_count', 'min_ds_margin', 'destination_gateway']].sort_values(by='order_id')

        # Join T2 result to T1/Orders model.
        self._joiner(self._t2)
        LEN = len(n_df.order_id.unique())
        rev_df = n_df.copy()
        n_df = pd.merge(n_df, self._df_cm, on=['state', 'c_proc', 'cc_type'], how='left')
        LEN = len(n_df.order_id.unique())
        # filter the model

        def final_filt(_df):
            return _df.loc[(~_df.d_proc.isna()) &
                        (~_df.client_id.isna()) &
                        (_df.d_proc == _df.n_proc) &
                        (_df.gateway_id != _df.n_gateway) &
                        ((self._cascade_all) |
                         ((_df.d_count >= 200) &
                         (_df.d_conv - _df.o_conv > 0.005)))
                        ]
        n_df = final_filt(n_df)
        n_df['is_manual_cascade'] = 0

        def fix_missing(key=['c_proc', 'cc_type']):
            nonlocal final_filt
            nonlocal n_df
            if self._cascade_all:
                fix_no_state = rev_df.loc[~rev_df.order_id.isin(n_df.order_id.unique())].sort_values(by='order_id')
                n_keys = ['c_proc', 'cc_type', 'state']

                if not len(fix_no_state):
                    return
                drp = list(set(n_keys) - set(key))
                fix_no_state = fix_no_state.merge(self._df_cm.drop(drp, axis=1), on=key).sort_values(
                    by=['order_id', 'c_proc', 'state'])
                fix_no_state = final_filt(fix_no_state)
                fix_no_state = fix_no_state.drop_duplicates(subset=['order_id', 'n_gateway'])
                if len(fix_no_state):
                    fix_no_state['is_manual_cascade'] = 0
                    n_df = n_df.append(fix_no_state)
                mis_route_ids = rev_df.loc[~rev_df.order_id.isin(n_df.order_id.unique())].order_id.unique().tolist()
                if len(key) == 1:
                    if len(mis_route_ids):
                        manual_alerts = rev_df.loc[~rev_df.order_id.isin(n_df.order_id.unique())].drop_duplicates(subset='order_id')
                        manual_alerts['is_manual_cascade'] = 1
                        manual_alerts['n_gateway'] = 0
                        n_df = n_df.append(manual_alerts)
                        test = n_df.loc[n_df.is_manual_cascade ==1 ]
                    return
                else:
                    return fix_missing(['c_proc'])

        fix_missing()
        if not len(n_df):
            return None

        # Dupe Handler
        _dupe_mask = lambda x: (x.order_id.isin(x.loc[x.order_id.duplicated(), 'order_id']))
        dupe_mask = _dupe_mask(n_df)
        LEN = len(n_df.order_id.unique())
        # first filter duplicate dest
        n_df = n_df.loc[~dupe_mask].append(
            n_df.loc[dupe_mask].sort_values('order_id').drop_duplicates(subset=['crm_id', 'order_id', 'client_id', 'n_corp', 'n_gateway']))
        dupe_mask = _dupe_mask(n_df)

        # Load Balance
        ordex = n_df[['n_gateway']].drop_duplicates()
        ordex['count'] = 0
        n_df['use'] = False

        # Filter B4 load balance if processor sources specified
        if isinstance(sources, dict):
            qry = ' & '.join([f"{k}.str.lower().str.contains('{v.lower()}')" for k, v in sources.items()])
            msk = n_df.eval(qry)
            n_df = n_df.loc[msk]

        # Execute Load Balance
        for o in n_df.order_id.unique():
            msk = n_df.order_id == o
            if n_df.loc[msk].iloc[0].n_gateway == 0:
                n_df.loc[msk, ['use']] = True
                continue
            dex = ordex.loc[ordex.n_gateway.isin(n_df.loc[msk].n_gateway)]
            gty = dex.sort_values('count').iloc[0].n_gateway
            ordex.loc[ordex.n_gateway == gty, ['count']] += 1
            n_df.loc[(msk) & (n_df.n_gateway == gty), ['use']] = True

        n_df = n_df.loc[n_df.use]
        n_df = n_df.sample(frac=1).drop_duplicates(subset='order_id')

        df = pd.merge(df.drop('is_manual_cascade', errors='ignore', axis=1), n_df[['order_id', 'n_gateway', 'c_proc', 'd_proc', 'is_manual_cascade']], on='order_id', how='left')
        cas_mask = (~df.n_gateway.isna())

        df.loc[cas_mask, 'destination_gateway'] = df.loc[cas_mask, 'n_gateway'].astype(int)
        df.loc[cas_mask, 'parent_processor'] = df.loc[cas_mask, 'c_proc']
        df.loc[cas_mask, 'destination_processor'] = df.loc[cas_mask, 'd_proc']
        self._result = n_df

        if return_type == 'filtered':
            return df.loc[cas_mask].drop(['n_gateway', 'd_proc', 'c_proc'], axis=1)
        if self._cascade_all:
            df.loc[~cas_mask, ['destination_gateway', 'is_manual_cascade']] = pd.Series([0, 1]).values
        return df.drop(['n_gateway', 'd_proc', 'c_proc'], axis=1)

