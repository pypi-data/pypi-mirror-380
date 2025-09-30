from models.db import Db, pd


class RbSet(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'processing', 'rb_set')
        self.set_constraint('rb_set_pk', ['crm_id'])

    def get_crm(self, crm_id):
        return self.get(where=f" where crm_id='{crm_id}'")
