from models.db import ClientStructure, pd, Db


class Mids(ClientStructure):
    def __init__(self, db, account_id):
        ClientStructure.__init__(self, db, 'mids', account_id)
        self.set_constraint('mids_pk', ['mid_id'])

    def get_app_info(self, mid_id):
        df = pd.read_sql('SELECT * from ui_accx_module.apps_to_pdf({}::int)'.format(mid_id), self.engine)
        data = df.to_dict(orient='records')
        return data[0]

    def get_app_info_x(self, mid_id):
        conn = None
        cur = None
        ret = {}
        try:
            conn = self.engine.raw_connection()
            cur = conn.cursor()
            cur.execute()
            ret = cur.fetchall()
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

    def get_template(self):
        return pd.read_sql(f"select * from {self.schema}.mid_template", self.engine)


class MidTemplates(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'ui_54407332_clients','mid_template')
        self.set_constraint('mid_template_pk', ['processor'])