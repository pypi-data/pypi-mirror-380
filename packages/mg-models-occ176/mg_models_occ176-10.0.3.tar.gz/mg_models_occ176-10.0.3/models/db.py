import pandas as pd
import warnings
from sqlalchemy.orm import sessionmaker

import json

import numpy as np
from models import api
from threading import Thread
import psycopg2 as psy
import psycopg2.errors as err
from sqlalchemy import exc
import _pickle as pickle
import os
DEBUG = bool(int(os.environ.get('DEBUG', 0)))
cast_map = {
    'smallint': int,
    'bigint': int,
    'integer': int,
    'decimal': float,
    'numeric': float,
    'real': float,
    'double precision': float,
    'smallserial': int,
    'serial': int,
    'bigserial': int,
    'bit': bool,
    'boolean': bool,
    'text': lambda x: f"'{x}'",
    'character': lambda x: f"'{x}'",
    'varchar': lambda x: f"'{x}'",
    'char': lambda x: f"'{x}'",
    'date': lambda x: f"'{x}'::date",
    'timestamp without time zone': lambda x: f"'{x}'::timestamp",
    'timestamp with time zone': lambda x: f"'{x}'::timestamp",
    'cidr': lambda x: f"'{x}'",
    'inet': lambda x: f"'{x}'",
    'macaddr': lambda x: f"'{x}'",
    'jsonb': lambda x: f"'{json.dumps(x)}'",
    'uuid': lambda x: f"'{x}'",
    'smallint[]': lambda x: '{' + f"""'{"','".join(x)}""" + '}::smallint[]',
    'bigint[]': lambda x: '{' + f"""'{"','".join(x)}""" + '}::bigint[]',
    'integer[]': lambda x: '{' + f"""'{"','".join(x)}""" + '}::integer[]',
    'decimal[]': lambda x: '{' + f"""'{"','".join(x)}""" + '}::decimal[]',
    'numeric[]': lambda x: '{' + f"""'{"','".join(x)}""" + '}::numeric[]',
    'real[]': lambda x: '{' + f"""'{"','".join(x)}""" + '}::real[]',
    'double precision[]': lambda x: '{' + f"""'{"','".join(x)}""" + '}::double precision[]',
    'bit[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::bit[]',
    'boolean[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::boolean[]',
    'bytea[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::bytea[]',
    'character[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::character[]',
    'character varying[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::character varying[]',
    'char[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::char[]',
    'text[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::text[]' if len(x) else "ARRAY[]::text[]",
    'cidr[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::cidr[]',
    'inet[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::inet[]',
    'macaddr[]': lambda x: '{' + f"""'{"','".join(x)}'""" + '}::macaddr[]',
}
import re

class Session:
    def __init__(self, engine):
        self.conn = engine.raw_connection()
        self.cur = self.conn.cursor()
        self._tmp_tables = []

    def temp_table_from_arrays(self, name, **kwargs):
        if name not in self._tmp_tables:
            self.cur.execute(f"DROP TABLE IF EXISTS {name}")
            cols = ''
            for k, v in kwargs.items():
                cols += f'unnest(ARRAY{v}) {k},'
            qry = f"""CREATE TEMP TABLE {name} as (select {cols[:-1]})"""
            self.cur.execute(qry)
            self._tmp_tables.append(name)
        return self

    def execute(self, qry):
        self.cur.execute(qry)
        return self

    def rollback(self):
        self.conn.rollback()
        return self

    def commit(self):
        self.conn.commit()

    def close(self):
        for t in self._tmp_tables:
            try:
                self.cur.execute(f"drop table if exists {t}")
            except psy.InterfaceError:
                break
        self._tmp_tables = []
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print(str(e))

    def work_mem(self, val='250MB'):
        self.cur.execute(f"SET LOCAL work_mem = '{val}'")
        return self

    def __del__(self):
        self.close()


