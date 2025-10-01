from models.db import ClientStructure, pd

class Iso(ClientStructure):
    def __init__(self, db, account_id):
        ClientStructure.__init__(self, db, 'iso', account_id)
        #self.set_constraint('banks_accounts_pk', ['internal_bank_id'])
