import pandas as pd
from models.reports.dependencies import ALERT_PROVIDERS, get_first_dom, now, today, _get_interval_date, get_cast, get_order_by, get_filters, format_group_by


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
