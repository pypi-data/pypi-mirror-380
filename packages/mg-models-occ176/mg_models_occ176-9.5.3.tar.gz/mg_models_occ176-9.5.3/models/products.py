from models.db import Db, pd


class Products(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'crm_global', 'products')
        self.set_constraint('products_pk', ['crm_id',  'product_id'])
        self.crm_id = crm_id

    def _kk_product_list(self, campaign_id=False, **kwargs):
        try:
            lst = self.get(['campaign_id::text', 'campaign_product_id as value', 'product_name as text'],
                       orderBy='campaign_product_id desc',
                       where=f"where campaign_id='{campaign_id}'" if campaign_id else "")
        except Exception as e:
            print(str(e))

        lst['text'] = lst.campaign_id + ' - ' + lst['value'].astype(str) + ' - ' + lst['text']
        lst['key'] = lst.value
        return lst.drop('campaign_id', axis=1).to_dict(orient='records')

    def _ll_product_list(self, campaign_id=False, **kwargs):
        lst = self.get(['product_id::int as value', 'name as text'],
                       where=f"where crm_id='{self.crm_id}'",
                       orderBy='product_id desc',
                       )
        lst['text'] = lst['value'].astype(str) + ' - ' + lst['text']
        lst['key'] = lst.value
        return lst.to_dict(orient='records')

    def product_list(self, campaign_id=False, **kwargs):
        prd = None
        if '_kk_' in self.crm_id:
            prd = self._kk_product_list(campaign_id, **kwargs)
        else:
            prd = self._ll_product_list(campaign_id, **kwargs)
        return [{'text':  'Select Product', 'value':  None, 'key': 'xxx'}] + prd

    def get_main_product_id(self, campaign_pid):
        if '_kk_' in self.crm_id:
            return self.engine.execute(f"""
                    select product_id from {self.schema}.{self.table}
                    where campaign_product_id='{campaign_pid}'
                    """).scalar()