from models.db import Db, pd


class ProcessingPreventedLog(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'thedatabase', 'processing_prevented_log')

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



