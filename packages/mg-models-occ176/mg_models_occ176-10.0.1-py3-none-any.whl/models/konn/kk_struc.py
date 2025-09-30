from models.db import Db, np, pd
import re
import datetime as dt
from models.konn import config as kk_conf


class KKStruc(Db):

    def __init__(self, db, crm_id, table):
        Db.__init__(self, db,  crm_id, table)
        self._crm_id = crm_id

    def format_col_names(self, df):
        d = df.rename(columns={c: re.sub("(\w)([A-Z])", r"\1_\2", f'{c}').lower() for c in df.columns}).rename(columns={'3_dtxn_result':'three_d_txn_result'})
        return d

    def format_data_to_glob(self, df, drop=[]):
        return df[list(self._col_map.keys())].drop(
            columns=drop, errors='ignore').replace(r'^\s*$', np.nan, regex=True).rename(columns=self._col_map)

    def format_data(self, df, format_col_names=True, drop=[]):
        print('formatting', self.table)
        _df = self.format_ts_offset(df)
        _df = _df.drop(columns=['items'] + drop, errors='ignore').replace(r'^\s*$', np.nan, regex=True)
        if 'merchantId' in _df.columns:
            _df['merchantId'] = _df['merchantId'].fillna(0).astype(int)
            ln = len(_df.loc[_df.merchantId.isna()])
            if ln:
                print(f'{ln} null merchant ids')

        if format_col_names:
            return self.format_col_names(_df)
        return _df

    @staticmethod
    def format_ts_offset(df):

        if 'dateCreated' in df.columns:
            def _set_date(d):
                return dt.datetime.strptime(d,  '%Y-%m-%d  %H:%M:%S')

            nd = _set_date(kk_conf.tz_next)
            fd = _set_date(kk_conf.tz_forward_date)
            bd = _set_date(kk_conf.tz_back_date)
            now = dt.datetime.now()
            df.dateCreated = pd.to_datetime(df.dateCreated)

            if nd.month < bd.month and dt.datetime.now() < fd and dt.datetime.now() > bd:
                msk = (df.dateCreated >= pd.to_datetime(fd)) & (df.dateCreated <= pd.to_datetime(bd))
                df.loc[msk, 'dateCreated'] += dt.timedelta(hours=1)
            elif nd.month > bd.month and dt.datetime.now() < bd and dt.datetime.now() > fd:
                msk = (df.dateCreated >= pd.to_datetime(bd)) & (df.dateCreated <= pd.to_datetime(fd))
                df.loc[msk, 'dateCreated'] -= dt.timedelta(hours=1)


        return df

    def max_last_modified(self):
        return self.engine.execute(f"""select max(date_updated) from {self.schema}.{self.table}""").scalar()

    def max_time_stamp(self):
        return self.engine.execute(f"""select max(date_created) from {self.schema}.{self.table}""").scalar()

    def max_most_recent_activity(self):
        return self.engine.execute(f"""select max(most_recent_activity) from {self.schema}.{self.table}""").scalar()

    def _global_update(self, df, keys):
        self.update(df[list(self._col_map.keys())].rename(columns=self._col_map), keys)