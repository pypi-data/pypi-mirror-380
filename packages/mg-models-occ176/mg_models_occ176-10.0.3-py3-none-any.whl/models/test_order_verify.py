from models.db import Db, pd


class TestOrderVerify(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'support_data', 'test_orders')
        self.set_constraint('test_orders_pk', ['order_id'])


