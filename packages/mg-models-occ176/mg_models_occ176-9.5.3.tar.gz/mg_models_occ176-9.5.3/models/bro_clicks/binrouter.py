from models.db import Db, pd


class BlackList(Db):
    def __init__(self, db):
        Db.__init__(self, db, f"ui_54407332_bins", 'bin_blacklist')
        #self.set_constraint('clicks_pk)

    def is_blocked(self,  bin):
        try:
            res = self.engine.execute(f"""Select count(*) from {self.schema}.{self.table} 
                                           where bin = '{str(bin)}' and enabled""").scalar()
            return 2 if res else 0

        except:
            return 0

    def get_bin(self, crm_id, bin, columns=False):
        cols = ','.join(columns) if isinstance(columns, list) and len(columns) else '*'
        try:
            return dict(self.engine.execute(f"""select {cols} from {self.schema}.{self.table} where crm_id='{crm_id}' and bin = '{bin}'""").fetchone())
        except Exception as e:
            return None

    def is_blocked_and_processor_exclusions(self, crm_id, bin):
        res = self.get_bin(crm_id, bin, ['enabled', 'enable_shave', 'excluded_processors'])
        if not res:
            return 0, 0, []
        block = 2 if res['enabled'] else 0
        shave = 2 if res['enable_shave'] else 0
        return block, shave, res['excluded_processors']

    def processor_exclusions(self, crm_id, bin):
        res = self.get_bin(crm_id, bin, ['excluded_processors'])
        if not res:
            return []
        return res['processor_exclusions']


class BinRouter(Db):
    def __init__(self, db):
        Db.__init__(self, db, f"ui_54407332_bins", 'bin_router')


