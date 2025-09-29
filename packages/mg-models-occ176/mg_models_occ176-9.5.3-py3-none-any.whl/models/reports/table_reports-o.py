import pandas as pd
from .dependencies import now, today, _get_interval_date, get_cast, get_order_by, get_filters, format_group_by

ALERT_PROVIDERS = ['ethoca', 'rdr']


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
                  sum(order_total_initial)                  AS "initial_order_total",
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
                 sum( pending ) AS "pending",
                 sum(distinct_customer_id) as "distinct_customer_id",
                 sum(attempted_pending)                        AS "attempted_pending",
                 sum(ds_attempted_pending)                     AS "ds_attempted_pending",
                 sum(ds_pending)                                AS "ds_pending",
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


def bin_report(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, **kwargs):
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    group_by = format_group_by(group_by)
    f_whr = get_filters(filters, 'a.')
    qry = f"""
     WITH
    blocked_bins AS (
        SELECT crm_id, bin,COALESCE(effective_from, '1999-01-01 00:00:00.00000') AS effective_from, enabled, block_pct, enable_shave,
        (CASE WHEN enabled THEN 'block'  WHEN enable_shave THEN 'shave' ELSE 'normal' END) AS bin_category
        FROM ui_54407332_bins.bin_blacklist
        where crm_id in (select crm_id from ui_54407332_clients.instance_data where not coalesce(archived, FALSE))
    ),
        cpa_orders_filtered AS (
        SELECT
            --added group by to select columns required in aggregations
            {'a.' + ', a.'.join(group_by)},
            b.bin_category,
            (COALESCE((1-(b.block_pct / 100)), 1))::numeric AS block_pct,
            CASE WHEN decline_reason IS NULL THEN order_total ELSE 0::numeric::real END AS order_total,
            refund_amount,
            amount_refunded_to_date,
            is_chargeback,
            CASE WHEN bc_inferred = 0::numeric AND step = 1::numeric AND refund_amount = 0::real AND decline_reason IS NULL THEN 1 ELSE NULL::integer END AS cycle_0_step_1_approved,
            CASE WHEN bc_inferred = 0::numeric AND decline_reason IS NULL AND include_in_r THEN 1 ELSE NULL::integer END AS cycle_0_r_approved,
            CASE WHEN bc_inferred = 1::numeric AND decline_reason IS NULL AND amount_refunded_to_date < order_total THEN 1 ELSE NULL::integer END AS cycle_1_r_approved,
            CASE WHEN bc_inferred = 2::numeric AND decline_reason IS NULL AND amount_refunded_to_date < order_total THEN 1 ELSE NULL::integer END AS cycle_2_r_approved,
            CASE WHEN step = 1::numeric AND bc_inferred = 0::numeric AND decline_reason IS NULL THEN customer_id ELSE NULL::integer END AS natural_approval_initial_customer,
            CASE WHEN order_total < 7::real THEN customer_id ELSE NULL::integer END AS natural_approval_initial_attempt_customer,
            CASE WHEN attempt_count = 0 AND bc_inferred = 1::numeric AND decline_reason IS NULL THEN 1 ELSE NULL::integer END AS natural_approval,
            CASE WHEN bc_inferred = 1::numeric AND decline_reason IS NULL THEN 1 ELSE NULL::integer END AS approval,
            CASE WHEN decline_reason IS NULL THEN 1 ELSE NULL::integer END AS all_cycles_approved,
            CASE WHEN bc_inferred = 1::numeric AND decline_reason IS NULL AND step = 1::numeric THEN order_total / 89.85::double precision
                WHEN bc_inferred = 1::numeric AND decline_reason IS NULL AND step = 2::numeric THEN order_total / 87.99::double precision
                ELSE 0::numeric::double precision END AS approval_real,
            CASE WHEN attempt_count = 0 AND bc_inferred = 1::numeric THEN 1 ELSE NULL::integer END AS attempt,
            CASE WHEN order_diverted = 1 THEN 0::numeric ELSE cpa END AS cpa,
            processing_cost,
            product_cost,
            total_refund,
            alert_cost,
            chargeback_cost,

            CASE WHEN decline_reason IS NULL THEN order_diverted ELSE 0::numeric END AS orders_diverted,
            CASE WHEN decline_reason IS NULL AND block_customer = 1 THEN block_customer ELSE 0::numeric END AS orders_block,
            CASE WHEN decline_reason IS NULL THEN saves ELSE 0::numeric END AS orders_saves,
            CASE WHEN decline_reason IS NULL THEN order_provider ELSE 0::numeric END AS orders_provider,
            step_2_salvaged,
            step_1_with_2_salvaged,
            CASE WHEN pending AND bc_inferred = 0::numeric AND extended_date IS NULL THEN 1 ELSE NULL::integer END AS pending,
            CASE WHEN pending AND bc_inferred = 1::numeric AND extended_date IS NULL THEN 1 ELSE NULL::integer END AS cycle_2_pending,
            CASE WHEN d_pending AND bc_inferred = 0::numeric AND extended_date IS NULL THEN 1 ELSE NULL::integer END AS ds_pending,
            CASE WHEN pending IS NULL AND retry_attempt_count IS NOT NULL AND decline_reason IS NULL AND bc_inferred = 0::numeric AND extended_date IS NULL THEN 1 ELSE NULL::integer END AS attempted_pending,
            CASE WHEN pending IS NULL AND retry_attempt_count IS NOT NULL AND decline_reason IS NULL AND bc_inferred = 1::numeric AND extended_date IS NULL THEN 1 ELSE NULL::integer END AS cycle_2_attempted_pending,
            CASE WHEN d_pending IS NULL AND retry_attempt_count IS NOT NULL AND retry_attempt_count > 0 AND decline_reason IS NULL AND bin_pause = 0::numeric AND extended_date IS NULL THEN 1 ELSE NULL::integer END AS ds_attempted_pending,
            customer_id
        FROM reporting.cpa_orders AS a
        LEFT JOIN blocked_bins As b ON b.crm_id = a.crm_id AND b.bin = a.bin
        WHERE acquisition_date >= '{sdate}'::timestamp without time zone
        AND acquisition_date <= '{edate}'::timestamp without time zone
        --added where
        AND a.crm_id in (select crm_id from ui_54407332_clients.instance_data where not coalesce(archived, FALSE))
    ), cpa_orders_aggregated AS (
        SELECT
            --added group by
            {'a.' + ', a.'.join(group_by)},
            coalesce(a.bin_category, 'normal') as bin_category,
            sum(order_total)::numeric as order_total,
            sum(natural_approval) as natural_approval,
            count(DISTINCT natural_approval_initial_customer) as natural_approval_initial,
            count(DISTINCT natural_approval_initial_attempt_customer) as natural_approval_initial_attempt,
            sum(attempt) as attempt,
            sum(approval) as approval,
            sum(all_cycles_approved) as all_cycles_approved,
            sum(approval_real) as approval_real,
            sum(refund_amount) + sum(amount_refunded_to_date) AS refund,
            sum(is_chargeback) AS chargeback,
            sum(cycle_0_step_1_approved) AS initial,
            sum(cycle_0_r_approved) AS retention_cycle_0,
            sum(cycle_1_r_approved) AS retention_cycle_1,
            sum(cycle_2_r_approved) AS retention_cycle_2,
            sum(cpa) AS cpa,
            sum(processing_cost) AS processing_cost,
            sum(product_cost) AS product_cost,
            sum(total_refund)  total_refund,
            sum(alert_cost) AS alert_cost,
            sum(chargeback_cost)::numeric AS chargeback_cost,
            sum(orders_provider) AS orders_provider,
            sum(orders_diverted) AS orders_diverted,
            sum(orders_saves) AS orders_saves,
            sum(pending) AS pending,
            sum(cycle_2_pending) AS cycle_2_pending,
            sum(ds_pending) AS ds_pending,
            sum(attempted_pending) AS attempted_pending,
            sum(cycle_2_attempted_pending) AS cycle_2_attempted_pending,
            sum(ds_attempted_pending) AS ds_attempted_pending,
            COUNT(DISTINCT customer_id) AS distinct_customer_id,
            max(block_pct::numeric) AS block_pct
        FROM cpa_orders_filtered AS a

        --added group by
        GROUP BY {'a.' + ', a.'.join(group_by)}, coalesce(a.bin_category, 'normal')

    )
    SELECT
        --added group by to add aggregated columns
        {'a.' + ', a.'.join(group_by)},
        a.bin_category,
        CASE
            WHEN a.bin LIKE '4%%' THEN 'VISA'
            WHEN a.bin LIKE '5%%' THEN 'MASTER'
            WHEN a.bin LIKE '6%%' THEN 'DISCOVER'
            ELSE 'MAP'
        END AS "Card",
        a.initial,
        a.natural_approval_initial / NULLIF(a.natural_approval_initial_attempt, 0) AS "Natural Approval Initial %%",
        a.pending,
        a.pending / NULLIF(a.attempted_pending + a.pending, 0) AS "Pending %%",
        a.ds_pending / NULLIF(a.ds_attempted_pending + a.ds_pending, 0) AS "DS Pending %%",
        a.approval AS "C1 Approved",
        a.natural_approval / NULLIF(a.attempt, 0) AS "Natural Approval C1 %%",
        a.approval_real / NULLIF(a.attempt, 0) AS "Rebill C1 %%",
        a.retention_cycle_1 / NULLIF(a.retention_cycle_0, 0) AS "Retention C1 %%",
        a.cycle_2_pending / NULLIF(a.cycle_2_attempted_pending + a.cycle_2_pending, 0) AS "Cycle 2 Pending %%",
        a.retention_cycle_2 / NULLIF(a.retention_cycle_0, 0) AS "Retention C2 %%",
        a.refund / NULLIF(a.order_total, 0) AS "Refund %%",
        a.chargeback,
        a.chargeback / NULLIF(a.all_cycles_approved, 0) AS "CB %%",
        a.chargeback_cost / NULLIF(a.order_total, 0) AS "CB Cost %%",
        a.alert_cost / NULLIF(a.order_total, 0) AS "Alert Cost %%",
        a.orders_saves / NULLIF(a.orders_saves + a.orders_provider, 0) AS "Scrub %%",
        (a.order_total - (a.cpa + a.processing_cost + a.product_cost + a.total_refund + a.alert_cost + a.chargeback_cost )) / NULLIF(a.order_total, 0) AS "GM %%",
        (a.order_total - (a.cpa + a.processing_cost + a.product_cost + a.total_refund + a.alert_cost  + a.chargeback_cost)) / NULLIF(a.distinct_customer_id, 0) AS "CLTV $",
        (a.order_total - ((block_pct * a.cpa) + a.processing_cost + a.product_cost + a.total_refund + a.alert_cost + a.chargeback_cost)) / NULLIF(a.order_total, 0) AS "GM no Block %%",
        (a.order_total - ((block_pct * a.cpa) + a.processing_cost + a.product_cost + a.total_refund + a.alert_cost + a.chargeback_cost)) / NULLIF(a.distinct_customer_id, 0) AS "CLTV no Block $"

    FROM cpa_orders_aggregated a

    --added where
    WHERE a.initial > 0 {f_whr}
    --added both where and group by
    ORDER BY a.initial DESC LIMIT 1000
    """

    # print(qry)

    ret = pd.read_sql(qry, db.engine)
    return ret


