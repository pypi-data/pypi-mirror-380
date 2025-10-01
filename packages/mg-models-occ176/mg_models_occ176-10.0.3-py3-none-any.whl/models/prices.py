from models.db import Db
import pandas as pd


class PriceTestDefs(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'optimization', 'price_test_defs')
        self.set_constraint('price_test_defs_pk', ['price_test_id', 'crm_id',  'price'])


class PriceList(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'optimization', 'price_list')
        self.set_constraint('price_list_pk', ['price'])


class PriceTestOffers(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'optimization', 'price_test_offers')
        self.set_constraint('price_test_offers_pk', ['crm_id',  'offer_id'])


class PriceTests(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'optimization', 'price_tests')
        self.set_constraint('price_tests_pk', ['price_test_id', 'crm_id'])
        self.crm_id = crm_id

    def get_test(self, price_test_id):
        whr = f"""where price_test_id='{int(price_test_id)}' and crm_id='{self.crm_id}' """
        defs = PriceTestDefs(self.engine).get(['price', 'pct'], where=whr)
        test = self.get(where=whr).iloc[0]
        return dict(
            random_pct=round(float(test.pct)/100, 2),
            active=test.active,
            prices=defs.price.astype(float).round(2).tolist(),
            dists=(defs.pct/100).round(2).tolist()

        )

    def get_all(self, include_inactive=False):
        return pd.read_sql(
            f"""select * from {self.schema}.{self.table} a 
                inner join optimization.price_test_defs b on b.crm_id = a.crm_id and b.price_test_id = a.price_test_id and a.crm_id = '{self.crm_id}'
                {"where a.active" if not include_inactive else ""}
        """, self.engine)
