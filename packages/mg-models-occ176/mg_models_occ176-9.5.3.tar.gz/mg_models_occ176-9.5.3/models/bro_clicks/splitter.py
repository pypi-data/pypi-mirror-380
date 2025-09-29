from models.db import Db, pd


class Variates(Db):
    def __init__(self, db):
        Db.__init__(self, db, "bro_clicks", "variates")
        self.set_constraint('variates_pk', ['click_id', 'variate', 'page'])


class VariateOptimization(Db):
    def __init__(self, db):
        Db.__init__(self, db, "bro_clicks", "variates_optimization")
        self.set_constraint('variates_pk', ['click_id', 'variate', 'page'])


class PriceVariates(Db):
    def __init__(self, db):
        Db.__init__(self, db, "bro_clicks", 'price_variates')
        self.set_constraint('price_variates_pk', ['click_id', 'variate', 'page', 'product'])


