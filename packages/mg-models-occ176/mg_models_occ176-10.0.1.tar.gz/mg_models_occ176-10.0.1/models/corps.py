from models.db import ClientStructure, pd


class Corps(ClientStructure):
    def __init__(self, db, account_id='54407332'):
        ClientStructure.__init__(self, db, 'corps', account_id)
        self.set_constraint('corps_pk', ['corp_id'])

    def get_corp_mid_cols_by_mid_id(self, mid_id, columns=['corps.corporation_name', 'mids.processor']):
        try:
            return pd.read_sql(
                f"""select {','.join(columns)} from {self.schema}.{self.table} corps 
                    inner join {self.schema}.mids mids on corps.corp_id = mids.corp_id and mids.mid_id = {int(mid_id)}
                  """,
                self.engine).to_dict(orient='records')[0]
        except:
            return {}

    def get_corp_mid_step_cols_by_gateway(self, gateway_id, crm_id, columns=['corps.corporation_name', 'mids.processor', 'steps.mid_number']):
        try:
            return pd.read_sql(
                f"""select {','.join(columns)} from {self.schema}.{self.table} corps 
                      inner join {self.schema}.mids mids on corps.corp_id = mids.corp_id
                      inner join {self.schema}.steps steps 
                        on steps.mid_id = mids.mid_id and steps.gateway_id = {int(gateway_id)} and steps.crm_id = '{crm_id}'
                    """,
                self.engine).to_dict(orient='records')[0]
        except:
            return {}



