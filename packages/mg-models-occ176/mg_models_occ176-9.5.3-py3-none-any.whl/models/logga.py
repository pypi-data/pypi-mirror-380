#from config import ABSPATH
import datetime as dt
import json
from flask import request,session
import os
import pandas as pd
ABSPATH = '/var/alexis/project'



def _log(action, user, path, data={}, use_ip=True):

    t = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(path, 'a') as f:
        log_line = t + ' | '
        log_line += str(user) + ' | '
        if use_ip:
            log_line += request.remote_addr + ' | '
        log_line += action + ' | '
        #log_line += _iu98Iokldk736UUmdhj90Ljh8(t, user, request.remote_addr)

        if isinstance(data, (dict, list)):
            log_line += json.dumps(data) + '\n'
        elif isinstance(data, (pd.DataFrame, pd.Series)):
            log_line += json.dumps(data.to_dict(orient='records')) + '\n'
        else:
            log_line += str(data)+'\n'
        f.write(log_line)


def _exception(data, exception):
    pass


def user_log(user, action, data={}):
    os.makedirs(ABSPATH + '/models/log', exist_ok=True)
    _log(action, str(user), ABSPATH + '/models/log/users.log', data)


def sub_log(user, action, data={}, exception=False):
    try:
        if exception:
            data = {**data, **{'exception': str(exception)}}
        os.makedirs('/var/log/php/', exist_ok=True)
        _log(action, str(user), '/var/log/php/sub.log', data, use_ip=False)
    except Exception as e:
        print(str(e))


def comm_log(user, action, data={}, exception=False):
    try:
        os.makedirs('/var/log/php/', exist_ok=True)
        if exception:
            data = {**data, **{'exception': str(exception)}}
        _log(action, str(user), '/var/log/php/comm.log', data, use_ip=False)
    except Exception as e:
        print(str(e))


def processing_log(action, data={}, exception=False):
    try:
        os.makedirs('/var/log/alexis/', exist_ok=True)
        if exception:
            data = {**data, **{'exception': str(exception)}}
        _log(action, 'processor', '/var/log/alexis/processing.log', data, use_ip=False)
    except Exception as e:
        print(str(e))


def duplicate_log(action, data={}, exception=False):
    try:
        os.makedirs('/var/log/alexis/', exist_ok=True)
        if exception:
            data = {**data, **{'exception': str(exception)}}
        _log(action, 'duplicate handler', '/var/log/alexis/duplicates.log', data, use_ip=False)
    except Exception as e:
        print(str(e))
