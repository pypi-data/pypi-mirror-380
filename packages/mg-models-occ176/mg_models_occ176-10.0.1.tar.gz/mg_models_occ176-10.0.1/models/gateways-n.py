import pandas as pd
import datetime as dt
from models.db import ClientStructure as Clients, Db
from models import config


class GatewaySettings(Clients):
    def __init__(self, db,  account_id='54407332'):
        Clients.__init__(self, db, 'gateway_settings', account_id)
        self.set_constraint('gateway_settings_pk', ['gateway_id', 'crm_id'])

    def get_exploded(self):
        df = self.get(orderBy='gateway_id')
        df.cascade_to = df.cascade_to.fillna(0)
        return self.explode(df, ['days', 'days_index']).drop(['min_hour', 'max_hour'], axis=1).set_index('gateway_id')

    def disable(self, crm_id, gateway_id):
        if not isinstance(gateway_id, list):
            gateway_id = [gateway_id]
        self.engine.execute(f"""update {self.schema}.{self.table} set enabled = false where crm_id = '{crm_id}' and gateway_id = any(Array{gateway_id}::int[]) """)

    @staticmethod
    def get_first_dom():
        return dt.datetime.now().replace(day=1).date()

    @staticmethod
    def get_get_tomorrow():
        return (dt.datetime.now() + dt.timedelta(days=1)).date()

    def cap_report(self, crm_id, s_date=False):
        return pd.read_sql(f"""         
        select a.crm_id, a.gateway_id, a.daily_cap,a.monthly_cap, processed from {self.schema}.{self.table} a 
           left join( 
               select crm_id, gateway_id, sum(order_total)::numeric processed from crm_global.orders 
               where crm_id = '{crm_id}' {f"and time_stamp >=  '{s_date}'" if s_date else ""} and decline_reason is null
               group by crm_id, gateway_id
               )  b  on  a.crm_id  = b.crm_id and a.gateway_id =  b.gateway_id
            where a.crm_id  = '{crm_id}'
           """, self.engine).fillna(0)

    def mtd_cap_report(self, crm_id):
        return self.cap_report(crm_id, self.get_first_dom())

    def today_cap_report(self, crm_id):
        return self.cap_report(crm_id, (dt.datetime.now() - dt.timedelta(hours=config.timeOffset)).date())

    def mtd_cascade_report(self, crm_id):
        qry = f"""         
              select a.crm_id, a.gateway_id, a.cascade_cap, b.cascade_processed from {self.schema}.{self.table} a 
                 left join( 
                     select c.crm_id, c.gateway_id, sum(c.order_total) cascade_processed from  
                       (select distinct(order_id) from processing.processing_actions where is_dead_mid_cascade AND crm_id='{crm_id}') a
                        inner join augmented_data.order_cycles b on b.parent_id = a.order_id and b.crm_id = '{crm_id}'  and b.decline_reason is null  
                        and b.time_stamp between '{self.get_first_dom()}'  AND '{self.get_get_tomorrow()}'
                        inner join crm_global.orders c on c.order_id =  b.order_id  and c.crm_id =  b.crm_id
                        --inner join crm_global.orders  d on d.order_id =  b.parent_id  and d.gateway_id !=  c.gateway_id and c.crm_id =  b.crm_id  
                        group  by  c.crm_id, c.gateway_id
                     )  b  on  a.crm_id  = b.crm_id and a.gateway_id =  b.gateway_id
                  where a.crm_id  = '{crm_id}'
                  
                  
                 """
        #print(qry)
        df = pd.read_sql(qry, self.engine)

        df.loc[df.cascade_cap.isna(), 'cascade_cap']  =  20000.00
        df.loc[df.cascade_processed.isna(), 'cascade_processed'] = 0
        df['available'] = df.cascade_cap - df.cascade_processed
        return df

    def cap_limits(self, crm_id):
        df = self.today_cap_report(crm_id).merge(
            self.mtd_cap_report(crm_id)[['gateway_id', 'crm_id', 'processed']].rename({
                'processed': 'available'}, axis=1),
            on=['gateway_id', 'crm_id'], how='left')
        df.loc[df.monthly_cap.isna(), 'cascade_cap'] = 20000.00
        df.loc[df.available.isna(), 'available'] = 0
        df['available'] = df.monthly_cap - df.available
        return df



