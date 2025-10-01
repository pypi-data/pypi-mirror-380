from .cb_struc import CbStructure ,np


class Alerts(CbStructure):
    col_map = {'case_no': 'case_number', 'case_type': 'cycle',
               'cc_type': 'card_type', 'date_post': 'post_date', 'date_trans': 'trans_date'}
    date_cols = ['auth_date', 'trans_date', 'refund_date', 'date_updated', 'date_disputed',
                  'date_created', 'date_billed', 'confirmed_date', 'completed_date','outcome_date']
    source_translator = {'issuer_alert': 'Ethoca', 'ISSUER_ALERT': 'Ethoca', 'dispute': 'Verifi', 'DISPUTE': 'Verifi'}

    def __init__(self, db, account_id):
        CbStructure.__init__(self, db, account_id, 'alert_data')
        self.set_constraint('alert_data_pk', ['id'])

    @staticmethod
    def format_data(df):
        d = Alerts.format_col_names(df).rename(columns=Alerts.col_map)
        d[Alerts.date_cols] = d[Alerts.date_cols].replace({'0000-00-00 00:00:00': np.nan, '0000-00-00': np.nan})
        d['cc_bin'] = d.cc_num.str.slice(stop=6)
        d['cc_last4'] = d.cc_num.str.slice(start=-4)
        d['source'] = d.type.replace(Alerts.source_translator)
        return d