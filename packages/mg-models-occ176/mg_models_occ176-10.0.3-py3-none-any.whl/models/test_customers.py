from models.db import Db, pd, np, Session


class TestCustomers(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'processing', 'test_customers')
        self.set_constraint('test_customers_pk', ['customer_id', 'test_type', 'crm_id'])
        self._crm_id = crm_id

    def add_test(self, customers, test_type):
        if not isinstance(customers, list):
            customers = [customers]
        df = pd.DataFrame([{'customer_id': int(c), 'test_type': test_type,  'crm_id':  self._crm_id} for c in customers])
        self.upsert(df)

    def bin_block_cascade_test(self, customers):
        self.add_test(customers, 'bin_block_cascade')

    def bin_block_no_cascade_test(self, customers):
        self.add_test(customers, 'bin_block_no_cascade')

    def discount_nsf_no_cascade_test(self, customers):
        self.add_test(customers, 'discount_nsf_no_cascade')

    def discount_nsf_cascade_test(self, customers):
        self.add_test(customers, 'discount_nsf_cascade')

    def get_test_set(self, test_type):
        return self.get(where=f" where test_type='{test_type}'")

