from models.db import Db, pd
from models import config
import datetime as dt
import pytz


def today():
    return (dt.datetime.now().astimezone(pytz.timezone('US/Eastern'))).date()


class AlertProviders(Db):
    def __init__(self, db, ):
        Db.__init__(self, db, 'reporting', 'alert_providers')
        self.set_constraint('alert_providers_pk', ['alert_provider'])

