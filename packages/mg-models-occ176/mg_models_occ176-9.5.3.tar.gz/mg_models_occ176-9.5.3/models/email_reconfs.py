from models.db import Db, pd


class EmailReconfs(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'crm_global', 'email_reconfs')
        self.crm_id = crm_id
