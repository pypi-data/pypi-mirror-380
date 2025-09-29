from models.db import ClientStructure, pd


class Banks(ClientStructure):
    def __init__(self, db, account_id='54407332'):
        ClientStructure.__init__(self, db, 'bank_accounts', account_id)
        self.set_constraint('banks_accounts_pk', ['internal_bank_id'])