class GatewayNames(Clients):
    def __init__(self, db,  account_id='54407332'):
        Clients.__init__(self, db, 'gateways', account_id)
        self.set_constraint('gatewaynames_pk', ['id', 'crm_id'])

    def gateway_corp_list(self, crm_id=False):
        whr = ''
        if crm_id:
            whr = f" WHERE crm_id = {crm_id} "
        return self.get(columns=['id', 'gateway_corp']).rename(columns={'id': 'gateway_id'}, where=whr)

    def update_lists(self, crm_id):
        gt_list = [q[0] for q in self.engine.execute(f"select distinct gateway_id from crm_global.orders where crm_id= '{crm_id}' ")]
        gateways_up = [q[0] for q in self.engine.execute(f"select  id from {self.schema}.{self.table} where crm_id = '{crm_id}'")]
        gateway_set_up = [q[0] for q in self.engine.execute(f"select gateway_id from {self.schema}.gateway_settings where crm_id = '{crm_id}'")]
        gateways_ins = list(set(gt_list) - set(gateways_up))
        gateway_set_ins = list(set(gt_list+gateways_up) - set(gateway_set_up))
        if not len(gt_list):
            gateway_set_ins = gateways_up
        return {
                'gt_list': gt_list,
                'gateways_up': gateways_up,
                'gateway_set_up': gateway_set_up,
                'gateways_ins': gateways_ins,
                'gateway_set_ins': gateway_set_ins
                }


class GatewaySteps(Clients):
    def __init__(self, db, account_id='54407332'):
        Clients.__init__(self, db, 'steps', account_id)
        self.set_constraint('steps_pk', ['app_step_id', 'crm_id'])

    def get_no_cvv_required(self, crm_id, columns=False):
        return self.get(columns, where=f""" where scv_level= 'not required' and crm_id='{crm_id}'""")

    def get_mid_numbers_by_mid_id(self, mid_id, step):
        ret = self.get(['crm_id', 'mid_number'], where=f""" where mid_id={int(mid_id)} and step={int(step)}""")
        if len(ret):
            return ret.drop_duplicates().to_dict(orient='records')

    def get_mid_numbers_by_gateway_id(self, gateway_id, crm_id):
            df = self.get(['mid_number'], where=f""" where gateway_id={gateway_id} and crm_id = '{crm_id}' """).dropna()
            if len(df):
                return df.mid_number.tolist()[0]
            return None


class CapReport(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'processing', 'cap')
        self.set_constraint('cap_pk', ['mid_id', 'step', 'processor'])

    def get_alert_level(self):
        return self.get(['mid_id', 'step', 'processor', 'gateway_id', 'alert_level'])

    def increment_transaction_counts(self, mid_id, processor, step, is_lp=False):
        _set = f"set used_dtc = used_dtc+1 {', used_lptc = used_lptc+1' if is_lp else ''}"
        self.engine.execute(f"""update {self.schema}.{self.table} set {_set} where mid_id ={int(mid_id)} and step = {int(step)}""")

    def get_gateway_cap_model(self, crm_id):
        return pd.read_sql(f"""
            select b.gateway_id, b.crm_id, a.* from {self.schema}.{self.table} a 
            inner join ui_54407332_clients.steps b on b.mid_id = a.mid_id and b.crm_id = '{crm_id}' and b.step = a.step                       
        """, self.engine)


class CCTypeCapReport(Db):
    def __init__(self, db):
        Db.__init__(self, db, 'processing', 'cap_cc_type')
        self.set_constraint('cap_cc_type_pk', ['mid_id', 'step', 'processor', 'cc_type'])

    def get_alert_level(self):
        return self.get(['mid_id', 'step', 'processor', 'gateway_id', 'alert_level'])

    def get_gateway_cap_model(self, crm_id):
        return pd.read_sql(f"""
            select b.gateway_id, b.crm_id, a.* from {self.schema}.{self.table} a 
            inner join ui_54407332_clients.steps b on b.mid_id = a.mid_id and b.crm_id = '{crm_id}' and b.step = a.step                       
        """, self.engine)
