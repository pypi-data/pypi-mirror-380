import pandas as pd
from models.reports.dependencies import ALERT_PROVIDERS, get_first_dom, now, today, _get_interval_date, get_cast, get_order_by, get_filters, format_group_by




def affid_report(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, **kwargs):
    f_whr = get_filters(filters)
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    group_by = format_group_by(group_by)

    qry = f"""
           SELECT
           {'a.' + ', a.'.join(group_by)},
           a.initial::int initials,
           a.initial_order_total / nullif(a.initial, '0') AS "IAOV $",
           a.pending::int,
           a.pending::numeric / nullif((a.attempted_pending + a.pending), '0')                   AS "pending %%",
           a.cycle_2_pending::numeric / nullif((a.cycle_2_attempted_pending + a.cycle_2_pending), '0') AS "C2 Pending %%",
           a.cycle_3_pending::numeric / nullif((a.cycle_3_attempted_pending + a.cycle_3_pending), '0') AS "C3 Pending %%",
           a.ds_pending::numeric / nullif((a.ds_attempted_pending + a.ds_pending), '0')                AS "DS Pending %%",
           a.cycle_2_ds_pending::numeric / nullif((a.cycle_2_ds_attempted_pending + a.cycle_2_ds_pending), '0')                AS "C2 DS Pending %%",
           a.orders_saves / (nullif((a.orders_saves + a.orders_provider), '0')) AS "scrub %%",
           a.refund::numeric / nullif(a.order_total, '0')                       AS "refund %%",
           a.natural_approval_cf::numeric / nullif(a.attempt_cf, '0')                 AS "natural approval cf %%",
           a.approval_cf::numeric / nullif(a.attempt_cf, '0')                         AS "rebill 1 cf %%",
           a.approval::int                                                           AS "c1 approved",
           a.natural_approval::numeric / nullif(a.attempt, '0')                 AS "natural approval %%",
           a.approval::numeric / nullif(a.attempt, '0')                         AS "rebill 1 %%",
           a.approval2::numeric / nullif(a.attempt2, '0')                         AS "rebill 2+ %%",

           a.retention_cycle_1::numeric / nullif(a.retention_cycle_0, '0')               AS "retention c1 %%",
           a.retention_cycle_2 / nullif(a.retention_cycle_0, '0')                                      AS "Retention C2 %%",
            a.retention_cycle_3 / nullif(a.retention_cycle_0, '0')                                      AS "Retention C3 %%",
           a.chargeback::numeric / nullif(a.all_cycles_approved, '0')           AS "chargeback %%",
           a.chargeback_cost::numeric / nullif(a.order_total, '0')                                       AS "chargeback cost %%",
           a.alert_cost::numeric / nullif(a.order_total, '0')                   AS "alert cost %%",
           (order_total - (a.cpa + processing_cost + product_cost + total_refund + alert_cost + chargeback_cost)) /
           nullif(distinct_customer_id, '0')                                             AS "cltv $",
           (a.cpa::numeric / nullif(a.initial::numeric, '0'))                   AS "average cpa $",
           (order_total - (a.cpa + processing_cost + product_cost + total_refund + alert_cost + chargeback_cost)) /
           nullif(order_total, '0')                                             AS "gm %%",
           nullif(mc_total::numeric,'0')::numeric / nullif(cc_total::numeric, 0)::numeric         AS "mc %%"


            FROM (SELECT
                {'a.' + ', a.'.join(group_by)},
                 sum(order_total_initial)                      AS "initial_order_total",
                 sum(order_total)                              AS "order_total",
                 sum(natural_approval)                         AS "natural_approval",
                 sum(natural_approval_cf)                      AS "natural_approval_cf",
                 sum(attempt)                                  AS "attempt",
                 sum(attempt_cf)                               AS "attempt_cf",
                 sum(attempt2)                                 AS "attempt2",
                 sum(approval)                                 AS "approval",
                 sum(approval_cf)                              AS "approval_cf",
                   sum(approval2)                              AS "approval2",
                 sum(total_refund)                             AS "refund",
                 sum(chargeback)                               AS "chargeback",
                 sum(cycle_0_step_1_approved)                  AS "initial",
                 sum(cycle_0_step_3_approved)                  AS "initial_step_3",
                 sum(cycle_0_r_approved)                       AS "retention_cycle_0",
                 sum(cycle_1_r_approved)                       AS "retention_cycle_1",
                 sum(cycle_2_r_approved)                       AS "retention_cycle_2",
                 sum(cycle_3_r_approved)                       AS "retention_cycle_3",
                 sum(cycle_2_pending)                          AS "cycle_2_pending",
                 sum(cycle_3_pending)                          AS "cycle_3_pending",
                 sum(cycle_2_attempted_pending)                AS "cycle_2_attempted_pending",
                 sum(cycle_3_attempted_pending)                AS "cycle_3_attempted_pending",
                 sum(cpa)                                      AS "cpa",
                 sum(processing_cost)                          AS "processing_cost",
                 sum(product_cost)                             AS "product_cost",
                 sum(total_refund)                             AS "total_refund",
                 sum(alert_cost)                               AS "alert_cost",
                 sum(chargeback_cost)                          AS "chargeback_cost",
                 sum(orders_provider)                          AS "orders_provider",
                 sum(orders_diverted)                          AS "orders_diverted",
                 sum(orders_saves)                             AS "orders_saves",
                 sum( pending )                                AS "pending",
                 sum(distinct_customer_id)                     AS "distinct_customer_id",
                 sum(attempted_pending)                        AS "attempted_pending",
                 sum(ds_attempted_pending)                     AS "ds_attempted_pending",
                 sum(ds_pending)                               AS "ds_pending",
                 sum(cycle_2_ds_attempted_pending)             AS "cycle_2_ds_attempted_pending",
                 sum(cycle_2_ds_pending)                       AS "cycle_2_ds_pending",
                 sum(all_cycles_approved)                      AS "all_cycles_approved",
                 sum(mc_total)                                 AS  "mc_total",
                 sum(cc_total)                                 AS  "cc_total"

          FROM ( SELECT
                             {','.join(group_by)},
                sum(CASE
                        WHEN a.decline_reason IS NULL THEN order_total
                        ELSE '0'::numeric END)::numeric        AS "order_total",
                sum(CASE
                        WHEN a.decline_reason IS NULL AND bc_inferred = '0' AND pp_customer = '0' AND not cap_fill THEN order_total 
                        ELSE '0'::numeric END)::numeric        AS "order_total_initial",
                sum(refund_amount)                             AS "refund_amount",
                sum(amount_refunded_to_date)                   AS "refund_amount_total",
                sum(is_chargeback)                             AS "chargeback",
                count(1)                                       AS "approved_count_order",

                count(CASE
                          WHEN bc_inferred = '0' AND step = '1' AND refund_amount = '0' AND
                               a.decline_reason IS NULL AND pp_customer = '0' AND not cap_fill
                              THEN 1 END)                      AS "cycle_0_step_1_approved",
                count(CASE
                          WHEN bc_inferred = '0' AND step = '3' AND refund_amount = '0' AND
                               a.decline_reason IS NULL AND pp_customer = '0' AND not cap_fill
                              THEN 1 END)                      AS "cycle_0_step_3_approved",
                count(CASE
                          WHEN bc_inferred = '0' AND a.decline_reason IS NULL AND pp_customer = '0' AND not cap_fill
                              AND include_in_r IS TRUE THEN 1 END)                      AS "cycle_0_r_approved",
                count(CASE
                          WHEN bc_inferred = '1' AND not cap_fill AND a.decline_reason IS NULL AND
                               amount_refunded_to_date < order_total AND pp_customer = '0'
                              THEN 1 END)                      AS "cycle_1_r_approved",
                count(CASE
                          WHEN bc_inferred = '2' AND not cap_fill AND a.decline_reason IS NULL AND
                               amount_refunded_to_date < order_total AND pp_customer = '0'
                              THEN 1 END)                      AS "cycle_2_r_approved",
                count(CASE
                          WHEN bc_inferred = '3' AND not cap_fill AND a.decline_reason IS NULL AND
                               amount_refunded_to_date < order_total AND pp_customer = '0'
                              THEN 1 END)                      AS "cycle_3_r_approved",

                count(DISTINCT (CASE
                                    WHEN step = '1' AND not cap_fill AND bc_inferred = '0' AND a.decline_reason IS NULL /*AND
                               pp_customer = '0'*/
                                        THEN customer_id END)) AS "natural_approval_initial",

                count(DISTINCT (CASE
                                    WHEN order_total < '7' AND not cap_fill /*AND
                               pp_customer = '0'*/
                                        THEN customer_id END)) AS "natural_approval_initial_attempt",

                count(CASE
                          WHEN attempt_count = '0' AND bc_inferred = '1' AND not cap_fill AND a.decline_reason IS NULL AND
                               pp_customer = '0'
                              THEN 1 END)                      AS "natural_approval",

                count(CASE
                          WHEN attempt_count = '0' AND bc_inferred = '1' AND a.decline_reason IS NULL AND
                               pp_customer = '0'
                              THEN 1 END)                      AS "natural_approval_cf",
                count(CASE
                          WHEN bc_inferred = '1' AND not cap_fill AND a.decline_reason IS NULL AND pp_customer = '0'
                              THEN 1 END)                      AS "approval",
                count(CASE
                          WHEN bc_inferred = '1' AND a.decline_reason IS NULL AND pp_customer = '0'
                              THEN 1 END)                      AS "approval_cf",
                count(CASE
                          WHEN bc_inferred > '1' AND not cap_fill AND a.decline_reason IS NULL AND pp_customer = '0'
                              THEN 1 END)                      AS "approval2",
                count(CASE
                          WHEN a.decline_reason IS NULL AND not cap_fill
                              THEN 1 END)                      AS "all_cycles_approved",
                sum(CASE
                        WHEN bc_inferred = '1' AND a.decline_reason IS NULL AND pp_customer = '0' AND step = '1' AND not cap_fill
                            THEN order_total / '89.85'::numeric
                        WHEN bc_inferred = '1' AND a.decline_reason IS NULL AND pp_customer = '0' AND step = '2' AND not cap_fill
                            THEN order_total / '87.99'::numeric
                        ELSE '0'::numeric END)                 AS "approval_real",
                count(CASE
                          WHEN attempt_count = '0' AND not cap_fill AND bc_inferred = '1' AND pp_customer = '0'
                              THEN 1 END)                      AS "attempt",
                count(CASE
                          WHEN attempt_count = '0' AND bc_inferred = '1' AND pp_customer = '0'
                              THEN 1 END)                      AS "attempt_cf",
                  count(CASE
                          WHEN attempt_count= '0' AND not cap_fill AND bc_inferred > '1' AND pp_customer = '0'
                              THEN 1 END)                      AS "attempt2",
                sum(cpa::numeric)                              AS "cpa",
                sum(processing_cost)                           AS "processing_cost",
                sum(product_cost)                              AS "product_cost",
                sum(total_refund)                              AS "total_refund",
                sum(alert_cost)                                AS "alert_cost",
                sum(chargeback_cost)                           AS "chargeback_cost",
                sum(CASE
                        WHEN decline_reason IS NULL AND not cap_fill THEN order_diverted::numeric
                        ELSE '0'::numeric END)                 AS "orders_diverted",
                sum(CASE
                        WHEN decline_reason IS NULL AND not cap_fill THEN saves::numeric
                        ELSE '0'::numeric END)                 AS "orders_saves",
                sum(CASE
                        WHEN decline_reason IS NULL AND not cap_fill THEN order_provider::numeric
                        ELSE '0'::numeric END)                 AS "orders_provider",
                sum(step_2_salvaged)                           AS "step_2_salvaged",
                sum(step_1_with_2_salvaged)                    AS "step_1_wtih_2_salvaged",

                count( distinct customer_id)  filter(where cc_type ='Master' and bc_inferred='0' and step='1' and decline_reason is NULL and pp_customer ='0') mc_total,
                count( distinct customer_id)  filter(where bc_inferred='0' and step='1' and decline_reason is NULL and pp_customer='0') cc_total,
                count(CASE
                          WHEN pending IS TRUE AND bc_inferred = '0' AND not cap_fill AND bin_pause = '0' AND extended_date IS NULL
                              THEN '1' END)                    AS "pending",
                count(CASE
                          WHEN pending IS TRUE AND bc_inferred = '1' AND bin_pause = '0' AND extended_date IS NULL AND not cap_fill
                              THEN '1' END)                    AS "cycle_2_pending",
                count(CASE
                          WHEN pending IS TRUE AND bc_inferred = '2' AND bin_pause = '0' AND extended_date IS NULL AND not cap_fill
                              THEN '1' END)                    AS "cycle_3_pending",
                count(CASE
                          WHEN d_pending IS TRUE AND bc_inferred = '0' AND bin_pause = '0' AND extended_date IS NULL AND not cap_fill
                              THEN '1' END)                    AS "ds_pending",
                count(CASE
                          WHEN d_pending IS TRUE AND bc_inferred = '1' AND bin_pause = '0' AND extended_date IS NULL AND not cap_fill
                              THEN '1' END)                    AS "cycle_2_ds_pending",
                count(CASE
                          WHEN pending IS NULL AND retry_attempt_count IS NOT NULL AND decline_reason IS NULL AND
                               bc_inferred = '0' AND bin_pause = '0' AND extended_date IS NULL AND not cap_fill
                              THEN '1' END)                    AS "attempted_pending",
                count(CASE
                          WHEN pending IS NULL AND retry_attempt_count IS NOT NULL AND decline_reason IS NULL AND
                               bc_inferred = '1' AND bin_pause = '0' AND extended_date IS NULL AND not cap_fill
                              THEN '1' END)                    AS "cycle_2_attempted_pending",
                count(CASE
                          WHEN pending IS NULL AND retry_attempt_count IS NOT NULL AND decline_reason IS NULL AND
                               bc_inferred = '2' AND bin_pause = '0' AND extended_date IS NULL AND not cap_fill
                              THEN '1' END)                    AS "cycle_3_attempted_pending",
                count(CASE
                          WHEN d_pending IS NULL AND retry_attempt_count IS NOT NULL AND retry_attempt_count > '0' AND
                               decline_reason IS NULL AND bc_inferred = '0' AND bin_pause = '0' AND
                               extended_date IS NULL AND not cap_fill
                              THEN '1' END)                    AS "ds_attempted_pending",
                count(CASE
                          WHEN d_pending IS NULL AND retry_attempt_count IS NOT NULL AND retry_attempt_count > '0' AND
                               decline_reason IS NULL AND bc_inferred = '1' AND bin_pause = '0' AND
                               extended_date IS NULL AND not cap_fill
                              THEN '1' END)                    AS "cycle_2_ds_attempted_pending",
                count(DISTINCT customer_id)                    AS "distinct_customer_id"

                      FROM reporting.cpa_orders AS "a"

                      WHERE a.acquisition_date BETWEEN '{sdate}' AND '{edate}'
                      {"and cc_type!='TESTCARD'" if not inc_test_cc else ''}
                      {f_whr}
                      GROUP BY {','.join(group_by)} ) AS "a"
        GROUP BY {'a.' + ', a.'.join(group_by)} ) AS "a"
        ORDER BY  {get_order_by(group_by, order_by)};
    """
    #   print(qry)

    res = pd.read_sql(
        qry,
        db.engine
    )
    return res


grouper_cols = []

