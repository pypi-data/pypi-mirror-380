from models.db import Db, pd


class Prospects(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'crm_global', 'prospects')
        self.set_constraint('prospects_pk', ['prospect_id', 'crm_id', 'email'])
        self._crm_id = crm_id


class ProspectLog(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'crm_global', 'prospect_submit_log')
        # self.set_constraint('prospects_pk', ['prospect_id', 'crm_id', 'email'])
        self._crm_id = crm_id
