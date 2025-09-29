from models.konn.kk_struc import KKStruc, pd


class Merchants(KKStruc):
    def __init__(self, db, account_id, crm_id):
        KKStruc.__init__(self, db, crm_id, 'merchants')
        self.set_constraint('merchants_pk', ['merchant_id', 'mid_number'])
        self.crm_id = crm_id
        self.account_id = account_id

    def update_merchants(self):
        cols = '"merchant_id"::int,"merchant","merchant_descriptor", "mid_number"'
        df = pd.read_sql(f'''
            SELECT {cols} FROM {self.schema}.transactions
            WHERE "merchant" is not null
            GROUP BY {cols}
            ORDER BY "merchant_id" DESC       
        
        ''', self.engine)
        #self.upsert(df)
        return df

    def update_merchants_from_steps(self):
        cols = 'gateway_id::int as merchant_id, descriptor as merchant, descriptor as merchant_descriptor, mid_number'
        df = pd.read_sql(f'''
            SELECT {cols} FROM ui_{self.account_id}_clients.steps
            WHERE  crm_id = '{self.crm_id}'
          
            ORDER BY "merchant_id" DESC       

        ''', self.engine)
        #self.upsert(df)
        return df
