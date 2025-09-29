import pandas as pd
from models.reports.dependencies import ALERT_PROVIDERS, get_first_dom, now, today, _get_interval_date, get_cast, get_order_by, get_filters, format_group_by



def continuity_report(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, **kwargs):
    f_whr = get_filters(filters)
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    _group_by = ','.join(format_group_by(group_by))

    qry = f"""
            select {_group_by},


           count(approval)
           FILTER ( WHERE retry_attempt_count = '0' )                                                                     AS "natural_recurring_count",
           count(approval) FILTER ( WHERE retry_attempt_count = '0' AND bc_inferred =  '1' )                              AS "c1_recurring_count",
           coalesce(round(sum(approval) FILTER ( WHERE bc_inferred = '1' AND retry_attempt_count = '0' ), 0),
                    '0')                                                                                                  AS "c1_projected_count",
           avg(approval)
           FILTER ( WHERE bc_inferred = '1' AND retry_attempt_count = '0' )                                               AS "c1_projected_approval %%",
           coalesce(round(sum(approval) FILTER ( WHERE bc_inferred > '1' AND retry_attempt_count = '0' ), 0),
                    '0')                                                                                                  AS "c2+_projected_count",
           avg(approval)
           FILTER ( WHERE bc_inferred > '1' AND retry_attempt_count = '0' )                                               AS "c2+_projected_approval %%",
           coalesce(round(sum(approval) FILTER ( WHERE retry_attempt_count = '0' ), 0),
                    '0')                                                                                                  AS "natural_projected_count",
           avg(approval) FILTER ( WHERE retry_attempt_count = '0' )                                                       AS "natural_projected_approval %%",
           coalesce(round(count(approval) FILTER ( WHERE retry_attempt_count > '0' ), 0),
                    '0')                                                                                                  AS "decline_recurring_count",
           coalesce(round(avg(retry_attempt_count::numeric) FILTER ( WHERE retry_attempt_count > '0' ), 0),
                    '0')                                                                                                  AS "average_decline_attempt",
           avg(approval) FILTER ( WHERE retry_attempt_count > '0' )                                                       AS "decline_approval %%",
           coalesce(round(sum(approval) FILTER ( WHERE retry_attempt_count > '0' ), 0),
                    '0')                                                                                                  AS "decline_approved_count",
           coalesce(round((avg(approval) * sum(order_total))::numeric, 2),
                    '0')                                                                                                  AS "projected_revenue $",
           coalesce(round((sum(order_total))::numeric, 2), '0')                                                           AS "recurring_revenue $",
           coalesce(round((sum(order_total) FILTER ( WHERE retry_attempt_count = '0' ))::numeric, 2),
                    '0')                                                                                                  AS "natural_recurring_revenue $"
            FROM reporting.continuity
            WHERE next_cycle_date > '{now()}'::date
              AND retry_attempt_count < '6'
                {f_whr}

            GROUP BY  {_group_by}
            ORDER BY {','.join(order_by) if order_by else _group_by}
    """
    # print(qry)

    return pd.read_sql(
        qry,
        db.engine
    )

