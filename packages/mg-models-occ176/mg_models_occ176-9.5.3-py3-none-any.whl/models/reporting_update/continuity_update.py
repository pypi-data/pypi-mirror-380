
def run(db, *crm_ids, work_mem='20GB'):
    if not len(crm_ids):
        raise ValueError('Must include pass at least 1 crm_id')
    _in_crm_ids = "','".join(crm_ids)
    conn = db.engine.raw_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"SET LOCAL WORK_MEM = '{work_mem}'")
        cur.execute(
            f"""
                DROP TABLE IF EXISTS product_is_recurring;
                    CREATE TEMP TABLE product_is_recurring ON COMMIT DROP AS (SELECT DISTINCT a.crm_id, a.product::integer AS "product"
                                                                              FROM ((SELECT DISTINCT crm_id, charge_product_id AS "product"
                                                                                     FROM ui_54407332_offers.offer_globals
                                                                                     WHERE is_rebill IS TRUE)
                                                                                    UNION ALL
                                                                                    (SELECT DISTINCT crm_id, rebill_product_id AS "product"
                                                                                     FROM ui_54407332_offers.offer_globals
                                                                                     WHERE is_rebill IS TRUE)
                                                                                    UNION ALL
                                                                                    (SELECT DISTINCT crm_id, trial_product_id AS "product"
                                                                                     FROM ui_54407332_offers.offer_globals
                                                                                     WHERE is_rebill IS TRUE)
                                                                                    UNION ALL
                                                                                    (SELECT DISTINCT crm_id, main_product_id AS "product"
                                                                                     FROM ui_54407332_offers.offer_globals
                                                                                     WHERE is_rebill IS TRUE)) AS "a"
                                                                              WHERE a.product IS NOT NULL);
                    
                    DROP TABLE IF EXISTS orders_filtered;
                    CREATE TEMP TABLE orders_filtered ON COMMIT DROP AS (SELECT a.crm_id,
                                                                                a.order_id,
                                                                                a.time_stamp,
                                                                                a.gateway_id,
                                                                                b.acquisition_date,
                                                                                d.campaign_id,
                                                                                a.decline_reason,
                                                                                b.bc_inferred,
                                                                                b.attempt_count,
                                                                                d.class,
                                                                                CASE
                                                                                    WHEN d.class = 'prepaid' OR d.class = 'block' THEN TRUE::boolean
                                                                                    ELSE FALSE::boolean END AS "prepaid",
                                                                                e.vertical,
                                                                                c.step,
                                                                                a.main_product_id,
                                                                                CASE
                                                                                    WHEN lower(a.cc_type) = 'mastercard' THEN 'master'
                                                                                    ELSE lower(cc_type) END AS "cc_type",
                                                                                a.amount_refunded_to_date,
                                                                                a.order_total,
                                                                                a.is_chargeback,
                                                                                b.parent_id,
                                                                                b.ancestor_id,
                                                                                b.first_affiliate
                                                                         FROM crm_global.orders AS "a"
                                                                                  INNER JOIN augmented_data.order_cycles AS "b"
                                                                                             ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                                                                                  INNER JOIN augmented_data.order_cycles AS "c"
                                                                                             ON c.crm_id = a.crm_id AND c.order_id = b.ancestor_id
                                                                                  INNER JOIN ui_54407332_offers.campaigns AS "d"
                                                                                             ON d.crm_id = a.crm_id AND d.campaign_id = c.campaign_id
                                                                                  INNER JOIN ui_54407332_offers.offers AS "e" ON e.offer_id = d.offer_id);
                    
                    DROP TABLE IF EXISTS orders_provider;                                               
                    CREATE TEMP TABLE orders_provider ON COMMIT DROP AS (SELECT DISTINCT ON ( crm_id, order_id ) crm_id, order_id, c1
                                                                         FROM crm_global.orders
                                                                         WHERE c1 IS NOT NULL);
                    DROP TABLE IF EXISTS orders_filtered_2;
                    CREATE TEMP TABLE orders_filtered_2 ON COMMIT DROP AS (SELECT a.crm_id,
                                                                                  a.order_id,
                                                                                  a.time_stamp,
                                                                                  a.gateway_id,
                                                                                  a.acquisition_date,
                                                                                  a.campaign_id,
                                                                                  a.decline_reason,
                                                                                  a.bc_inferred,
                                                                                  a.attempt_count,
                                                                                  a.class,
                                                                                  a.prepaid,
                                                                                  a.vertical,
                                                                                  a.step,
                                                                                  a.cc_type,
                                                                                  a.amount_refunded_to_date,
                                                                                  a.order_total,
                                                                                  a.is_chargeback,
                                                                                  a.parent_id,
                                                                                  a.ancestor_id,
                                                                                  a.first_affiliate,
                                                                                  g.processor,
                                                                                  h.c1 AS "provider"
                                                                           FROM orders_filtered AS "a"
                                                                                    INNER JOIN (SELECT DISTINCT ON ( crm_id, gateway_id ) crm_id,
                                                                                                                                          gateway_id,
                                                                                                                                          mid_id,
                                                                                                                                          CASE
                                                                                                                                              WHEN close_date IS NULL
                                                                                                                                                  THEN now() + interval '1 day'
                                                                                                                                              ELSE close_date END AS "close_date"
                                                                                                FROM ui_54407332_clients.steps) AS "f"
                                                                                               ON f.crm_id = a.crm_id AND f.gateway_id = a.gateway_id
                                                                                    INNER JOIN ui_54407332_clients.mids AS "g" ON g.mid_id = f.mid_id
                                                                                    INNER JOIN product_is_recurring pir
                                                                                               ON a.crm_id = pir.crm_id AND
                                                                                                  pir.product::integer =
                                                                                                  a.main_product_id::integer
                                                                                    INNER JOIN orders_provider AS "h"
                                                                                               ON h.crm_id = a.crm_id AND h.order_id = a.ancestor_id
                                                                           WHERE a.time_stamp < f.close_date );
                    DROP TABLE IF EXISTS order_total_average;
                    CREATE TEMP TABLE order_total_average ON COMMIT DROP AS (SELECT a.crm_id,
                                                                                    a.bc_inferred,
                                                                                    a.attempt_count,
                                                                                    avg(a.order_total) AS "order_total"
                                                                             FROM orders_filtered AS "a"
                                                                             WHERE a.decline_reason IS NULL
                                                                               AND ((a.time_stamp > now() - interval '10 days') OR
                                                                                    (a.attempt_count > '0' AND a.time_stamp > now() - interval '30 days'))
                                                                             GROUP BY a.crm_id, a.bc_inferred, a.attempt_count); 
                    DROP TABLE IF EXISTS vertical_stats;
                    CREATE TEMP TABLE vertical_stats ON COMMIT DROP AS (SELECT cc_type,
                                                                               prepaid,
                                                                               vertical,
                                                                               bc_inferred,
                                                                               attempt_count,
                                                                               count(1) AS "sample",
                                                                               coalesce(((count(1) FILTER ( WHERE decline_reason IS NULL ))::numeric /
                                                                               nullif(count(DISTINCT parent_id), '0')), '0'::numeric)  AS "approval"
                                                                        FROM orders_filtered_2
                                                                        WHERE bc_inferred > '0'
                                                                          AND attempt_count >= '0'
                                                                        GROUP BY cc_type, prepaid, vertical, bc_inferred, attempt_count );
                    DROP TABLE IF EXISTS crm_stats;
                    CREATE TEMP TABLE crm_stats ON COMMIT DROP AS (SELECT cc_type,
                                                                               prepaid,
                                                                               crm_id,
                                                                               bc_inferred,
                                                                               attempt_count,
                                                                               count(1) AS "sample",
                                                                               coalesce(((count(1) FILTER ( WHERE decline_reason IS NULL ))::numeric /
                                                                               nullif(count(DISTINCT parent_id),'0')),'0'::numeric ) AS "approval"
                                                                        FROM orders_filtered_2
                                                                        WHERE bc_inferred > '0'
                                                                          AND attempt_count >= '0'
                                                                        GROUP BY cc_type, prepaid, crm_id, bc_inferred, attempt_count );
                    DROP TABLE IF EXISTS cc_stats;
                    CREATE TEMP TABLE cc_stats ON COMMIT DROP AS (SELECT cc_type,
                                                                               prepaid,
                                                                               bc_inferred,
                                                                               attempt_count,
                                                                               count(1) AS "sample",
                                                                               coalesce((count(1) FILTER ( WHERE decline_reason IS NULL ))::numeric /
                                                                               nullif(count(DISTINCT parent_id), '0'),'0'::numeric ) AS "approval"
                                                                        FROM orders_filtered_2
                                                                        WHERE bc_inferred > '0'
                                                                          AND attempt_count >= '0'
                                                                        GROUP BY cc_type, prepaid, bc_inferred, attempt_count );
                    DROP TABLE IF EXISTS provider_stats;
                    CREATE TEMP TABLE provider_stats ON COMMIT DROP AS (SELECT cc_type,
                                                                               prepaid,
                                                                               vertical,
                                                                               provider,
                                                                               bc_inferred,
                                                                               attempt_count,
                                                                               count(1) AS "sample",
                                                                               coalesce((count(1) FILTER ( WHERE decline_reason IS NULL ))::numeric /
                                                                               nullif(count(DISTINCT parent_id), '0'), '0' ) AS "approval"
                                                                        FROM orders_filtered_2
                                                                        WHERE bc_inferred > '0'
                                                                          AND attempt_count >= '0'
                                                                        GROUP BY cc_type, prepaid, vertical, provider, bc_inferred,
                                                                                 attempt_count
                                                                        HAVING count(1) > '100');
                    DROP TABLE IF EXISTS first_aff_stats;
                    CREATE TEMP TABLE first_aff_stats ON COMMIT DROP AS (SELECT cc_type,
                                                                                prepaid,
                                                                                vertical,
                                                                                provider,
                                                                                first_affiliate,
                                                                                bc_inferred,
                                                                                attempt_count,
                                                                                count(1) AS "sample",
                                                                                coalesce((count(1) FILTER ( WHERE decline_reason IS NULL ))::numeric /
                                                                                nullif(count(DISTINCT parent_id), '0'), '0') AS "approval"
                                                                         FROM orders_filtered_2
                                                                         WHERE bc_inferred > '0'
                                                                           AND attempt_count >= '0'
                                                                         GROUP BY cc_type, prepaid, vertical, provider, first_affiliate,
                                                                                  bc_inferred, attempt_count
                                                                         HAVING count(1) > '100');
                    DROP TABLE IF EXISTS recurring_orders_temp;
                    CREATE TEMP TABLE recurring_orders_temp ON COMMIT DROP AS ( SELECT DISTINCT ON ( crm_id, order_id ) crm_id, order_id, gateway_id, cc_type FROM crm_global.orders WHERE is_recurring = '1' AND decline_reason IS NULL AND cc_type <> 'TESTCARD' AND crm_id IN ( '{_in_crm_ids}' ) );
                    DROP TABLE IF EXISTS recurring_orders_filter;
                    CREATE TEMP TABLE recurring_orders_filter ON COMMIT DROP AS (SELECT a.crm_id,
                                                                                        c.ancestor_id,
                                                                                        c.order_id,
                                                                                        c.parent_id,
                                                                                        c.bc_inferred + '1'::integer                                                                                                              AS "bc_inferred",
                                                                                        c.attempt_count,
                                                                                        CASE
                                                                                            WHEN c.retry_attempt_count IS NULL THEN '0'::integer
                                                                                            ELSE c.retry_attempt_count + '1'::integer END                                                                                         AS "retry_attempt_count",
                                                                                        b.destination_gateway,
                                                                                        a.gateway_id,
                                                                                        c.first_affiliate,
                                                                                        /*CASE WHEN b.recurring_date > b.retry_date AND b.recurring_date - b.time_stamp > '200 days' THEN b.time_stamp + interval '155 days'
                                                                                            WHEN b.recurring_date > b.retry_date THEN coalesce( b.recurring_date, b.retry_date ) ELSE coalesce( b.retry_date, b.recurring_date ) END*/coalesce(b.retry_date, b.recurring_date)/*coalesce(b.recurring_date::date, (CASE
                                                                 WHEN c.bc_inferred = '0' THEN a.time_stamp + interval '15 days'
                                                                 ELSE a.time_stamp + interval '30 days' END))::date*/ AS "next_cycle_date",
                                                                                        CASE WHEN c.step = '1' THEN '89.99'::numeric ELSE '87.85'::numeric END                                                                    AS "amount",
                                                                                        e.class,
                                                                                        CASE
                                                                                            WHEN e.class = 'prepaid' OR e.class = 'block'
                                                                                                THEN TRUE::boolean
                                                                                            ELSE FALSE::boolean END                                                                                                               AS "pp_customer",
                                                                                        g.c1                                                                                                                                      AS "provider",
                                                                                        e.step,
                                                                                        e.offer_id,
                                                                                        f.name                                                                                                                                    AS "offer",
                                                                                        f.vertical,
                                                                                        h.processor,
                                                                                        i.corporation_name AS "corp",
                                                                                        CASE
                                                                                            WHEN lower(a.cc_type) = 'mastercard'
                                                                                                THEN 'master'
                                                                                            ELSE lower(a.cc_type) END                                                                                                             AS "cc_type",
                                                                                        b.active,
                                                                                        b.is_dead_mid_cascade                                                                                                                     AS "is_cascade"
                                                                                 FROM recurring_orders_temp AS "a"
                                                                                          LEFT JOIN (SELECT DISTINCT ON ( crm_id, order_id ) crm_id,
                                                                                                                                             order_id,
                                                                                                                                             active,
                                                                                                                                             processing_status,
                                                                                                                                             time_stamp,
                                                                                                                                             recurring_date,
                                                                                                                                             retry_date,
                                                                                                                                             is_dead_mid_cascade,
                                                                                                                                             parent_gateway,
                                                                                                                                             destination_gateway
                                                                                                     FROM processing.recurring_orders
                                                                                                     WHERE processing_status = '0') AS "b"
                                                                                                    ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                                                                                          INNER JOIN augmented_data.order_cycles AS "c"
                                                                                                     ON c.crm_id = a.crm_id AND c.order_id = a.order_id
                                                                                          INNER JOIN augmented_data.order_cycles AS "d"
                                                                                                     ON d.crm_id = c.crm_id AND d.order_id = c.ancestor_id
                                                                                          INNER JOIN ui_54407332_offers.campaigns AS "e"
                                                                                                     ON e.crm_id = a.crm_id AND e.campaign_id = d.campaign_id
                                                                                          INNER JOIN ui_54407332_offers.offers AS "f" ON f.offer_id = e.offer_id
                                                                                          INNER JOIN orders_provider AS "g"
                                                                                                     ON g.crm_id = a.crm_id AND g.order_id = d.order_id
                                                                                          INNER JOIN (SELECT DISTINCT ON ( crm_id, gateway_id ) crm_id, gateway_id, corp_id, processor
                                                                                                      FROM ui_54407332_clients.mids AS "a"
                                                                                                               INNER JOIN (SELECT DISTINCT ON ( crm_id, gateway_id ) crm_id, gateway_id, mid_id
                                                                                                                           FROM ui_54407332_clients.steps) AS "b"
                                                                                                                          ON b.mid_id = a.mid_id) AS "h"
                                                                                                     ON h.crm_id = a.crm_id AND
                                                                                                        h.gateway_id =
                                                                                                        coalesce(b.destination_gateway, a.gateway_id)
                                                                                 INNER JOIN ui_54407332_clients.corps AS "i" ON i.corp_id = h.corp_id );
                    --SELECT count( 1 ) FROM recurring_orders_filter WHERE crm_id = 'crm_kk_3' AND bc_inferred = '1' AND retry_attempt_count = '0' AND active IS TRUE AND next_cycle_date > now()::date;
                    --SELECT count( 1 ) FROM recurring_orders_filter WHERE crm_id = 'crm_ll_2' AND bc_inferred = '1' AND retry_attempt_count = '0' AND active IS NOT NULL;
                    --SELECT count( 1 ) FROM processing.recurring_orders;
                    --SELECT count( 1 ) FROM crm_global.orders WHERE crm_id IN ( 'crm_kk_3', 'crm_ll_2' ) AND
                    DROP TABLE reporting.continuity;
                    CREATE TABLE reporting.continuity AS (SELECT a.crm_id,
                                                                 a.ancestor_id,
                                                                 a.order_id,
                                                                 a.parent_id,
                                                                 a.bc_inferred,
                                                                 a.attempt_count,
                                                                 a.retry_attempt_count,
                                                                 a.destination_gateway,
                                                                 a.gateway_id,
                                                                 a.first_affiliate AS "affid",
                                                                 a.next_cycle_date,
                                                                 a.amount,
                                                                 a.class,
                                                                 CASE WHEN a.pp_customer IS TRUE THEN '1' ELSE '0' END AS "pp_customer",
                                                                 a.provider,
                                                                 a.step,
                                                                 a.offer_id,
                                                                 a.offer,
                                                                 a.vertical,
                                                                 a.processor,
                                                                 a.corp,
                                                                 a.cc_type,
                                                                 a.active,
                                                                 a.is_cascade,
                                                                 coalesce(d.approval, c.approval, b.approval, '0.5'::numeric)                                                                                                                                                                             AS "approval_1",
                                                                 coalesce(((coalesce(d.approval, '0')::numeric *
                                                                            coalesce(d.sample * '10'::numeric, '0')::numeric)
                                                                     + (coalesce(c.approval, '0')::numeric *
                                                                        coalesce(c.sample, '0')::numeric)
                                                                     + (coalesce(b.approval, '0')::numeric *
                                                                        coalesce(b.sample, '0')::numeric)
                                                                     + (coalesce(f.approval, '0')::numeric *
                                                                        coalesce(f.sample, '0')::numeric)
                                                                     + (coalesce(g.approval, '0')::numeric *
                                                                        coalesce(g.sample, '0')::numeric))::numeric / nullif(
                                                                                  (coalesce(d.sample * '10'::numeric, '0')::numeric +
                                                                                   coalesce(c.sample, '0')::numeric +
                                                                                   coalesce(b.sample, '0')::numeric +
                                                                                   coalesce(f.sample, '0')::numeric +
                                                                                   coalesce(g.sample, '0')::numeric), '0'), '0.50'::numeric)/* / ( ( CASE WHEN b.sample IS NULL THEN '0' ELSE '1' END )::numeric
                                                                                                      + ( CASE WHEN c.sample IS NULL THEN '0' ELSE '1' END )::numeric
                                                                                                      + ( CASE WHEN d.sample IS NULL THEN '0' ELSE '1' END )::numeric
                                                                                                      + ( CASE WHEN f.sample IS NULL THEN '0' ELSE '1' END )::numeric
                                                                                                      + ( CASE WHEN g.sample IS NULL THEN '0' ELSE '1' END )::numeric)::numeric*/ AS "approval",/*
                                                                                            d.approval AS "d", c.approval AS "c", b.approval AS "b", f.approval AS "f", g.approval AS "g",
                                                                                            d.sample AS "d", c.sample AS "c", b.sample AS "b", f.sample AS "f", g.sample AS "g",*/
                                                                 e.order_total
                                                          FROM recurring_orders_filter AS "a"
                                                                   LEFT JOIN vertical_stats AS "b"
                                                                             ON b.bc_inferred = a.bc_inferred AND
                                                                                b.attempt_count =
                                                                                a.retry_attempt_count AND
                                                                                b.cc_type = a.cc_type AND
                                                                                b.prepaid = a.pp_customer AND
                                                                                b.vertical = a.vertical
                                                                   LEFT JOIN provider_stats AS "c"
                                                                             ON c.bc_inferred = a.bc_inferred AND
                                                                                c.attempt_count =
                                                                                a.retry_attempt_count AND
                                                                                c.cc_type = a.cc_type AND
                                                                                c.prepaid = a.pp_customer AND
                                                                                c.vertical = a.vertical AND
                                                                                c.provider = a.provider
                                                                   LEFT JOIN first_aff_stats AS "d"
                                                                             ON d.bc_inferred = a.bc_inferred AND
                                                                                d.attempt_count =
                                                                                a.retry_attempt_count AND
                                                                                d.cc_type = a.cc_type AND
                                                                                d.prepaid = a.pp_customer AND
                                                                                d.vertical = a.vertical AND
                                                                                d.provider = a.provider AND
                                                                                d.first_affiliate =
                                                                                a.first_affiliate
                                                                   LEFT JOIN order_total_average "e"
                                                                             ON e.crm_id = a.crm_id AND
                                                                                e.bc_inferred = a.bc_inferred AND
                                                                                e.attempt_count =
                                                                                a.retry_attempt_count
                                                                   LEFT JOIN crm_stats AS "f"
                                                                             ON f.bc_inferred = a.bc_inferred AND
                                                                                f.attempt_count =
                                                                                a.retry_attempt_count AND
                                                                                f.cc_type = a.cc_type AND
                                                                                f.prepaid = a.pp_customer AND
                                                                                f.crm_id = a.crm_id
                    
                                                                   LEFT JOIN cc_stats AS "g"
                                                                             ON g.bc_inferred = a.bc_inferred AND
                                                                                g.attempt_count =
                                                                                a.retry_attempt_count AND
                                                                                g.cc_type = a.cc_type AND
                                                                                g.prepaid = a.pp_customer);
                    ALTER TABLE reporting.continuity OWNER TO cloudsqlsuperuser;
            
                    
                    """)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        cur.close()
        conn.close()
        raise e
