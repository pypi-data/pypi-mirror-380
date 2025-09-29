from .cb_struc import CbStructure


class ChargeBacks(CbStructure):
    col_map = {'id': 'chargeback_id', 'case_no': 'case_number', 'case_type': 'cycle',
               'cc_type': 'card_type', 'date_post': 'post_date', 'date_trans': 'trans_date', 'bin': 'cc_bin', 'card_last_four': 'cc_last4'}

    def __init__(self, db, account_id):
        CbStructure.__init__(self, db, account_id, 'cb_data')
        self.set_constraint('cb_data_pk', ['chargeback_id'])

    @staticmethod
    def format_data(df):
        d = ChargeBacks.format_col_names(df).rename(columns=ChargeBacks.col_map)
        d.status_history = d.status_history.astype(str)
        return d

