from models.db import ClientStructure, pd


class GatewayProviders(ClientStructure):
    def __init__(self, db, acc_id):
        ClientStructure.__init__(self, db, 'provider', acc_id)

