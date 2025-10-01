from models.db import Db, pd, np, Session


class ProcessingQueue(Db):
    def __init__(self, db, account_id, crm_id):
        Db.__init__(self, db, 'processing', 'recurring_orders')
        self.set_constraint('recurring_orders_pk', ['order_id', 'crm_id', 'last_child'])
        self._account_id = account_id
        self._crm_id = crm_id

    def get_recurring(self):
        cols = list(set(self.columns()) - set(['order_id', 'max_attempt', 'decline_reason', 'last_retry_date', 'step','billing_cycle',
                                               'native_order_id', 'crm_id', 'campaign_id', 'extended_date']))
        c_cols = 'c.' + ',c.'.join(cols)
        qry = f""" 
            Select  a.crm_id, a.campaign_id::int, a.customer_id::int, a.time_stamp, a.step, a.order_id::int,
                    a.bc_inferred::int as billing_cycle, b.on_hold as real_hold_status,
                    b.gateway_id::int, b.native_order_id, b.is_recurring::int, 
                    b.extended_date, {c_cols}
            FROM {self.schema}.order_cycles a
            INNER JOIN crm_global.orders b on a.order_id = b.order_id and  a.crm_id = b.crm_id
            LEFT JOIN {self.schema}.{self.table} c on c.order_id = a.order_id and c.crm_id = a.crm_id
            where (b.is_recurring >0 or c.order_id is not null) and a.crm_id = '{self._crm_id}' --and c.order_id is null
            ORDER BY customer_id,order_id
        """
       # print(qry)
        df = pd.read_sql(qry, self.engine)
        df.on_hold = df.on_hold.fillna(0)
        return df

    def reset_settings(self):
        gt_set = pd.read_sql(f""" 
            select a.crm_id, a.gateway_id::int, b.enabled, b.enable_decline_salvage, a.close_date from ui_{self._account_id}_clients.steps a 
            inner join  ui_{self._account_id}_clients.gateway_settings b on b.crm_id = a.crm_id and b.gateway_id=a.gateway_id 
            where a.gateway_id is not null and a.crm_id = '{self._crm_id}'            
        """, self.engine)
        active_gateways = gt_set.loc[(gt_set.enabled) & ((gt_set.close_date.isna()) | (gt_set.close_date == ''))].gateway_id.unique().tolist()
        disable_gateways = gt_set.loc[~((gt_set.enabled) & ((gt_set.close_date.isna()) | (gt_set.close_date == '')))].gateway_id.unique().tolist()
        dec_disable_gateways = gt_set.loc[~gt_set.enable_decline_salvage.astype(bool)].gateway_id.unique().tolist()
        self.engine.execute(f"""UPDATE {self.schema}.{self.table} 
                                set active = true 
                                where
                                    crm_id = '{self._crm_id}' 
                                    and processing_status = 0
                                    and destination_gateway::int = any(ARRAY{active_gateways}::int[])""")

        if disable_gateways is not None and len(disable_gateways):
            self.engine.execute(f"""UPDATE {self.schema}.{self.table} 
                                      set active = false 
                                      where
                                        crm_id = '{self._crm_id}'
                                        and processing_status = 0 
                                        and destination_gateway::int = any(ARRAY{disable_gateways}::int[])""")

        if dec_disable_gateways is not None and len(dec_disable_gateways):
            self.engine.execute(f"""UPDATE {self.schema}.{self.table} 
                                              set active = false 
                                              where
                                                crm_id = '{self._crm_id}'
                                                and processing_status = 0 
                                                and retry_attempt_count is not null
                                                and destination_gateway::int = any(ARRAY{dec_disable_gateways}::int[])""")

    def get_declines(self):
        return self.get(where=f""" where crm_id = '{self._crm_id}' and attempt >0""")

    def delete_non_recurring(self, disabled_campaigns=[]):
        self.engine.execute(
            f"""Delete from {self.schema}.{self.table} as a 
                            USING  crm_global.orders b
                              where a.order_id = b.order_id 
                                   and a.crm_id = b.crm_id 
                                    and a.crm_id= '{self._crm_id}' 
                                    and (b.is_recurring =0 {f"or b.campaign_id = any(ARRAY{disabled_campaigns})" if len(disabled_campaigns) else ""})
                                                      
                                                         
                               """)
        return self

    def delete_customers(self, customer_ids):
        self.engine.execute(f"""delete from processing.recurring_orders where crm_id='{self._crm_id}' 
                                and customer_id = ANY(ARRAY{customer_ids})""")

    def delete_all(self):
        self.engine.execute(f"""delete from {self.schema}.{self.table} where crm_id ='{self._crm_id}'""")

    def sample_cols(self, as_array=False):
        return self._kw_cols('_sample', as_array=as_array)

    def optimization_cols(self, as_array=False):
        return self._kw_cols('_optimized', as_array=as_array)

    def _ml_cols(self, col_wild_card):
        if col_wild_card == '_both':
            columns = self.sample_cols()+','+self.optimization_cols()
        else:
            columns = self._kw_cols(col_wild_card)
        df = pd.read_sql(f"""
                        select b.customer_id::int, a.order_id, d.time_stamp::timestamp,
                        d.extended_date, a.campaign_id, a.crm_id, a.parent_client, a.parent_corp, 
                        a.parent_mid, a.parent_gateway, a.destination_gateway,a.decline_reason,a.on_hold,a.hold_reason,
                        d.billing_state as state, d.cc_type, d.order_total,
                        b.bc_inferred::int as billing_cycle, b.step, a.group_key,
                        b.first_affiliate as affid, a.attempt::int, 
                        c.provider, c.offer_id, a.last_retry_date,
                        {columns}
                        from {self.schema}.{self.table} a
                        inner join {self.schema}.order_cycles b 
                            on b.crm_id = a.crm_id and b.order_id = a.order_id
                        inner join {self.schema}.order_cycles anc on anc.order_id = b.ancestor_id and anc.crm_id = b.crm_id                         
                        left join ui_{self._account_id}_offers.campaigns c 
                            on c.crm_id = a.crm_id and c.campaign_id = anc.campaign_id       
                        left join crm_global.orders d on a.crm_id = d.crm_id and a.order_id = d.order_id             
                       where a.crm_id = '{self._crm_id}'
                    """, self.engine)
        df.provider = df.provider.fillna('unk')
        df.offer_id = df.offer_id.fillna(-1).astype(int)
        df.affid = df.affid.fillna('unk').astype(str)
        df.customer_id = df.customer_id.astype(int)
        df.on_hold = df.on_hold.fillna(0).astype(int)
        #df.decline_reason = df.decline_reason.replace({0: np.nan})
        return df

    def _ml_cols_2(self, col_wild_card):
        if col_wild_card == '_both':
            columns = self.sample_cols()+','+self.optimization_cols()

        else:
            columns = self._kw_cols(col_wild_card)
        df = pd.read_sql(f"""
                        select b.customer_id::int, a.order_id, d.time_stamp::timestamp,
                        d.extended_date, a.campaign_id, a.crm_id, a.parent_client, a.parent_corp, a.parent_mid, a.parent_gateway, a.destination_gateway, 
                        d.state, d.cc_type, d.order_total,
                        b.bc_inferred::int as billing_cycle, a.step, a.group_key,
                        b.first_affiliate as affid, a.attempt
                        c.provider, c.offer_id, a.last_retry_date,
                        {columns}
                        from {self.schema}.{self.table} a
                        inner join {self.schema}.order_cycles b 
                            on b.crm_id = a.crm_id and b.order_id = a.order_id
                        inner join {self.schema}.order_cycles anc on anc.order_id = b.ancestor_id and anc.crm_id = b.crm_id                         
                        left join ui_{self._account_id}_offers.campaigns c 
                            on c.crm_id = a.crm_id and c.campaign_id = anc.campaign_id       
                        left join crm_global.orders d on a.crm_id = d.crm_id and a.order_id = d.order_id             
                       where a.crm_id = '{self._crm_id}'
                    """, self.engine)
        df.provider = df.provider.fillna('unk')
        df.offer_id = df.offer_id.fillna(-1).astype(int)
        df.affid = df.affid.fillna('unk').astype(str)
        df.customer_id = df.customer_id.astype(int)
        df.decline_reason = df.decline_reason.replace({0: np.nan})
        return df

    def ml_sample_model(self):
        return self._ml_cols('_sample')

    def ml_optimize_model(self):
        return self._ml_cols('_is_optimized')

    def ml_model(self):
        return self._ml_cols('_both')

    def get_holds(self):
        return self.get(where=f" where (hold_reason is not null or on_hold >0) and crm_id='{self._crm_id}' ")

    def get_cascades(self):
        return self.get(['native_order_id', 'step', 'parent_gateway', 'destination_gateway'],
                        where=f"where destination_gateway <> parent_gateway and on_hold <> 1")

    def get_due_orders(self, date, include_processed, include_error=False, limit=False):
        qry = f"""
                SELECT * from {self.schema}.{self.table}
                where (retry_date <= '{date}'::date and ((retry_date >= recurring_date + INTERVAL '3 days') or ('{date}'::date >= recurring_date + INTERVAL '3 days')) or 
                      (retry_date is null and recurring_date <= '{date}'::date))
                      and ((processing_status =0
                              and attempt < 6
                              and is_manual_cascade = 0
                             and destination_gateway <> 0)
                            {f"or (processing_status  in ('1','2') and p_ts::date >= '{date}'::date )" if include_processed else ""} 
                            {f"or (processing_status = '3' and p_ts::date >= '{date}'::date)" if include_error else ""}             
                           )
                      and active
                      and crm_id = '{self._crm_id}'                          
                      ORDER BY step,customer_id
                     {f'LIMIT {limit}' if limit else ''}
        """
        #print(qry)
        df = pd.read_sql(qry, self.engine)
        if '_kk' in self._crm_id:
            df.shipping_id = df.shipping_id.fillna(0)
        int_cols = ['order_id', 'customer_id', 'destination_product', 'destination_campaign', 'shipping_id', 'last_child']
        df[int_cols] = df[int_cols].astype(int)
        return df

    def deactivate(self, gateway_id):
        if not isinstance(gateway_id, list):
            gateway_id = [gateway_id]
        gateway_id = [int(g) for g in gateway_id]
        self.engine.execute(f"""update {self.schema}.{self.table} set active=false 
        where crm_id = '{self._crm_id}' 
        and destination_gateway = any(Array{gateway_id})  and  processing_status=0 and is_dead_mid_cascade=0""")
        return self

    def deactivate_orders(self, oids):
        if not isinstance(oids, list):
            oids = [oids]
        self.engine.execute(f"""update {self.schema}.{self.table} set active=False where crm_id = '{self._crm_id}' and order_id = any(ARRAY{oids}::numeric[]) and processing_status=0""", self.engine)

    def processing_report(self, s_ts, e_ts):
        pass
        # df = pd.read_sql(f"""SELECT approved, declined, processed, recurring_date, retry_date
        #                     FROM {self.schema}.{self.table}
        #                     where processed = 1 and  recurring_date >= '{since}'
        #                     """, self.engine)

    def reset_expirations(self):
        self.engine.execute(f""" UPDATE processing.recurring_orders   SET  p_dec=null, p_ts=null, processing_status=0, p_gateway=null, p_native=null, 
                                p_attempt =  (case when p_attempt is null then 0 else p_attempt end),  p_child  = null
                                where crm_id = '{self._crm_id}' and p_dec  ilike '%%Expired%%'
                """, self.engine)

    def get_processing_status(self, oids):
        if not isinstance(oids, list):
            oids = [oids]
        return self.get(['order_id::int', 'processing_status'],
                        where=f"""where crm_id='{self._crm_id}' 
                                  and order_id = Any(ARRAY{oids}::numeric[])""")


