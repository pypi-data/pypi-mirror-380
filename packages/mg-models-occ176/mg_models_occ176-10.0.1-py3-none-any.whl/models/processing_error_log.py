from models.db import Db, pd, np
import datetime as dt


class ProcessingErrorLog(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'int_log', 'processing_error_log')
        self.set_constraint('processing_error_log_pk', ['id'])

    @staticmethod
    def error_log_line(ords, error, error_code):
        pd.set_option('mode.chained_assignment', None)
        err_cols = ['order_id', 'customer_id', 'is_recurring', 'on_hold', 'is_void']
        if 'time_stamp' in ords:
            err_cols.append('time_stamp')

        loglines = None

        if isinstance(ords, dict):
            loglines = pd.DataFrame(ords)
            err_cols = list(set(err_cols) & set(list(loglines.columns)))
            loglines = ords[err_cols]
        elif isinstance(ords, (pd.DataFrame, pd.Series)):
            err_cols = list(set(err_cols) & set(list(ords.columns)))
            loglines = ords[err_cols]
        else:
            raise TypeError('ords must be of type dict dataframe or series')
        loglines['error'] = error
        loglines['error_code'] = error_code

        if 'on_hold' in loglines.columns:
            loglines.on_hold.fillna(0, inplace=True)
            loglines = loglines.replace({'yes': 1, 'no': 0})
        return loglines

    def processing_prevented_report(self, date):
        qry = """        
            SELECT a.*, hours_index, tot_proc_hours,tot_proc_gwy from (
                  SELECT gateway_id, days_index, count(*) as tot_proc_days from thedatabase.processing_log
                  WHERE time_stamp::date = '{d}'::date
                  GROUP BY gateway_id, days_index
                  ORDER BY gateway_id, days_index
              ) as a
            LEFT JOIN (
                SELECT gateway_id, days_index, hours_index, count(*) as tot_proc_hours from thedatabase.processing_log
                WHERE time_stamp::date = '{d}'::date
                GROUP BY gateway_id, days_index,hours_index
                ORDER BY gateway_id, days_index,hours_index) as b
            ON (a.gateway_id = b.gateway_id AND a.days_index=b.days_index)
            LEFT JOIN (
                SELECT gateway_id, count(*) as tot_proc_gwy from thedatabase.processing_log
                WHERE time_stamp::date = '{d}'::date
                GROUP BY gateway_id
                ORDER BY gateway_id) as c
            ON (a.gateway_id = c.gateway_id)
             
        """.format(d=date)
        return pd.read_sql(qry, self.engine)



