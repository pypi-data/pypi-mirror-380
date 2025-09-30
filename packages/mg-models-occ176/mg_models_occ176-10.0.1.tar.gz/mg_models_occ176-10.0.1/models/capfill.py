from models.db import Db, pd
from models import config
import datetime as dt
import pytz


def today():
    return (dt.datetime.now().astimezone(pytz.timezone('US/Eastern'))).date()


class CapfillReactivate(Db):
    def __init__(self, db, ):
        Db.__init__(self, db, 'processing', 'capfill_reactivate')
        self.set_constraint('capfill_reactivate_pk', ['crm_id',  'order_id'])


