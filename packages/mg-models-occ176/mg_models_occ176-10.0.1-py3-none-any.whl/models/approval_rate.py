from .db import Db, pd


class ApprovalRates(Db):
    def __init__(self, db, gateway_ids=False, billing_cycle_from=0, look_back=30):
        Db.__init__(self, db, 'augmented_data', 'gateway_id_stats')
        self.gateway_ids = gateway_ids
        self.billing_cycle_from = billing_cycle_from
        self.look_back = look_back

    def get(self, whr=''):

        if self.gateway_ids:
            whr = ' WHERE gateway_id in('+','.join([str(g) for g in self.gateway_ids])+') '
        df = pd.read_sql(
            f"""
                SELECT *
                from {self.schema}.{self.table}('{str(self.look_back)} days'::interval, '{self.billing_cycle_from}'::integer)
                {whr}
            """,
            self.engine
        )
        df.columns = df.columns.str.replace('_', '', 1)
        return df

    def _group(self, df):
        df = df[['gateway_id', 'approved_count', 'order_count']].groupby('gateway_id').sum()
        df['approval_rate'] = df['approved_count'] / df['order_count'] * 100
        return df.reset_index()

    def get_general(self):
        return self._group(self.get())

    def get_prepaid(self, processing_type=False):
        df = self.get()
        return self._group(df.loc[(df.prepaid_campaign == 'prepaid')])

    def get_postpaid(self, processing_type=False):
        df = self.get()
        return self._group(df.loc[df.prepaid_campaign == 'provider'])

    def get_salvage(self, campaign_type=False):
        df = self.get()
        return self._group(df.loc[df.processing_type == 'salvage'])

    def get_natural(self, campaign_type=False):
        df = self.get()
        return self._group(df.loc[df.processing_type == 'natural'])




