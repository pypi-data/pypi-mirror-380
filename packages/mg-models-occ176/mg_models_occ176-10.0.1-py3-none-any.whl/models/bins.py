from models.db import Db, pd
from models import config
import datetime as dt
import pytz


def today():
    return (dt.datetime.now().astimezone(pytz.timezone('US/Eastern'))).date()


class _BinData(Db):
    def __init__(self, db, schema, table):
        Db.__init__(self, db, schema, table)

    def get_null(self,  crm_id=False, limit=False, exclude=False,  **kwargs):
        return pd.read_sql(f"""select  a.bin 
              from (select distinct(cc_first_6) bin from crm_global.orders
                      {f"where crm_id {'!=' if exclude else '='}  '{crm_id}'" if crm_id else ""}
                  ) a  
                  left join {self.schema}.{self.table} b on b.bin  = a.bin
                  where b.bin is null
                  {f"limit {int(limit)}" if limit else ""}
              """, self.engine).dropna().bin.tolist()



    def get_oldest(self,  limit=False, **kwargs):
        return self.get(
            orderBy=f"""date_checked {f"limit {limit}" if isinstance(limit,int) else""}""")

    def insert_new(self,  df):
        d = today()
        df[['date_modified', 'date_checked']] = pd.Series([d, d]).values
        self.upsert(df)

    def get_bin(self, cc_first_6, columns=None):
        cols = ','.join(columns) if isinstance(columns, list) else '*'
        try:
            return dict(self.engine.execute(f"""SELECT {cols} from {self.schema}.{self.table} where bin='{cc_first_6}'""").fetchone())
        except Exception as e:
            return False

    def get_iin(self, cc_first_8, columns=None):
        cols = ','.join(columns) if isinstance(columns, list) else '*'
        try:
            return dict(self.engine.execute(
                f"""SELECT {cols} from {self.schema}.{self.table} where bin='{cc_first_8}'""").fetchone())
        except Exception as e:
            return False


class BinData(_BinData):
    def __init__(self, db):
        _BinData.__init__(self, db, 'ui_54407332_bins', 'iin_data')
        self.set_constraint('iin_data_pk', ['bin',  'date_modified'])


class _FBinData(_BinData):
    def __init__(self, db, schema, table, iin_col, data_table='foreign_data.issuer_acquirer'):
        _BinData.__init__(self, db, schema, table)
        self._iin_col = iin_col
        self._data_table = data_table
        self.conn = self.engine.raw_connection()
        self.cur = self.conn.cursor()

    def cleanup(self):
        try:
            self.conn.rollback()
        except:
            pass
        try:
            self.cur.close()
        except:
            pass
        try:
            self.conn.close()
        except:
            pass

    def commit(self):
        try:
            self.conn.commit()
        except Exception as e:
            self.cleanup()
            raise e
        return self

    def get_null(self, batch_size=10, lock_rows=False, **kw):
        try:
            self.execute(f"""
                SELECT {self._iin_col} from {self.schema}.{self.table} {'FOR UPDATE' if lock_rows else ''} WHERE bank IS NULL AND date_checked IS NULL FOR UPDATE LIMIT {batch_size}
            """)
        except Exception as e:
            raise e

    def insert_new(self,  df):
        d = today()
        df[['date_modified', 'date_checked']] = pd.Series([d, d]).values

        qry, j = self.upsert(df, as_qry=True)
        try:
            self.cur.execute(qry, j)
            self.commit()
        except Exception as e:
            self.cleanup()
            raise e

    def __del__(self):
        self.cleanup()


class ForeignBinData(_FBinData):
    def __init__(self, db):
        _FBinData.__init__(self, db, 'foreign_bins', 'iin_data', 'bin')
        self.set_constraint('iin_data_pkey', ['bin'])


class ForeignIIN8Data(_FBinData):
    def __init__(self, db,):
        _FBinData.__init__(self, db, 'foreign_bins', 'iin8_data', 'iin')
        self.set_constraint('iin8_data_pkey', ['iin'])


class BinDelay(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'ui_54407332_bins', 'bin_delay')
        self.set_constraint('bin_delay_pk', ['crm_id', 'cc_first_6'])


class BinBlock(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'ui_54407332_bins', 'bin_blacklist')
        self.set_constraint('bin_blacklist_pk', ['bin', 'crm_id'])


class BinRules(Db):
    def __init__(self, db, rule):
        Db.__init__(self, db, 'ui_54407332_bins', f'rule_{rule}')
        self.set_constraint('bin_delay_pk', ['crm_id', 'bin', 'rule'])

    @classmethod
    def affid(cls):
        pass