def get_first_dom():
    return now().replace(day=1).date()


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


def continuity_report(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, **kwargs):
    f_whr = get_filters(filters)
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    _group_by = ','.join(format_group_by(group_by))

    qry = f"""
            select {_group_by},


           count(approval)
           FILTER ( WHERE retry_attempt_count = '0' )                                       AS "natural_recurring_count",
           count(approval) FILTER ( WHERE retry_attempt_count = '0' AND bc_inferred =  '1' )               AS "c1_recurring_count",
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


def inactive_report(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, **kwargs):
    f_whr = get_filters(filters, translate={'corp': 'corporation_name', 'is_cascade': 'is_dead_mid_cascade'},
                        prefix="WHERE")
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    qry = f"""
        SELECT c.corporation_name,
       b.mid_number,
       a.destination_gateway::int::text                AS gateway_id,
       a.crm_id,
       b.close_date::text,
       d.enabled::TEXT as "is_enabled",
       c.daily_available                    AS daily_available_cap,
       c.monthly_available                  AS monthly_available_cap,
       c.daily_transaction_cap - c.used_dtc AS available_daily_transaction_cap,
       e.available_tc                       AS available_trailing30_cap,
       a.total_inactive::int::text,
       a.dead_mid_cascade::int::text,
       a.total_inactive_visa::int::text,
       a.total_inactive_master::int::text,
       a.total_inactive_discover::int::text

        FROM (SELECT a_1.crm_id,
             a_1.destination_gateway,
             count(1)                                                       AS total_inactive,
             count(1) FILTER (WHERE a_1.is_dead_mid_cascade = '1'::numeric)::int AS dead_mid_cascade,
             count(1) FILTER (WHERE a_1.cc_type = 'master'::text)           AS total_inactive_master,
             count(1) FILTER (WHERE a_1.cc_type = 'visa'::text)             AS total_inactive_visa,
             count(1) FILTER (WHERE a_1.cc_type = 'discover'::text)         AS total_inactive_discover
      FROM processing.recurring_orders a_1
      WHERE a_1.active IS FALSE
        AND a_1.retry_date IS NULL
      GROUP BY a_1.crm_id, a_1.destination_gateway) a
         JOIN (SELECT DISTINCT ON (steps.crm_id, steps.gateway_id) steps.crm_id,
                                                                   steps.gateway_id,
                                                                   steps.mid_number,
                                                                   steps.mid_id,
                                                                   steps.step,
                                                                   steps.close_date
               FROM ui_54407332_clients.steps) b ON b.crm_id = a.crm_id AND b.gateway_id = a.destination_gateway
         JOIN processing.cap c ON c.mid_id = b.mid_id::numeric AND c.step = b.step
         JOIN  (SELECT mid_id,step, available_tc from processing.trailing_cap) e on e.mid_id=b.mid_id and e.step=b.step
         JOIN ui_54407332_clients.gateway_settings d
              ON d.crm_id = a.crm_id AND d.gateway_id::numeric = a.destination_gateway
-- {f_whr}
        ORDER BY c.corporation_name, b.mid_number, a.destination_gateway, a.crm_id;
    """

    return pd.read_sql(qry, db.engine)


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
       from ( select a.*, e.corporation_name, e.corp_id, d.processor, d.mid_id, c.mcc,  c.mid_number, b.cc_type

       from (select crm_id, order_id, retry_attempt_count as attempt, decline_reason, bc_inferred 
      from augmented_data.order_cycles
      where month_date >= '{sdate}'::date
        and month_date <= '{edate}'::date) a
         inner join (select crm_id, order_id, gateway_id, cc_type
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