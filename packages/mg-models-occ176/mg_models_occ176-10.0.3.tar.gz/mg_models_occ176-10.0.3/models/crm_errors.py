from models.db import Db, pd


class CrmErrors(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'processing', 'crm_errors')

    def reset_decrement_reasons(self, max_ts, crm_id, schema='processing', table='recurring_orders'):
        self.engine.execute(f"""UPDATE {schema}.{table} 
                                SET processing_status = 0
                                where
                                    crm_id = '{crm_id}' 
                                    and (p_dec in(select decline_reason from {self.schema}.{self.table} where status =0) or 
                                    decline_reason in(select decline_reason from {self.schema}.{self.table} where status=0 ))
                                    and p_ts <= '{max_ts}'
                                    and processing_status <> 0   
                                """)

    def disable_reasons(self):
        return self.get(['decline_reason'], where="where status = 2").decline_reason.tolist()

    def get_holds(self, crm_id):
        decs = self.get(['decline_reason'], where=" where status = 1").decline_reason.tolist()
        return pd.read_sql(f"""
            SELECT * from processing.recurring_orders 
            where                         
            crm_id = '{crm_id}'
            and ((p_dec is not null and p_dec ILIKE ANY(ARRAY{[f"%%{d.lower().strip()}%%" for d in decs]}) and processing_status=1 and p_ts is not null)) --or 
                --(decline_reason is not null and decline_reason ILIKE ANY(ARRAY{[f"%%{d.lower().strip()}%%" for d in decs]}))
                
                --)
                
        """, self.engine)
