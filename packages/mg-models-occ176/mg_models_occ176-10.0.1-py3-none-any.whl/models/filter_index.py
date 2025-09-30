
import pandas as pd




class FilterIndex():
    def __init__(self, db):
        self.db = db
        self.schema = 'ui_filter_values'
    _col_map = {}

    @staticmethod
    def name_map(filters):
        def _map(f):
            try:
                return FilterIndex._col_map[f]
            except KeyError:
                return f

        return {_map(k): v for k, v in filters.items()}

    def get(self, name):
        return pd.read_sql(f"select * from {self.schema}.{name}", self.db.engine).rename({
            'filter_display_value': 'name', 'filter_query_value': 'value'},
            axis=1)



