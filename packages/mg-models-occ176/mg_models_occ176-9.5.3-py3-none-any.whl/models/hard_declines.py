from models.db import Db, pd


class HardDeclines(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'crm_global', 'hard_decline_reasons')
        self.set_constraint('hard_decline_reasons_pk', ['decline_reason'])

    def update(self, crm_id):
        self.upsert(pd.read_sql(
            f"""select distinct(split_part(response_text, 'REFID',1)) as decline_reason 
                from {crm_id}.transactions where response_type = 'HARD_DECLINE'""", self.engine))
        return self


