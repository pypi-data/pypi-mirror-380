import datetime as dt
from models import config
CASTS = {'float64': 'decimal','decimal':'decimal', 'int64': 'int', 'O': 'text', 0: 'text', '0': 'text', 'o': 'text', 'object': 'text'}
ALERT_PROVIDERS = ['ethoca', 'rdr']
AGG_CAST = {
    'acquisition_date': 'date',
    'month_date': 'date',
    "next_cycle_date": 'date',
    "gateway_date_added": 'date'
}

def format_agg(a):
    if '::' in a:
        return a
    agg = AGG_CAST.get(a, None)
    if not agg:
        return a
    return f'{a}::{agg}'

def now():
    return dt.datetime.now() - dt.timedelta(hours=config.timeOffset)


def today():
    return now().date()


def _get_interval_date(date,offset):
    return f"('{date}'::date -INTERVAL '{offset} days')"


def get_first_dom():
    return now().replace(day=1).date()


def get_cast(c, dtype):
    global CASTS
    #print(c)

    try:
        d = str(dtype)
        if d == 0 or d == '0':
            print(d)
        if '%' in c:
            return 'percent'
        elif '$' in c:
            return 'dollar'
        cast = CASTS[d]
    except Exception as e:
        print('error', str(e))
        cast = 'text'
    return cast


def get_order_by(group_by, order_by):
    return f"""{'a.' + ', a.'.join(group_by) if order_by == 'group' else ','.join([format_agg(o) for o in order_by]) if isinstance(
        order_by, list) else 'initial desc'}"""


def get_filters(filters, alias='', translate={}, prefix="AND", convert_bool=False):
    f_whr = ""

    for k, v in filters.items():

        f_whr += f""" {prefix if  not f_whr else "AND"} lower({alias}{translate[k] if k in  translate else k}::text) = Any(ARRAY{str(v).lower()}::text[]) """ + '\n'
    return f_whr


def format_group_by(group_by):
    if not isinstance(group_by, list):
        if not isinstance(group_by, str):
            raise TypeError(f'group_by must be of type str or list got {str(type(group_by))}')
        group_by = [group_by]

    return [format_agg(g) for g in group_by]