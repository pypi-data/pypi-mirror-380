import pandas as pd
from models.reports.dependencies import ALERT_PROVIDERS, get_first_dom, now, today, _get_interval_date, get_cast, get_order_by, get_filters, format_group_by


def mtd_report(db, group_by=[], reporting_query=False, filters={}, order_by=False, **kwargs):
    filters_allowed = ['crm_id']
    f_whr = get_filters(filters)
    group_by = format_group_by(group_by)
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    alert_cols = ','.join([f"{a}_cost_$" for a in ALERT_PROVIDERS])
    refund_cols = ','.join([f"{a}_refunds_$" for a in ALERT_PROVIDERS])
    alert_block = ', \n'.join(
        [f"""coalesce((sum(value) FILTER( WHERE type='alert' and alert_provider='{a}')),0) as "{a}_cost_$" """ for a in
         ALERT_PROVIDERS])
    refund_block = ', \n'.join(
        [f"""coalesce((sum(value) FILTER( WHERE type='refund' and alert_provider='{a}')),0) as "{a}_refunds_$" """ for a
         in ALERT_PROVIDERS])

    qry = f"""
      SELECT {'a.' + ', a.'.join(group_by)},
       cycle_0                                               AS "cycle_0_$",
       cycle_1                                               AS "cycle_1_$",
       cycle_2                                               AS "cycle_2_$",
       cycle_3                                               AS "cycle_3_$",
       revenue_$,
       {refund_cols},
       cs_refunds_$,
       total_refunds_$,
       {alert_cols},
       alerts_$,
       cb_count,
       cb_costs_$,
       cb_amount_$,
       reserves_$,
       processing_cost_$,
       transaction_cost_$,
       cpa_$,
       total_$,
       coalesce((a.total_$ / nullif(a.revenue_$, '0')), '0') AS "gm_%%"
FROM (SELECT  {','.join(group_by)},
             --coalesce(sum(value) FILTER ( WHERE type = 'revenue' AND step = '1' AND bc_inferred = '0' AND value > '0' ), '0') AS "cycle_0_step_1",
             coalesce(sum(value) FILTER ( WHERE type = 'revenue' AND bc_inferred = '0' AND value > '0' ),
                      '0')                                                          AS "cycle_0",
             coalesce(sum(value) FILTER ( WHERE type = 'revenue' AND bc_inferred = '1' AND value > '0' ),
                      '0')                                                          AS "cycle_1",
             coalesce(sum(value) FILTER ( WHERE type = 'revenue' AND bc_inferred = '2' AND value > '0' ),
                      '0')                                                          AS "cycle_2",
             coalesce(sum(value) FILTER ( WHERE type = 'revenue' AND bc_inferred = '3' AND value > '0' ),
                      '0')                                                          AS "cycle_3",             
             coalesce((sum(value) FILTER ( WHERE type = 'revenue' )), '0')          AS "revenue_$",
             {alert_block},
             {refund_block},
             coalesce((sum(value) FILTER ( WHERE type = 'refund' and alert_provider is NULL )), '0')           AS "cs_refunds_$",
             coalesce((sum(value) FILTER ( WHERE type = 'refund' )), '0')           AS "total_refunds_$",
             coalesce((sum(value) FILTER ( WHERE type = 'alert' )), '0')            AS "alerts_$",
             coalesce((count(distinct order_id) FILTER ( WHERE type = 'cb_cost' )), '0')          AS "cb_count",
             coalesce((sum(value) FILTER ( WHERE type = 'cb_cost' )), '0')          AS "cb_costs_$",

             coalesce((sum(value) FILTER ( WHERE type = 'cb_amount' )), '0')          AS "cb_amount_$",
             coalesce((sum(value) FILTER ( WHERE type = 'reserves' )), '0')         AS "reserves_$",
             coalesce((sum(value) FILTER ( WHERE type = 'processing_cost' )), '0')  AS "processing_cost_$",
             coalesce((sum(value) FILTER ( WHERE type = 'transaction_cost' )), '0') AS "transaction_cost_$",
             coalesce((sum(value) FILTER ( WHERE type = 'cpa' )), '0')              AS "cpa_$",
             coalesce((sum(value)), '0')                                            AS "total_$"
      FROM reporting.ui_revenue_transactions
      WHERE date >= '{sdate}'::date AND date <= '{edate}'::date
      {f_whr}
      GROUP BY  {','.join(group_by)}
       -- corporation_name, processor, mid_id
      ) AS "a"
     ORDER BY  {get_order_by(group_by, order_by)}

--a.corporation_name, a.processor, a.mid_id;
    """
    # print(qry)
    try:
        return pd.read_sql(qry, db.engine)
    except:
        return pd.read_sql(qry.replace('mid_number', 'mid_id'), db.engine)


