import pandas as pd
from models.reports.dependencies import ALERT_PROVIDERS, get_first_dom, now, today, _get_interval_date, get_cast, get_order_by, get_filters, format_group_by


def approval_report(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, **kwargs):
    f_whr = get_filters(filters, translate={'corp': 'corporation_name', 'is_cascade': 'is_dead_mid_cascade'},
                        prefix="WHERE")
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    grp = format_group_by(group_by)
    grp = ','.join(grp)
    qry = f""" select * from(
        select {grp},

       count(1) "order count",
       coalesce(nullif(count(1) filter (where decline_reason is null)::numeric,0) / count(1)::numeric ,0) "approval%%",
       coalesce(nullif(count(1) filter (where decline_reason is null and bc_inferred = '0')::numeric,0) / count(1) filter (where  bc_inferred = '0')::numeric ,0) "approval C0%%",
       coalesce(nullif(count(1) filter (where decline_reason is null and bc_inferred = '1')::numeric,0) / count(1) filter (where  bc_inferred = '1')::numeric ,0) "approval C1%%",
       coalesce(nullif(count(1) filter (where decline_reason is null and bc_inferred >= '2')::numeric,0) / count(1) filter (where bc_inferred >= '2')::numeric ,0) "approval C2+%%"
       from ( select a.*, e.corporation_name, e.corp_id, d.processor, d.mid_id, c.mcc,  c.mid_number, b.cc_type, b.affid, b.provider

       from (select crm_id, order_id, retry_attempt_count as attempt, decline_reason, bc_inferred 
      from augmented_data.order_cycles
      where month_date >= '{sdate}'::date
        and month_date <= '{edate}'::date) a
         inner join (select crm_id, order_id, gateway_id, cc_type, affid, c1 as "provider"
                     from crm_global.orders
                     where month_date >= '{sdate}'::date and month_date <= '{edate}'::date) b
                    on b.crm_id = a.crm_id and b.order_id = a.order_id
         inner join (select gateway_id, mid_number, mid_id, crm_id, mcc from ui_54407332_clients.steps) c
                    on c.crm_id = b.crm_id and c.gateway_id = b.gateway_id
         inner join (select mid_id, processor, corp_id from ui_54407332_clients.mids) d on d.mid_id = c.mid_id
        inner join (select corporation_name, corp_id from ui_54407332_clients.corps ) e on e.corp_id = d.corp_id

        ) a 
        {f_whr}
         group by {grp}
        ) a
    """

    return pd.read_sql(qry, db.engine)


def approval_report_2(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, **kwargs):
    f_whr = get_filters(filters, translate={'corp': 'corporation_name', 'is_cascade': 'is_dead_mid_cascade'},
                        prefix="AND")
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    grp = format_group_by(group_by)
    grp = ','.join(grp)
    qry = f""" select *, round(coalesce(approved::numeric/nullif(total, '0')::numeric, 0),2) as "approval%%" from(
        select {grp}, sum(approved) approved, count(1)    total
            from (select crm_id,
                   order_id,
                   bc_inferred::int billing_cycle,
                   attempt_count::int,
                   campaign_class,
                   mid_number,
                   processor,
                   offer,
                   gateway_id,
                   cc_type,
                   cc_first_6,
                   approved,
                   month_date
            from reporting.initials_attempts
            where attempt_count < 6 and month_date >= '{sdate}'::date and month_date <= '{edate}'::date
                  {f_whr}

            UNION ALL
            select a.crm_id,
                   a.order_id::int,
                   bc_inferred::int billing_cycle,
                   (attempt_count + 1)::int attempt_count,
                   campaign_class,
                   mid_number,
                   processor,
                   offer,
                   b.gateway_id,
                   cc_type,
                   b.cc_first_6,
                   (case when a.decline_reason is null then 1 else 0 end) as approved,
                   month_date
            from reporting.cpa_orders a
                     inner join (select crm_id, order_id, gateway_id,  cc_first_6, month_date from crm_global.orders where month_date >= '{edate}'::date) b on b.crm_id = a.crm_id and b.order_id::int = a.order_id::int
            where attempt_count < 6
              and bc_inferred > 0
              and acquisition_date >= '{sdate}'::date and acquisition_date <= '{edate}'::date
               {f_whr}
            ) a
      group by {grp}
      order by {grp}) a
      """

    return pd.read_sql(qry, db.engine)

from DataFactory import sqlinterface as se


    