class ActionsLog(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'processing', 'processing_actions')
        self.set_constraint('processing_actions_pk', ['id_key'])
        self._crm_id = crm_id

    def sample_cols(self, as_array=False, join_val='a'):
        return self._kw_cols('_sample', as_array=as_array, join_val=join_val)

    def optimization_cols(self, as_array=False,join_val='a'):
        return self._kw_cols('_optimized', as_array=as_array, join_val=join_val)

    def get_latest(self):
        return pd.read_sql(
            f"""
                SELECT order_id,last_child,status,send_status, {self._sample_cols(join_val='b')},{self._optimze_cols(join_val='b')} 
                FROM 
                 (SELECT crm_id, order_id, last_child, max(id_key) 
                    from {self.schema}.{self.table} 
                    GROUP BY crm_id, order_id, last_child, id_key
                  ) a
                 left join {self.schema}.{self.table} b on b.id_key = a.id_key
                
            
            """, self.engine
        )

    def get_optimized(self):
        cols = self.optimization_cols(as_array=True)
        sel_c = ','.join([f"max({c}) {c}" for c in cols])
        hav_c = 'OR'.join([f" max({c}) > 0 " for c in cols])
        return pd.read_sql(f"""
            SELECT crm_id,order_id,last_child,send_status, {sel_c}
              from processing.processing_actions
              where crm_id = '{self._crm_id}' and close_date is null 
              GROUP BY crm_id, order_id, last_child, send_status,id_key
              HAVING ({hav_c}) and max(id_key) = id_key
              ORDER BY order_id;
        """, self.engine)

    def get_by_after_retry_date(self, retry_date, null_extended=True):
        return pd.read_sql(
            f"""SELECT * FROM {self.schema}.{self.table}
                  where send_status = 'REACTIVATE_SUCCESS'
                        {'and extended_date is null' if null_extended else ''}
                  GROUP BY order_id     
                  HAVING max(retry_date) > '{retry_date}'::date
                  ORDER BY id_key asc         
            """, self.engine).drop_duplicates(subset=['order_id', 'last_child'], keep='last')

    def optimization_report(self):
        return pd.read_sql(f"""selec""", self.engine)

    def sample_report(self):
        return pd.read_sql(f"""""", self.engine)


class DSCycler(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'processing', 'ds_cycler')
        # self.set_constraint('decline_reactivate_pk', [])
        self._crm_id = crm_id



