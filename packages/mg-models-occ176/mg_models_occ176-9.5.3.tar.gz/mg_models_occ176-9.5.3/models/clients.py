from models.db import ClientStructure, pd


class Clients(ClientStructure):
    def __init__(self, db,account_id):
        ClientStructure.__init__(self, db, 'clients', account_id)
        self.set_constraint('clients_pk', ['client_id'])

    def get_client_tree(self, crm_id=False, include_proc_info=False, include_step=False, get_excluded_cc_types=False, add_cols=[], add_close_date=False):
        whr = ''
        if crm_id:
            whr = f" where d.crm_id = '{crm_id}'"
        if get_excluded_cc_types:
            add_cols.append('exclude_cc_types')
        use_ac = bool(isinstance(add_cols, list) and len(add_cols))
        add_cols = list(set(add_cols))
        df = pd.read_sql(
            f"""
            SELECT a.client_id::int, b.corp_id::int, c.mid_id::int, d.crm_id, d.gateway_id::int
            {  ',e.'+',e.'.join(add_cols) if use_ac else ''} 
            {',d.step::int' if include_step else ''}
            {',d.close_date' if add_close_date else ''}
            {',c.processor, d.scv_level, d.mcc, d.price' if include_proc_info else ''} 
            from {self.schema}.{self.table} a 
            LEFT JOIN {self.schema}.corps b on b.client_id = a.client_id
            LEFT JOIN {self.schema}.mids c on c.corp_id = b.corp_id
            LEFT JOIN {self.schema}.steps d on d.mid_id = c.mid_id
            {f"LEFT JOIN {self.schema}.gateway_settings e on e.crm_id = d.crm_id and e.gateway_id = d.gateway_id" if use_ac else ""}
            {whr}
            """, self.engine
        )
        df[['client_id', 'corp_id', 'mid_id', 'gateway_id']] = df[['client_id', 'corp_id', 'mid_id', 'gateway_id']].fillna(-1).astype(int)
        return df