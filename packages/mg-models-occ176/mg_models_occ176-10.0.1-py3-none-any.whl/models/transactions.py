from models.db import ClientStructure, pd


class Transactions(ClientStructure):
    def __init__(self, db, account_id):
        ClientStructure.__init__(self, db,  'transactions', account_id)
        self.set_constraint('transactions_pk', ['transaction_id'])
