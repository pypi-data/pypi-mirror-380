from models.db import ClientStructure, Db, pd


class ProcessorStruc(ClientStructure):
    def __init__(self, db, table, acc_id):
        ClientStructure.__init__(self, db, table, acc_id)

    def get_settings(self, crm_id=False):
        if crm_id:
            return self.get(where=f" WHERE crm_id={crm_id}")
        return self.get()

    def set_settings(self, settings, crm_id=False):
        res = self.upsert(settings)
        return res


class Processor(ProcessorStruc):
    def __init__(self, db, acc_id):
        ProcessorStruc.__init__(self, db, 'processor_settings', acc_id)
        self.set_constraint('processor_settings_pk', ['crm_id'])


class TpApis(ProcessorStruc):
    def __init__(self, db, acc_id):
        ProcessorStruc.__init__(self, db, 'tp_integrate', acc_id)


class ProcessingQueue(Db):
    def __init__(self, db, account_id, crm_id):
        Db.__init__(self, db, 'processing', 'recurring_orders')
        self.set_constraint('recurring_orders_pk', ['order_id', 'crm_id', 'last_child'])
        self._account_id = account_id
        self._crm_id = crm_id

    def get_recurring(self):
        cols = list(set(self.columns()) - set(
            ['order_id', 'max_attempt', 'decline_reason', 'last_retry_date', 'step', 'billing_cycle',
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

    def get_declines(self):
        return self.get(where=f""" where crm_id = '{self._crm_id}' and attempt >0""")

    def delete_all(self):
        self.engine.execute(f"""delete from {self.schema}.{self.table} where crm_id ='{self._crm_id}'""")

    def sample_cols(self, as_array=False):
        return self._kw_cols('_sample', as_array=as_array)

    def optimization_cols(self, as_array=False):
        return self._kw_cols('_optimized', as_array=as_array)

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

    def get_due_orders(self, date, include_processed, include_error=False, limit=False, as_query=False):
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
                      and crm_id = '{self._crm_id}'                          
                      ORDER BY step,customer_id
                     {f'LIMIT {limit}' if limit else ''}
        """
        if as_query:
            return qry
        df = pd.read_sql(qry, self.engine)
        if '_kk' in self._crm_id:
            df.shipping_id = df.shipping_id.fillna(0)
        int_cols = ['order_id', 'customer_id', 'destination_product', 'destination_campaign', 'shipping_id',
                    'last_child']
        df[int_cols] = df[int_cols].astype(int)
        return df

    def reset_settings(self):
        gt_set = pd.read_sql(f""" 
            select crm_id, gateway_id::int, enabled, close_date from ui_{self.account_id}_clients.steps a 
            inner join  ui_{self.account_id}_clients.gateway_settings b on b.crm_id= a.crm_id and b.gateway_id=a.gateway_id 
            where a.gateway_id is not null and a.crm_id = '{self._crm_id}'            
        """, self.engine)
        active_gateways = gt_set.loc[(gt_set.enabled) & ((gt_set.close_date.isna()) | (gt_set.close_date==''))].gateway_id.unique().tolist()
        self.engine.execute(f"""UPDATE ui_{self._account_id}_clients.gateway_settings 
                                set active = true 
                                where
                                    crm_id = '{self._crm_id}' 
                                    and processing_status = 0
                                    and destination_gateway::int = any(ARRAY{active_gateways}::int[])""")

        self.engine.execute(f"""UPDATE ui_{self._account_id}_clients.gateway_settings 
                                      set active = false 
                                      where
                                        crm_id = '{self._crm_id}'
                                        and processing_status = 0 
                                        and destination_gateway::int != all(ARRAY{active_gateways}::int[])""")

    def processing_report(self, s_ts, e_ts):
        pass
        # df = pd.read_sql(f"""SELECT approved, declined, processed, recurring_date, retry_date
        #                     FROM {self.schema}.{self.table}
        #                     where processed = 1 and  recurring_date >= '{since}'
        #                     """, self.engine)
