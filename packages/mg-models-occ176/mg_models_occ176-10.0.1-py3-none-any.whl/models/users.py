from models.db import Db, pd
from hashlib import sha256
import json


class Users(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'clients_global', 'users')
        # self.set_constraint('clients_pk', ['client_id'])

    @staticmethod
    def encoded_user(user):
        return sha256(user.encode()).hexdigest()

    def get_ui_config(self, user):
        return self.get(['ui_config'], where=f" where username = '{user}'").iloc[0].values

    def set_ui_config(self, user, acc_id, key, config):
        try:
            conf = self.engine.execute(
                f""" select ui_config from {self.schema}.{self.table} where username = '{user}' and account_id = '{acc_id}'

                """
            ).fetchone()[0]
            conf[key] = config
            self.engine.execute(
                f"""update {self.schema}.{self.table} 
                    set ui_config = %s::jsonb
                    where username='{user}'
                    and account_id = '{acc_id}'
                """,
                [json.dumps(conf)]

            )
            return True
        except Exception as e:
            return False

    def del_ui_config(self, user, acc_id, key):
        try:
            conf = self.engine.execute(
                f""" select ui_config from {self.schema}.{self.table} where username = '{user}' and account_id = '{acc_id}'

                           """
            ).fetchone()[0]
            res = conf.pop(key, None)
            if res:
                self.engine.execute(
                    f"""update {self.schema}.{self.table} 
                                   set ui_config = '{json.dumps(conf)}'::jsonb
                                   where username='{user}'
                                   and account_id = '{acc_id}'
                               """
                )
            return True
        except Exception as e:
            return False