class Db:
    _constraint = None
    _columns = None
    _pkey = None
    # _data_types = None
    _cast_map = cast_map

    def __init__(self, db, schema, table, use_month_part=False):
        try:
            self.engine = db.engine

        except AttributeError:
            self.engine = db


        self.Base = False
        self.SessionFactory = sessionmaker(self.engine)
        self.Session = False
        self.schema = schema
        self.table = table
        self._constraint = False
        self._conflict = False
        self._ins_conflict = False
        self._constraint_columns = []
        self._casts = {}
        self._cls = self.__class__

    def cast(self, **kwargs):
        self._casts = {**self._casts, **kwargs}
        return self

    @staticmethod
    def _make_list(obj):
        if not isinstance(obj, list):
            raise TypeError('obj must be of type list. Got ' + str(type(obj)))
        return ",".join([str(c) for c in obj])

    @staticmethod
    def col_stmt(columns):
        if not isinstance(columns, list):
            columns = columns
        return ','.join(columns)

    @staticmethod
    def _sub_mod_from_array_col(df, col, index, add_cols=[], merge=False, orient='columns'):
        d = df.set_index(index)
        d = d.explode(col)
        d = d.loc[~d[col].isna(), add_cols + [col]]
        nj = pd.DataFrame.from_dict(d[col].tolist())
        return d.drop(col, axis=1).reset_index().join(nj.reset_index(drop=True).drop(columns=index, errors='ignore'))

    @staticmethod
    def _sub_mod_from_dict_col(df, col, index, add_cols=[], orient='nested'):
        d = df.set_index(index)
        d = d.loc[~d[col].isna(), add_cols + [col]]
        nj = d[col].tolist()
        if orient == 'nested':
            for i in range(len(nj)):
                nj[i] = nj[i].values()
        nj = pd.DataFrame.from_dict(nj)

        return d.drop(col, axis=1).reset_index().join(nj.reset_index(drop=True))

    def _set_cast(self, k):
        try:
            return f'{k}::{self._casts[k]}'
        except KeyError:
            return k

    def get(self, columns=False, where='', orderBy=False, return_type='result'):
        _cols = '*'
        _orderBy = ''
        if len(self._casts) and not columns:
            columns = self.columns()
        if columns:
            _cols = ','.join([self._set_cast(c) for c in columns])
        if orderBy:
            _orderBy = "ORDER BY {}".format(orderBy)
        stmt = """SELECT {c} FROM {tbl} {whr} {ob} 
               """.format(c=_cols, ob=_orderBy, tbl=self.schema + '.' + self.table, whr=where)
        df = pd.read_sql(stmt, self.engine).fillna("")
        return df

    def serialize(self, df, name=False):
        try:
            if not name:
                name = self.table
            with open(f'./{name}.pickle', 'wb') as handle:
                pickle.dump(df, handle)
        except Exception as e:
            print(str(e))

    def deserialize(self, name=False):
        try:
            out = None
            if not name:
                name = self.table
            try:
                with open(f'./{name}.pickle', 'rb') as handle:
                    out = pickle.load(handle)
                return out
            except FileNotFoundError as e:
                return None
        except Exception as e:
            print(str(e))

    def scalar(self, column, where):
        return self.engine.execute(
            """
        SELECT {c} FROM {tbl} {whr} 
        """.format(c=column, tbl=self.schema + '.' + self.table, whr=where)
        ).scalar()

    def _append_relation(self):
        return self.schema + '.' + self.table

    def columns(self, nullable=None):
        if self._columns is None:
            self._columns = pd.read_sql("""
                SELECT column_name, is_nullable
                FROM information_schema.columns
                WHERE table_schema = '{s}' AND table_name   = '{t}'

            """.format(s=self.schema, t=self.table), self.engine)
            self._columns.is_nullable = self._columns.is_nullable.replace({'YES': '1', 'NO': '0'}).astype(int).astype(
                bool)
        if nullable is None:
            return self._columns.column_name.tolist()
        return self._columns.loc[self._columns.is_nullable == nullable].column_name.tolist()

    def pkey(self):
        if self._pkey is None or not hasattr(self.__class__, self._pkey):
            res = [q for q in self.engine.execute("""
            SELECT
               c.conname,
               a.attname
               FROM pg_constraint c
                    INNER JOIN pg_namespace n
                               ON n.oid = c.connamespace
                    CROSS JOIN LATERAL unnest(c.conkey) ak(k)
                    INNER JOIN pg_attribute a
                               ON a.attrelid = c.conrelid
                                  AND a.attnum = ak.k
               WHERE c.conrelid::regclass::text = '{s}.{t}'
               ORDER BY c.contype;
            """.format(s=self.schema, t=self.table))]

            self._pkey = [*zip(*res)]
            self.set_constraint(self._pkey[0], self._pkey[1])
        return self._pkey

    def data_types(self):
        if not hasattr(self.__class__, '_data_types'):
            res = [q for q in self.engine.execute(f"""
            SELECT
                pg_attribute.attname AS column_name,
                pg_catalog.format_type(pg_attribute.atttypid, pg_attribute.atttypmod) AS data_type
            FROM
                pg_catalog.pg_attribute
            INNER JOIN
                pg_catalog.pg_class ON pg_class.oid = pg_attribute.attrelid
            INNER JOIN
                pg_catalog.pg_namespace ON pg_namespace.oid = pg_class.relnamespace
            WHERE
                pg_attribute.attnum > 0
                AND NOT pg_attribute.attisdropped
                AND pg_namespace.nspname = '{self.schema}'
                AND pg_class.relname = '{self.table}'
            ORDER BY
                attnum ASC;
            """)]
            setattr(self.__class__, '_data_types', dict(res))
        return self._data_types

    def _kw_cols(self, col_wild_card, as_array=False, join_val='a'):
        if as_array:
            return [c for c in self.columns() if col_wild_card in c]
        return ','.join([f'{join_val}.{c}' for c in self.columns() if col_wild_card in c])

    def delete_all(self):
        self.engine.execute("""DELETE FROM {s}.{t}""".format(s=self.schema, t=self.table))

    def delete(self, idKey, ids, cascade=False):
        if isinstance(ids, list):
            ids = ','.join([str(i) for i in ids])
        cas = ''
        if cascade:
            cas = "CASCADE"
        stmt = """DELETE FROM {tbl} WHERE {k} in ({i}) {c}""".format(
            k=idKey, i=ids, tbl=self.schema + '.' + self.table, c=cas)
        try:
            self.engine.execute(stmt)
            return api.Response()
        except Exception as e:
            return api.Response().fail(290).data({'exception': str(e),
                                                  'error_display': 'Delete failed. Please refresh page to repopulate data set. Please contact support and notify if problem continues.'})

    def insert(self, data, return_id=False, check_cols=False, sanitize=False, **kw):
        print('inserting')
        if not isinstance(data, (list, pd.DataFrame)):
            if isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(v, str) and sanitize:
                        data[k] = re.sub(r"(?<!')'(?!')", "", v)
            if return_id:
                d = {}
                if check_cols:
                    cols = self.columns()
                    for k, v in data.items():
                        if k in cols:
                            d[k] = v
                else:
                    d = data
                names = ','.join(data.keys())
                placeholders = ','.join(['%s'] * len(data))  # Create a placeholder for each value

                sql = f"""
                         INSERT INTO {self.schema}.{self.table} ({names}) 
                         VALUES ({placeholders}) 
                         RETURNING {return_id}
                     """

                try:
                    return api.Response().data({
                        return_id: self.engine.execute(sql, list(data.values())).scalar()  # Pass values as a list
                    })
                except exc.IntegrityError as e:
                    if isinstance(e.orig, psy.errors.NotNullViolation):
                        return api.Response().fail(290).data(
                            {'error_display': e.orig.diag.column_name.replace('_', ' ').capitalize() + " is required."})
                    if isinstance(e.orig, psy.errors.UniqueViolation):
                        return api.Response().fail(290).data(
                            {'error_display': str(e.orig).split('=')[1].replace(')', '').replace('(', '').capitalize()})
                    return api.Response().fail(290).data(
                        {'exception': str(e), 'error_display': 'Save Failed. Please report to support'})
                except Exception as e:
                    t = type(e)
                    return api.Response().fail(290).data(
                        {'exception': str(e), 'error_display': 'Save Failed. Please report to support'})
            data = [data]
        try:
            return self.batch_insert(pd.DataFrame(data), check_cols=check_cols, **kw)
        except Exception as e:
            print(e)
            return api.Response().fail(290).data(
                {'exception': str(e), 'error_display': 'Save Failed. Please report to support'})

    def update(self, data):
        if not isinstance(data, list):
            data = [data]
        self._init_base()
        self._init_session()
        try:
            self.Session.bulk_update_mappings(self.tbl, data)
            self.Session.commit()
            return api.Response()
        except Exception as e:
            print(e)
            self.Session.rollback()
            return api.Response().fail(290).data({'exception': str(e)})

    def set_constraint(self, constraint, columns):
        self._constraint = constraint
        self._constraint_columns = columns

    def _set_on_conflict(self, columns):
        co = set(columns) - set(self._constraint_columns)
        colstr = ''

        for c in co:
            if colstr != '':
                colstr += ','
            colstr += """{c} =  EXCLUDED.{c} """.format(c=c, s=self.schema, t=self.table)

        self._ins_conflict = """ON CONFLICT ({c}) DO NOTHING
                                        """.format(c=','.join(self._constraint_columns))
        if not self._constraint_columns:
            self._ins_conflict = ''
            self._conflict = ''

        if colstr == '':
            self._conflict = """ON CONFLICT ({c}) DO NOTHING
                                """.format(c=','.join(self._constraint_columns))
            return
        self._conflict = """
                        ON CONFLICT ({c}) DO UPDATE SET {cols}
                    """.format(c=','.join(self._constraint_columns), cols=colstr)

    def max(self, col, where=''):
        return self.engine.execute(
            "select max ({c}) from {s}.{t} {w}".format(c=col, t=self.table, s=self.schema, w=where)).scalar()

    def multisert(self, df, max_threads=4, check_cols=True, chunk_size=1500):
        threads = []
        chunk_size = int(len(df) / max_threads)
        if chunk_size > len(df):
            chunk_size = len(df)

        def _join(_threads):
            for t in _threads:
                try:
                    t.join()

                except Exception as e:
                    print('Thread join non critical exception', e)
            _threads = []


        sdex = 0
        cols = self.columns()
        while sdex < len(df):
            threads.append(Thread(target=self.upsert, args=(df[sdex:sdex + chunk_size], list(df.columns), check_cols)))
            sdex += chunk_size
            threads[len(threads) - 1].start()
            if len(threads) >= max_threads:
                _join(threads)
                threads = []
        _join(threads)

    def _check_cols(self, df):
        cols = self.columns()
        for c in df.columns.tolist():
            if c not in cols:
                df = df.drop(c, axis=1, errors='ignore')
        return df

    def get_pg_stat(self):
        return pd.read_sql("select * from  pg_stat_activity")

    def get_blocking_queries(self, min_duration_seconds=300):
        res = pd.read_sql(
            f"""
            SELECT
            activity.pid,
            activity.usename,
            activity.query,
            activity.client_addr,
            activity.query_start,
            activity.wait_event,
            now(),
            activity.state,
            blocking.pid AS blocking_id,
            blocking.query AS blocking_query
            FROM pg_stat_activity AS activity
            LEFT JOIN pg_stat_activity AS blocking ON blocking.pid = ANY(pg_blocking_pids(activity.pid))
            where  activity.query_start + Interval '{int(min_duration_seconds)} seconds' < now() and
                activity.query   not like '%%START_REPLICATION%%' and  (
                    activity.state  =  'idle in transaction'  or
                blocking.pid is  not null);
        """, self.engine)

        return res

    def kill_process(self, pid):
        return self.engine.execute(f"select pg_terminate_backend({int(pid)})").scalar()

    def _format_sert(self, df, columns=False, check_cols=True, **kw):
        if isinstance(df, list):
            df = pd.DataFrame(df)
        elif isinstance(df, dict):
            df = pd.DataFrame([df])
        cols = columns
        if not cols:
            cols = df.columns.tolist()
        else:
            df = df[cols]
        if check_cols:
            df = self._check_cols(df)
            cols = df.columns.tolist()
        if 'month_date' in self._constraint_columns:
            try:
                df['month_date'] = pd.to_datetime(df.time_stamp).dt.date
            except KeyError:
                df['month_date'] = pd.to_datetime(df.date_time).dt.date
        return cols, df

    def batch_insert(self, df, columns=False, check_cols=True, **kw):
        if not len(df):
            return
        cols, df = self._format_sert(df, columns, check_cols)
        return self._sert(df, self._ins_conflict)

    def upsert(self, df, columns=False, check_cols=True, as_qry=False, **kw):
        if not len(df):
            return
        cols, df = self._format_sert(df, columns, check_cols)
        self._set_on_conflict(cols)
        return self._sert(df, self._conflict, as_qry=as_qry)

    def multi_insert(self, df):
        if not len(df):
            return
        if isinstance(df, list):
            df = pd.DataFrame(df)
        if self._constraint:
            if not self._ins_conflict:
                self._set_on_conflict(df.columns.tolist())
        return self._sert(df, self._ins_conflict)

    def p_keys(self):
        return self._constraint_columns

    def _sert(self, df, conflict, as_qry=False):
        qry = """
                   INSERT INTO {s}.{t} ({c})
                   Select {c}
                   FROM json_populate_recordset(null::{s}.{t},%s)
                   {con}

               """.format(con=conflict if conflict else '', s=self.schema, t=self.table,
                          c=','.join(df.columns.tolist()),
                          v='%(' + ')s,%('.join(df.columns.tolist()) + ')s')

        try:
            ic = self.__getattribute__('int_cols')
            if isinstance(ic, list):
                for c in ic:
                    df[c] = df[c].fillna(-139458273984729).astype(int).astype(str).replace({'-139458273984729': 'nan'})

        except AttributeError:
            pass
        except Exception as e:
            print(df[ic])
        try:
            if self._constraint_columns and len(self._constraint_columns):
                df = df.drop_duplicates(subset=self._constraint_columns, keep='last')
        except Exception as e:
            if DEBUG:
                print(
                    'WARNING dedup query failed not necessarily a problem unless duplicates exist that cause the query to fail later',
                    str(e))
        try:
            j = json.dumps(df.astype(str).replace(
                {'0000-00-00 00:00:00': None, 'NaT': None, 'Nan': None, 'Not ': None, 'NaN': None, 'Not': None,
                 '': None, 'nan': None, '0000-00-00': None}).replace(r"(?<!')'(?!')", "", regex=True).to_dict(
                orient='records'), ensure_ascii=False).replace('"None"', 'null')
            if as_qry:
                return qry, j
            self.engine.execute(qry, j)

        except exc.IntegrityError as e:
            print('UPSERT ERROR:', str(e))
            if isinstance(e.orig, psy.errors.NotNullViolation):
                return api.Response().fail(290).data(
                    {'error_display': e.orig.diag.column_name.replace('_', ' ').capitalize() + " is required."})
            if isinstance(e.orig, psy.errors.UniqueViolation):
                return api.Response().fail(290).data(
                    {'error_display': e.orig.diag.column_name.replace('_', ' ').capitalize() + " is must be unique."})

            return api.Response().fail(290).data(
                {'exception': str(e), 'error_display': 'Save Failed. Please report to support'})
        except Exception as e:
            print('UPSERT ERROR:', str(e))
            #  raise e
            return api.Response().fail(290).data(
                {'exception': str(e), 'error_display': 'Save Failed. Please report to support'})
        return api.Response()

    def _up(self, df, conflict):
        qry = """
                   UPDATE  {s}.{t} ({c})
                   Select {c}
                   FROM json_populate_recordset(null::{s}.{t},%s)
                   {con}

               """.format(con=conflict if conflict else '', s=self.schema, t=self.table,
                          c=','.join(df.columns.tolist()),
                          v='%(' + ')s,%('.join(df.columns.tolist()) + ')s')

        try:
            ic = self.__getattribute__('int_cols')
            if isinstance(ic, list):
                for c in ic:
                    df[c] = df[c].fillna(-139458273984729).astype(int).astype(str).replace({'-139458273984729': 'nan'})

        except AttributeError:
            pass
        except Exception as e:
            print(df[ic])
        try:
            if self._constraint_columns and len(self._constraint_columns):
                df = df.drop_duplicates(subset=self._constraint_columns, keep='last')
        except Exception as e:
            print(
                'WARNING dedup query failed not necessarily a problem unless duplicates exist that cause the query to fail later',
                str(e))
        try:
            j = json.dumps(df.astype(str).replace(
                {'NaT': None, 'Nan': None, 'Not ': None, 'NaN': None, 'Not': None, '': None, 'nan': None,
                 '0000-00-00': None}).to_dict(
                orient='records'), ensure_ascii=False).replace('"None"', 'null')
            self.engine.execute(qry, j)
        except exc.IntegrityError as e:
            if isinstance(e.orig, psy.errors.NotNullViolation):
                return api.Response().fail(290).data(
                    {'error_display': e.orig.diag.column_name.replace('_', ' ').capitalize() + " is required."})
            if isinstance(e.orig, psy.errors.UniqueViolation):
                msg = str(e).split(')')[1].strip()

                return api.Response().fail(290).data(
                    {'error_display': msg.split('\n')[0] if msg.startswith(
                        'Gateway ') else e.orig.diag.column_name.replace('_',
                                                                         ' ').capitalize() + " is must be unique."})

            return api.Response().fail(290).data(
                {'exception': str(e), 'error_display': 'Save Failed. Please report to support'})
        except Exception as e:
            return api.Response().fail(290).data(
                {'exception': str(e), 'error_display': 'Save Failed. Please report to support'})
        return api.Response()

    def pd_create(self, df, chunk_size=1500, table=False, schema=False):
        try:
            df = df.reindex(sorted(df.columns), axis=1).astype(str)
            df.to_sql(
                table if table else self.table,
                self.engine,
                schema if schema else self.schema,
                if_exists='replace',
                index=False,
                chunksize=chunk_size,
                method='multi')
        except Exception as e:
            print(e)
        return self

    def exec_raw(self, stmt):
        conn = None
        cur = None
        try:
            conn = self.engine.raw_connection()
            cur = conn.cursor()
            cur.execute(stmt)

            cur.close()
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            try:
                cur.close()
            except:
                pass
            try:
                conn.rollback()
            except:
                pass
            try:
                conn.close()
            except:
                pass

    def explode(self, df, columns):
        if not isinstance(columns, list):
            columns = [columns]
        keys = df.columns.drop(columns)

        return pd.DataFrame({
            col: np.repeat(df[col].values, df[columns[0]].str.len())
            for col in keys}
        ).assign(**{c: np.concatenate(df[c].values) for c in columns})[df.columns]

    def __del__(self):
        try:
            if self.Session:
                self.Session.close()
        except:
            pass


class Ui(Db):
    def __init__(self, db, module, table, account_id):
        Db.__init__(self, db, f"ui_{account_id}_{module}", table)


class ClientStructure(Ui):
    def __init__(self, db, table, account_id):
        Ui.__init__(self, db, 'clients', table, account_id)


class OfferStructure(Ui):
    def __init__(self, db, table, account_id):
        Ui.__init__(self, db, 'offers', table, account_id)


class Bins(Ui):
    def __init__(self, db, table, account_id):
        Ui.__init__(self, db, 'bins', table, account_id)