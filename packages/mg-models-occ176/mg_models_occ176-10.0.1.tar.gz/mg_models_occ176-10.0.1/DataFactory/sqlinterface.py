from  sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import pandas as pd
from cryptography.fernet import Fernet
import requests
import datetime as dt


class Db:
    def __init__(self, connstr=False, schema='public', max_connections=10, max_overflow=10, server=False, pool_recycle=1200, **kw):
        self.server = None
        if server:
            self.server = server
            con = self.my_conn_str()
        else:
            con = connstr

        self.engine = create_engine(con, pool_size=max_connections, max_overflow=max_overflow, pool_pre_ping=True, pool_recycle=pool_recycle, **kw)

    def __del__(self):
        if self.server:
            try:
                self.server.stop(force=True)
            except Exception as e:
                print(str(e))



    @staticmethod
    def my_conn_str(user,  password, host, port, db_name, **kwargs):
        return 'mysql+pymysql://' + user + ':' + password + '@' + host + ':'+str(port)+'/'+db_name

    @classmethod
    def ssh_tunnel(cls, ssh_host,  ssh_host_pass, conn,  ssh_user='root',  ssh_port=22):
            server = SSHTunnelForwarder(
                (ssh_host, int(ssh_port)),
                ssh_username=ssh_user,
                ssh_password=ssh_host_pass,
                remote_bind_address=(conn['host'], int(conn['port'])))
            server.start()
            local_port = str(server.local_bind_port)
            return cls(connstr=cls.my_conn_str(conn['user'], conn['pass'],
                                               conn['host'], local_port, conn['db_name']),
                       server=server)


class select:
    def __init__(self, Db, qry=None):
        self.engine = Db.engine
        self.qry = qry

    def get(self, res=False, index=None):
        try:
            r = [dict(q) for q in self.engine.execute(self.qry)]
        except:
            return False
        if res:
            if index is not None:
                res[index] = r
            else:
                re = r
            return
        return r

    def getDf(self,res=None, index=None):
        df = None
        try:
            df = pd.read_sql(self.qry, self.engine)
        except Exception as e:
            print(e)
            return False

        if res is not None:
            if index is not None:
                res[index] = df
            else:
                res = df
            return True
        return df

    @staticmethod
    def buildqry(name, cols, **kwargs):
        c = '*'
        if isinstance(cols,list):
            c = str('.'.join(cols))
        elif isinstance(cols,str):
            c = cols
        whr = ''
        ob =''
        if 'where' in kwargs:
            whr = "where "+kwargs['where']

        if 'orderby' in kwargs:
            ob = "Order By "+kwargs['orderby']

        return "select {c} from {name} {whr} {ob} ".format(c=c, name=name, whr=whr, ob=ob)
