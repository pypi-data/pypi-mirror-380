from models.db import ClientStructure, pd


class Invoices(ClientStructure):
    def __init__(self, db, account_id):
        ClientStructure.__init__(self, db, 'invoices', account_id)
        self.set_constraint('invoices_pk', ['invoice_id'])
