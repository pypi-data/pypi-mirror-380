from models.db import ClientStructure, pd


class ProcessorSettings(ClientStructure):
    def __init__(self, db, account_id):
        ClientStructure.__init__(self, db, 'processor_settings', account_id)
        self.set_constraint('processor_settings_pk', ['crm_id'])

    def _current_chk(self, curr_set, crm_id):
        if not curr_set:
            return self.get(where=f" where crm_id='{crm_id}' " if crm_id else '')
        if crm_id:
            curr_set = curr_set.loc[curr_set.crm_id == crm_id]
        return curr_set

    def _fmt_pct(self, pct):
        if pct > 100:
            pct = 100
        elif pct < 0:
            pct = 0
        return pct

    def _set_combined(self, curr_set, pct, crm_id, ch_col, unch_col):
        df = self._current_chk(curr_set, crm_id)
        df[ch_col] = self._fmt_pct(pct)
        df['tot'] = df[ch_col] + df[unch_col]
        msk = df.tot > 100
        df.loc[msk, unch_col] -= (df.loc[msk, 'tot'] - float(100))
        df.loc[df[unch_col] < .01, unch_col] = 0
        df.drop('tot', axis=1, inplace=True)
        self.upsert(df[['crm_id', ch_col, unch_col]])
        return df

    def set_sample_pct(self, pct, crm_id=False, curr_set=False):
        return self._set_combined(curr_set, pct, crm_id, 'ml_sample_pct', 'ml_optimize_pct')

    def set_optimize_pct(self, pct, crm_id=False, curr_set=False):
        return self._set_combined(curr_set, pct, crm_id, 'ml_optimize_pct', 'ml_sample_pct')


class MLSettings(ClientStructure):
    def __init__(self, db, account_id):
        ClientStructure.__init__(self, db, 'ml_settings', account_id)
        self.set_constraint('ml_settings_pk', ['group_key'])

    def next_group_key(self):
        return self._max('group_key') + 1

    def get_active(self, crm_id=False):
        an = ''
        if crm_id:
            an = f"and crm_id = '{crm_id}'"
        return pd.read_sql(f"""Select a.*,b.crm_id, b.col ,b.enable_optimise, b.enable_random_sampling
                                   from  {self.schema}.{self.table} a
                                   Join {self.schema}.ml_sample_groups b on b.group_key = a.group_key
                                   where a.active = true
                                   {an}""", self.engine)


class MLSampleGroups(ClientStructure):
    def __init__(self, db, account_id):
        ClientStructure.__init__(self, db, 'ml_sample_groups', account_id)
        self.set_constraint('ml_sample_groups_pk', ['crm_id', 'col', 'active', 'group_key'])



