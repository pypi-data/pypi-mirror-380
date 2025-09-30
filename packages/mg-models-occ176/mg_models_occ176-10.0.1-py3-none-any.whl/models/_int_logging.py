import datetime as dt
from flask import request, session
import json
import os
import pandas as pd
ABSPATH = '/var/log/'
from threading import Lock
from filelock import FileLock


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


def update_log(action, data={}, exception=False):

    try:
        os.makedirs('/var/log/updater/', exist_ok=True)
        with FileLock('/var/log/updater/update.log.lock'):
            if exception:
                data = {**data, **{'exception': str(exception)}}
            _log(action, 'updater', '/var/log/updater/update.log', data, use_ip=False)
    except Exception as e:
      pass


def processor_log(crm_id, action, data={}, exception=False):
    try:
        os.makedirs('/var/log/alexis/', exist_ok=True)
        with FileLock('/var/log/alexis/processor.log.lock'):
            if exception:
                data = {**data, **{'exception': str(exception)}}
            _log(crm_id + ' | ' + action, 'processor', '/var/log/alexis/processor.log', data, use_ip=False)
    except Exception as e:
      pass
