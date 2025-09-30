import pandas as pd

from models.db import Db


class OrderActionsQueue(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'processing', 'order_actions_queue')
        self.set_constraint('order_actions_queue_pk', ['id'])

    def get_new(self, crm_id, order_actions):
        return self.get(where=f"""where status = '0' and crm_id='{crm_id}' and order_action = any(ARRAY{order_actions})""")

    @staticmethod
    def _action_formatter(df, action, crm_id, user):
        _df = df.copy()
        if 'crm_id' not in _df.columns:
            if crm_id is None:
                raise AttributeError('crm_id must be passed either via the data frame or function call')
            _df['crm_id'] = crm_id
        if 'order_id' not in _df.columns:
            raise AttributeError('order_id must be present in Dataframe columns')
        _df['user'] = user
        _df['order_action'] = action
        return _df

    def _date_putter(self, df, column, crm_id=None, user='internal', **kw):
        action = f'set_{column}'
        if column not in df.columns:
            raise AttributeError('DataFrame must contain recurring_date column')
        _df = self._action_formatter(df, action, crm_id, user)
        _df[column] = pd.to_datetime(_df[column])
        _df.dropna(subset=column, inplace=True)
        return self.upsert(_df)

    def _put_stop_recurring(self, df, action, crm_id, user):
        _df = self._action_formatter(df, action, crm_id, user)
        _df['is_recurring'] = 0
        return self.upsert(df)

    def put_cancel(self, df, crm_id=None, user='internal', **kw):
        return self._put_stop_recurring(df, 'cancel', crm_id, user)

    def put_pause(self, df, crm_id=None, user='internal', **kw):
        return self._put_stop_recurring(df, 'pause', crm_id, user)

    def put_blacklist(self, df, crm_id=None, user='internal', **kw):
        return self._put_stop_recurring(df, 'blacklist', crm_id, user)

    def put_ds_pause(self, df, crm_id=None, user='internal', **kw):
        return self._put_stop_recurring(df, 'ds_pause', crm_id, user)

    def put_batch_process(self,  df, crm_id=None, user='internal', **kw):
        _df = self._action_formatter(df, 'batch_process', crm_id, user)
        return self.upsert(_df)

    def put_set_recurring_date(self,  df, crm_id=None, user='internal', **kw):
        return self._date_putter(df, 'recurring_date', crm_id, user)

    def put_set_retry_date(self,  df, crm_id=None, user='internal', **kw):
        return self._date_putter(df, 'retry_date', crm_id, user)

    def put_set_rebill_price(self, df, crm_id=None, user='internal', **kw):
        price_key = None
        p_cols = ['dynamic_product_price', 'price', 'rebill_price']
        for p in p_cols:
            if p in df.columns:
                price_key = p
                break
        if price_key is None:
            raise AttributeError(f"DataFrame must contain 1 of the following columns: {p_cols.join(', ')}")
        _df = self._action_formatter(df, 'rebill_price', crm_id, user)
        _df['rebill_price'] = _df[price_key]
        _df.dropna(subset='rebill_price', inplace=True)
        return self.upsert(_df)

    def put_set_billing_info(self, df, crm_id=None, user='internal'):
        _df = self._action_formatter(df, 'set_billing_info', crm_id, user)
        return self.upsert(_df)

# Next go to the actions handlers and fill all the above in properly and test them all
# then work on the batch order filler specifically for H's ds thing
# then implement the cancel methods across everywhere

class InternalOverride(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'processing', 'internal_override')
        self.set_constraint('internal_override_pk', ['crm_id', 'order_id'])

