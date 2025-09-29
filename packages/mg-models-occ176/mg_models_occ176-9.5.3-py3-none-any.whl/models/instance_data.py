from models.db import ClientStructure, pd


class InstanceData(ClientStructure):
    def __init__(self, db, account_id='54407332'):
        ClientStructure.__init__(self, db, 'instance_data', account_id)
        self.set_constraint('instance_data_pk', ['crm_id'])
    def get_instances(self, cols=False, instances=False, crm='',   archived=False):

        where = ''

        def _set_where(whr):
            nonlocal where
            if where != '':
                where = f'{where} and {whr}'
                return
            where = f' where {whr}'

        if crm:
            _set_where(f"crm_brand = '{crm}'")
        if instances:
            _set_where(f"crm_id = ANY(ARRAY{instances}::text[])")
        if archived is not None:
            _set_where('archived' if archived else 'not archived')

        return self.get(cols, where=where)

    def get_instance(self, crm_id, cols=['crm_id', 'api_users', 'api_passwords', 'api_url', 'proxies'], as_tuple=False):
        res = self.get(cols, where=f"where crm_id = '{crm_id}'")
        if as_tuple:
            return res.to_records(index=False)[0]
        return res.to_dict('records')[0]

    def crm_list(self, archived=False,  as_combo_box=False, add_cols=[]):
        where = ''
        if archived is not None:
            where = f"where {'archived' if archived else  'not archived'}"
        try:
            payload = self.get(['crm_id', 'user_friendly_name']+add_cols,  where=where)
            if as_combo_box:
                payload['text'] = payload.user_friendly_name
            return payload.rename(
                columns={'crm_id': 'value', 'user_friendly_name': 'name'},

            )
        except Exception as e:
            print(e)

    def get_crm_id_list(self):
        return self.get(['crm_id']).crm_id.tolist()

    def get_test_info(self, crm_id):
        return self.get(['test_offers', 'test_card_profile'], where=f" where crm_id = '{crm_id}'")
