from models.db import Db, pd


class Conversions(Db):
    def __init__(self, db):
        Db.__init__(self, db, "bro_clicks", 'conversions')
        self.set_constraint('conversions_pk', ['crm_id', 'offer_id', 'order_id', 'step', 'click_id'])

    @staticmethod
    def provider_aff_part(provider, affid=False):
        return f""" provider = '{provider}' {f"and affid = '{affid}'" if affid else ''}"""

    def get_scrub_pct(self, offer_id, provider, affid, look_back, step, test_mode=False, crm_id=None, **kwargs):
        res = self.engine.execute(f""" 
            SELECT 
                sum(a.approved) approved, sum(a.saved) as saved            
            from (select approved, saved             
                    from {self.schema}.{self.table}
                    where 
                    offer_id = {offer_id}
                    and {self.provider_aff_part(provider, affid)}
                    and approved > 0
                    and step = {step}
                    and  (is_network = true )
                    {"and test !=  '1'" if not test_mode else ""}
                    {f"and crm_id='{crm_id}'" if crm_id else ""}
                    order by time_stamp desc 
                    limit {look_back}) as a
        """)

        res = list(res)[0]
        if not res[1]:
            return 0
        if not res[0]:
            return 0
        else:
            return res[1] / res[0] * 100

    def get_epc_pct(self, offer_id, provider, affid, trailing_click_count, test_mode=False, crm_id=None, **kwargs):
        qry = f"""
            select  coalesce(sum(coalesce(cpa,0))::numeric / count(*)::numeric,0)
            from (select b.cpa from (select distinct on(click_id) click_id, time_stamp
                  from {self.schema}.clicks
                 where
                    offer_id = '{int(offer_id)}'
                    and affid = '{affid}'
                    and provider = '{provider}'
                    and time_stamp > now()::date  - Interval '10 days'--- - Interval '10 Days'
                  ) a

                left join {self.schema}.conversions b on b.click_id = a.click_id  and step=1 and approved=1 and is_network 
                {'and test = 0 ' if not test_mode else ''}
                {f"and crm_id='{crm_id}'" if crm_id else ""}
                order by a.time_stamp desc
                limit {int(trailing_click_count)}
                ) a;
        """
        # print(qry)
        return self.engine.execute(qry).scalar()

    def traffic_report(self, start_date, end_date, offer_id=False, provider=False, affid=False, crm_id='all',
                       test_mode=False):
        if crm_id != 'all' and not isinstance(crm_id, list):
            crm_id = [crm_id]
        qry = f"""
            SELECT offer_id, provider, affid, step,
                    count(order_id) as orders,
                    sum(approved) as approved,
                    sum(declined) as declined,
                    sum(saved) as saved,
                    sum(coalesce(cpa, 0)) cpa
            from {self.schema}.{self.table}
            where time_stamp::date >= '{start_date}'::date and time_stamp::date <= '{end_date}'::date
                and is_network = true
                {f" and crm_id = ANY(ARRAY{crm_id})" if crm_id != 'all' else ""}
                {f"and offer_id = '{offer_id}'" if offer_id else ""}
                {f"and provider = '{provider}'" if provider else ""}
                {f"and affid = '{affid}'" if affid else ""}
                {"and test != '1'" if not test_mode else ""}

            group by offer_id, provider, affid, step


        """
        # print(qry)
        return pd.read_sql(qry, self.engine)

    def steps_report(self, start_date, end_date, step, offset=0, crm_id='all'):
        qry = f"""
               SELECT  count(order_id) as steps                       
               from {self.schema}.{self.table}
              where time_stamp::date >= '{start_date}'::date -INTERVAL '{offset} days'
                and time_stamp::date <= '{end_date}'::date -INTERVAL '{offset} days'
                  {f" and crm_id = '{crm_id}'" if crm_id and crm_id != 'false' and crm_id != 'all' else ""}
                and step={step}
                and test != '1' 
           """

        res = self.engine.execute(qry).scalar()
        return res

    def is_scrubbed(self, order_id, crm_id):
        val = self.engine.execute(
            f"select saved from {self.schema}.{self.table} where order_id='{int(order_id)}' and crm_id='{crm_id}'").scalar()
        if not val:
            val = 0
        return int(val)



