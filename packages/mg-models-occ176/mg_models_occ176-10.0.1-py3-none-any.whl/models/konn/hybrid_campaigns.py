from models.campaigns import Campaigns, pd


class HybridCampaigns(Campaigns):
    def __init__(self, db, account_id):
        Campaigns.__init__(self, db, account_id)
        self._col_map = {
            'campaignId': 'campaign_id',
            'campaignName': 'campaign_name',
            'campaignType': 'campaign_type',

        }

    def format_data(self, df, crm_id):
        nd = df[list(self._col_map.keys())].rename(columns=self._col_map)
        nd['crm_id'] = crm_id
        return nd
