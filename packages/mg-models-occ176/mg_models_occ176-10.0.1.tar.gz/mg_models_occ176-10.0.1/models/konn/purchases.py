from models.konn.kk_struc import KKStruc
import pandas as pd


class Purchases(KKStruc):
    def __init__(self, db, crm_id):
        KKStruc.__init__(self, db, crm_id, 'purchases')
        self.set_constraint('purchases_pk', ['purchase_id'])

    def format_data(self, df, format_col_names=True):
        tran2 = pd.DataFrame(df.transactions.explode().tolist())
        #tran2 = tran2.drop_duplicates(subset='transactionId', keep='first').reset_index(drop=True)
        df = df.join(tran2[['transactionId']])
        df.transactionId = df.transactionId.astype(int)
        df = self.format_ts_offset(df)
        if format_col_names:
            df = self.format_col_names(df)
        return df

    @staticmethod
    def format_by_first_transaction(df):
        tran = df['transactions'].tolist()
        tran2 = pd.DataFrame(df.transactions.explode().tolist())
        tran2 = tran2.drop_duplicates(subset='transactionId', keep='first').reset_index(drop=True)
        df = df.join(tran2[['transactionId']])
        df.transactionId = df.transactionId.astype(int)
        return df[['purchaseId', 'transactionId', 'orderId']]

