from models.gateways import GatewayNames, GatewaySettings
import pandas as pd


class HybridGatewayNames(GatewayNames):
    def __init__(self, db, account_id):
        GatewayNames.__init__(self, db, account_id)
        self._col_map = {
            'merchant': 'gateway_alias',
            'merchant_id': 'id',
            'merchant_descriptor': 'descriptor',
        }

    def format_data(self, df, crm_id):
        nd = df[list(self._col_map.keys())].rename(columns=self._col_map)
        nd['crm_id'] = crm_id
        return nd


class HybridGatewaySettings(GatewaySettings):
    def __init__(self, db, account_id):
        GatewaySettings.__init__(self, db, account_id)
        self._col_map = {
            'merchant_id': 'gateway_id',
        }

    def format_data(self, df, crm_id):
        nd = df[list(self._col_map.keys())].rename(columns=self._col_map)
        nd['crm_id'] = crm_id
        return nd