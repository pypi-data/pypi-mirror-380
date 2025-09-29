from models.db import Db, pd
from calendar import monthrange
import datetime as dt
from models import config
from threading import Thread
import json
class ErrorLog(Db):
    def __init__(self, db):
        Db.__init__(self, db, "bro_clicks", 'error_log')

    @staticmethod
    def get_val(key, **kw):
        try:
            return kw[key]
        except:
            return None

    @staticmethod
    def format(error_type, error_message, error_category,error_detail=False, **kw):
        cid = ErrorLog.get_val('click_id', **kw)
        if isinstance(error_detail, dict):
            try:
                error_detail=json.dumps(error_detail).replace("'", "''")
            except:
                error_detail = None
        else:
            error_detail = None

        return {
            'click_id': cid if cid else 'missing_click_id',
            'offer_id': ErrorLog.get_val('offer_id', **kw),
            'page': ErrorLog.get_val('page', **kw),
            'time_stamp': ErrorLog.get_val('time_stamp', **kw),
            'error_type': error_type.upper(),
            'error_message': str(error_message),
            'error_category': error_category,
            'error_detail': error_detail
        }



