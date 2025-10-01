from models.db import Db, np, pd
import re


class CbStructure(Db):


    def __init__(self, db, account_id, table):
        Db.__init__(self, db, f'ui_{account_id}_cb_911', table)

    @staticmethod
    def format_col_names(df):
        return df.rename(columns={c: re.sub("(\w)([A-Z])", r"\1_\2", f'{c}').lower()
                                  for c in df.columns}).astype(str).apply(lambda x: x.str.strip(), axis=1)



