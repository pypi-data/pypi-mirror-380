
import pandas as pd


class ColorIndex():
    def __init__(self, db):
        self.db = db
        self.schema = 'ui_color_index'
    _col_map = {}

    @staticmethod
    def name_map(filters):
        def _map(f):
            try:
                return ColorIndex._col_map[f]
            except KeyError:
                return f

        return {_map(k): v for k, v in filters.items()}

    def get(self, name, key):
        return pd.read_sql(f"select * from {self.schema}.{name}",
                           self.db.engine).astype(str).set_index(key).to_dict(orient='index')