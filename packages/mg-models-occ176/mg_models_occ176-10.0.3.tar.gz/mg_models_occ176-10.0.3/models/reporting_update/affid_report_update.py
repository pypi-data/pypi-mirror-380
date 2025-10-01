
def run(db, crm_id, work_mem='15GB', overwrite=False, **kw):
    conn = db.engine.raw_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            f"""
            SET LOCAL work_mem = '{work_mem}';
            /*CPA*/
            
            
            CREATE TEMP TABLE cpa_all_crms ON COMMIT DROP AS (SELECT crm_id, order_id, cpa + coalesce(credit, '0'::numeric) AS "cpa"
                                                          FROM reporting.assigned_cpa_orders
                                                          WHERE crm_id = '{crm_id}'
                                                            AND cpa IS NOT NULL
                                                            AND cpa > '0');
            /*ALERT*/
            -- TODO Add alert prices for ethoca and rdr seperately
            -- TODO Change this to be the parameterized crm_id
             CREATE TEMP TABLE cpa_alerts_{crm_id} ON COMMIT DROP AS ( select a.crm_id, a.order_id, b.alert_fee as "alert_cost" from
                                                                    (SELECT '{crm_id}'                          AS "crm_id",
                                                                        max((CASE WHEN note ~~* '%%rdr%%' THEN 'rdr'::text ELSE 'ethoca' END)) as "alert_provider",
                                                                        native_order_id                     AS "order_id"
                                                                 FROM crm_global.employee_notes AS "a"
                                                                 WHERE crm_id = '{crm_id}'
                                                                   AND (note  ~~* '%%alert%%' or note ~~* '%%CB360%%' )
                                                                 GROUP BY native_order_id) a
                               inner join reporting.alert_providers b on b.alert_provider= a.alert_provider);
        """)
            
            
        cur.execute(f"""
            SET LOCAL work_mem = '{work_mem}';
            CREATE TEMP TABLE cpa_decline_salvage_recurring ON COMMIT DROP AS (SELECT DISTINCT a.crm_id, a.order_id
                                                                           FROM augmented_data.order_cycles_{crm_id} AS "a"
                                                                                    INNER JOIN crm_global.orders_{crm_id} AS "b"
                                                                                               ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                                                                                    INNER JOIN (SELECT DISTINCT a.crm_id, a.product
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
                                                                                                       WHERE is_rebill IS TRUE)) AS "a") AS "c"
                                                                                               ON c.crm_id = a.crm_id AND
                                                                                                  c.product::integer =
                                                                                                  b.main_product_id::integer
                                                                           WHERE a.retry_attempt_count IS NOT NULL
                                                                             AND a.retry_attempt_count > '0'
                                                                             AND b.is_recurring > '0');
            
            --SELECT DISTINCT main_product_id
            --FROM crm_global.orders_{crm_id};
            CREATE TEMP TABLE orders_temp ON COMMIT DROP AS (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id,
                                                              a.order_id,
                                                              a.time_stamp,
                                                              a.customer_id,
                                                              a.refund_amount,
                                                              a.amount_refunded_to_date,
                                                              a.is_chargeback,
                                                              a.decline_reason,
                                                              a.order_total,
                                                              c.campaign_id,
                                                              c.gateway_id as ancestor_gateway,
                                                              a.native_order_id,
                                                              a.tracking_number,
                                                              a.affiliate,
                                                              a.c1,
                                                              a.cc_type,
                                                              a.gateway_id,
                                                              NULL::date                               AS "extended_date",
                                                              a.last_modified,
                                                              substring(a.email_address from '@(.*)$') AS "domain",
                                                              a.shippable,
                                                              a.main_product_id
                  FROM crm_global.orders_{crm_id} AS "a"
                           INNER JOIN augmented_data.order_cycles_{crm_id} AS "b"
                                      ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                           INNER JOIN crm_global.orders_{crm_id} AS "c"
                                      ON c.crm_id = a.crm_id AND c.order_id = b.ancestor_id
                  WHERE a.is_test_cc = '0');
            """)
        cur.execute(f"""
            /*ORDERS**/
            
            --TODO: Check hard coded costs. Check bin shave
            CREATE TEMP TABLE temp_cpa_orders ON COMMIT DROP AS (
            SELECT a.crm_id,
                   a.customer_id,
                   a.order_id,
                   b.parent_id,
                   b.ancestor_id,
                   a.native_order_id,
                   d.vertical,
                   c.class                                                        AS "campaign_class",
                   c.offer_id,
                   d.name                                                         AS "offer",
                   coalesce(a.c1, h.source_title, '-')                            AS "provider",
                   coalesce(a.affiliate, h.source_value1, '-')                    AS "affid",
                   NULL::text                                                     AS "subaffid",
                   a.decline_reason,
                   a.order_total,
                   a.refund_amount,
                   a.amount_refunded_to_date,
                   CASE
                       WHEN (coalesce(a.refund_amount, '0'::numeric)) >
                            (coalesce(a.amount_refunded_to_date, '0'::numeric)) THEN (coalesce(a.refund_amount, '0'::numeric))
                       ELSE coalesce(a.amount_refunded_to_date, '0'::numeric) END AS "total_refund",
                   a.is_chargeback,
                   b.bc_inferred,
                   b.step,
                   b.attempt_count,
                   b.retry_attempt_count,
                   coalesce( j.ancestor_acquisition_date, b.acquisition_date ) AS "acquisition_date",
                   a.time_stamp,
                   CASE
                       WHEN a.decline_reason IS NULL THEN (a.order_total * '0.10'::numeric) + '0.30'::numeric
                       ELSE '0.30'::numeric END                                   AS "processing_cost",
                   CASE
                       WHEN a.decline_reason IS NULL AND a.is_chargeback > '0' THEN a.order_total + '45'::numeric
                       ELSE '0'::numeric END                                      AS "chargeback_cost",
                   CASE
                       WHEN a.decline_reason IS NULL AND a.shippable = '1' THEN '9'::numeric + (order_total*'0.02'::numeric)
                       ELSE '0'::numeric END                                      AS "product_cost",
                   '0'::numeric                                                   AS "alert_cost",
                   '0'::numeric                                                   AS "cpa",
                   CASE
                       WHEN c.class = 'prepaid' AND bc_inferred = '0' THEN '1'::numeric
                       ELSE '0'::numeric END                                      AS "prepaid_campaign",
                   CASE
                       WHEN c.class <> 'provider' AND bc_inferred = '0' THEN '1'::numeric
                       ELSE '0'::numeric END                                      AS "order_diverted",
                   CASE
                       WHEN c.class = 'saves' AND bc_inferred = '0' THEN '1'::numeric
                       ELSE '0'::numeric END                                      AS "saves",
                   CASE
                       WHEN c.class = 'block' AND bc_inferred = '0' THEN '1'::numeric
                       ELSE '0'::numeric END                                      AS "bin_pause",
                   CASE
                       WHEN c.class = 'provider' AND bc_inferred = '0' THEN '1'::numeric
                       ELSE '0'::numeric END                                      AS "order_provider",
                   CASE
                       WHEN g.customer_id IS NOT NULL THEN '1' ::numeric
                       ELSE '0'::numeric END                                      AS "pp_customer",
                   CASE
                       WHEN i.ancestor_id IS NOT NULL THEN '1' ::numeric
                       ELSE '0'::numeric END                                      AS "block_customer",
                   NULL::numeric                                                  AS "step_2_salvaged",
                   NULL::numeric                                                  AS "step_1_with_2_salvaged",
                   NULL::boolean                                                  AS "pending",
                   NULL::boolean                                                  AS "d_pending",
                   FALSE::boolean                                                 AS "customer_pending",
                   CASE
                       WHEN a.cc_type = 'VISA' THEN 'Visa'
                       WHEN a.cc_type = 'MASTERCARD' THEN 'Master'
                       WHEN a.cc_type = 'DISCOVER' THEN 'Discover'
                       WHEN a.cc_type = 'visa' THEN 'Visa'
                       WHEN a.cc_type = 'master' THEN 'Master'
                       WHEN a.cc_type = 'discover' THEN 'Discover'
                       ELSE 'unknown' END                                         AS "cc_type",
                   NULL::TEXT                                                     AS "processor",
                   a.gateway_id,
                   NULL::date AS "gateway_date_added",
                   NULL::TEXT                                                     AS "mid_id",
                   NULL::TEXT                                                     AS "mid_number",
                   NULL::TEXT                                                     AS "corp",
                   NULL::TEXT                                                     AS "bin",
                   a.extended_date,
                   a.last_modified,
                   NULL::text                                                     AS "mcc",
                   NULL::numeric                                                  AS "forecast_approval",
                   'no'::text                                                     AS "is_cascade",
                   NULL::text                                                     AS "sub_affid",
                   a.domain                                                       AS "domain",
                   NULL::text                                                     AS "product_recurring",
                   CASE WHEN b.step = '1' THEN TRUE ELSE FALSE END                AS "include_in_r",
                   CASE
                       WHEN ancestor_gateway = '1' THEN TRUE
                       ELSE FALSE::BOOLEAN END AS "cap_fill" --,
                   /*CASE
                      WHEN step = '1' and ancestor_gateway = '1' THEN 1
                      ELSE 0 END AS "free_sub"*/
            
            FROM orders_temp AS "a"
                     INNER JOIN augmented_data.order_cycles_{crm_id} AS "b"
                                ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                     INNER JOIN ui_54407332_offers.campaigns AS "c"
                                ON c.crm_id = a.crm_id AND c.campaign_id = a.campaign_id
                     INNER JOIN ui_54407332_offers.offers AS "d" ON d.offer_id = c.offer_id
         
                       
                     LEFT JOIN (SELECT DISTINCT customer_id
                                FROM crm_global.orders_{crm_id} AS "a"
                                         INNER JOIN ui_54407332_offers.campaigns AS "b"
                                                    ON b.crm_id = a.crm_id AND b.campaign_id = a.campaign_id
                                WHERE (class = 'prepaid' OR class = 'block')
                                   OR (prepaid_match IS TRUE)) AS "g" ON g.customer_id = a.customer_id
                     LEFT JOIN (SELECT DISTINCT ON ( crm_id, customer_id ) crm_id,
                                                                           customer_id,
                                                                           c1        AS "source_title",
                                                                           affiliate AS "source_value1"
                                FROM crm_global.orders_{crm_id} AS "a"
                                WHERE c1 IS NOT NULL
                                  AND affiliate IS NOT NULL) AS "h"
                               ON h.crm_id = a.crm_id AND h.customer_id = a.customer_id
                     LEFT JOIN (SELECT DISTINCT b.ancestor_id
                                FROM crm_global.orders_{crm_id} AS "a"
                                         INNER JOIN augmented_data.order_cycles_{crm_id} AS "b"
                                                    ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                                         INNER JOIN ui_54407332_offers.campaigns AS "c"
                                                    ON c.crm_id = a.crm_id AND c.campaign_id = a.campaign_id
                                WHERE (c.class = 'block')
                                  AND b.ancestor_id IS NOT NULL
                                  AND a.decline_reason IS NULL) AS "i" ON i.ancestor_id = b.ancestor_id
                     LEFT JOIN (SELECT a.crm_id, a.ancestor_id, b.order_id, a.ancestor_acquisition_date
                                 FROM (SELECT crm_id, ancestor_id, min(time_stamp) AS "ancestor_acquisition_date"
                                       FROM augmented_data.order_cycles_{crm_id}
                                       WHERE decline_reason IS NULL
                                       GROUP BY crm_id, ancestor_id) AS "a"
                                          INNER JOIN augmented_data.order_cycles_{crm_id} AS "b"
                                                     ON b.crm_id = a.crm_id AND b.ancestor_id = a.ancestor_id) AS "j"
                                ON j.crm_id = a.crm_id AND j.order_id = a.order_id
              WHERE c.class is not null
            --WHERE c.class IN ('provider', 'saves', 'prepaid', 'block', 'rebill')
            );""")
        cur.execute(f"""
                    --TODO: Check cog costs
            CREATE TEMP TABLE cog_cost ON COMMIT DROP AS (SELECT a.crm_id,
                                                             a.order_id,
                                                             'product_cost'                                                                 AS "type",
                                                             b.sku,
                                                             b.product_id,
                                                             c.cost_of_goods,
                                                             b.shipping_date,
                                                             a.time_stamp,
                                                          /*coalesce(*/(- (c.cost_of_goods::NUMERIC + CASE
                                                                                                          WHEN step = '1'
                                                                                                              THEN '0.0'::numeric + '0'::numeric
                                                                                                          WHEN step > '1'
                                                                                                              THEN '0.0'::numeric
                                                                                                          ELSE '0'::numeric END))/*, '0')*/ AS "value"
                                                      FROM (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id,
                                                                                                        a.order_id,
                                                                                                        a.step,
                                                                                                        a.time_stamp
                                                            FROM augmented_data.order_cycles_{crm_id} AS "a"
                                                                     INNER JOIN temp_cpa_orders uci
                                                                                on a.crm_id = uci.crm_id and a.order_id = uci.order_id) AS "a"
                                                               INNER JOIN (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id,
                                                                                                                       a.order_id,
                                                                                                                       a.main_product_id,
                                                                                                                       b.product_id,
                                                                                                                       b.sku,
                                                                                                                       a.shipping_date
                                                                           FROM crm_global.orders_{crm_id} AS "a"
                                                                                    LEFT JOIN crm_global.products AS "b"
                                                                                              ON b.crm_id = a.crm_id AND b.product_id::text = a.main_product_id::text
                                                INNER JOIN temp_cpa_orders AS "c" ON c.crm_id = a.crm_id AND c.order_id = a.order_id
                                                                           WHERE a.decline_reason IS NULL
                                                                             AND a.shippable = '1') AS "b"
                                                                          ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                                                               LEFT JOIN (SELECT DISTINCT ON ( crm_id, sku ) crm_id, sku, cost_of_goods
                                                                          FROM crm_global.products
                                                                          WHERE cost_of_goods::numeric > '0'
                                                                            /*AND cost_of_goods::numeric < '10'*/
                                                                            AND cost_of_goods IS NOT NULL) AS "c"
                                                                         ON c.crm_id = b.crm_id AND c.sku = b.sku);
            DELETE
            FROM cog_cost
            WHERE cost_of_goods IS NULL
            /*OR entered IS NOT NULL*/;
            UPDATE cog_cost
            SET shipping_date = time_stamp::date
            WHERE shipping_date = 'Not Shipped';
            UPDATE cog_cost
            SET shipping_date = date_trunc('MONTH', shipping_date::date) + interval '1 day';
            UPDATE temp_cpa_orders SET product_cost = abs(value) FROM cog_cost AS a WHERE temp_cpa_orders.crm_id = a.crm_id AND temp_cpa_orders.order_id = a.order_id AND abs(a.value) > '0' AND a.value IS NOT NULL;
            --
            UPDATE temp_cpa_orders
            SET cpa = a.cpa
            FROM cpa_all_crms AS "a"
            WHERE temp_cpa_orders.crm_id::text = a.crm_id::text
            AND temp_cpa_orders.order_id::text = a.order_id::text;
            UPDATE temp_cpa_orders
            SET alert_cost = ( a.alert_cost::numeric + total_refund::numeric )/*,
            total_refund = '0'*/
            FROM cpa_alerts_{crm_id} AS "a"
            WHERE temp_cpa_orders.crm_id = a.crm_id
            AND temp_cpa_orders.order_id::text = a.order_id;
            
            UPDATE temp_cpa_orders
            SET total_refund = '0'
            FROM cpa_alerts_{crm_id} AS "a"
            WHERE temp_cpa_orders.crm_id = a.crm_id
            AND temp_cpa_orders.order_id::text = a.order_id;/*
            AND a.alert_count > '0'
            AND a.alert_count < '3'
            AND cpa_orders.step = '1'*/;
            UPDATE temp_cpa_orders
            SET pending = NULL
            WHERE pending IS TRUE
            or pending IS FALSE;
            UPDATE temp_cpa_orders
            SET pending = TRUE::boolean
            FROM (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id, a.order_id
              FROM augmented_data.order_cycles_{crm_id} AS "a"
                       INNER JOIN (SELECT DISTINCT ON ( crm_id, order_id ) crm_id, order_id, main_product_id
                                   FROM crm_global.orders_{crm_id}
                                   WHERE is_recurring > '0') AS "b"
                                  ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                       INNER JOIN (SELECT DISTINCT a.crm_id, a.product
                                   FROM ((SELECT DISTINCT crm_id, rebill_product_id AS "product"
                                          FROM ui_54407332_offers.offer_globals
                                          WHERE is_rebill IS TRUE)
                                         UNION ALL
                                         (SELECT DISTINCT crm_id, charge_product_id AS "product"
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
                                   WHERE a.product IS NOT NULL
              ) AS "c" ON c.crm_id = a.crm_id AND c.product::integer = b.main_product_id::integer
              WHERE decline_reason IS NULL
                AND retry_attempt_count IS NULL) AS "a"
            WHERE temp_cpa_orders.order_id = a.order_id;
            UPDATE temp_cpa_orders
            SET pending = FALSE::boolean
            FROM (SELECT DISTINCT ON ( order_id ) order_id,
                                              concat(concat('20', substr(cc_expires, 3, 2)), '-', substr(cc_expires, 1, 2), '-',
                                                     '01')::date AS "cc_expires"
              FROM crm_global.orders_{crm_id} WHERE cc_expires IS NOT NULL) AS "a"
            WHERE a.order_id = temp_cpa_orders.order_id
            AND temp_cpa_orders.pending IS TRUE::boolean
            AND a.cc_expires::timestamp < now();
            UPDATE temp_cpa_orders
            SET customer_pending = TRUE::boolean
            FROM (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id, a.customer_id
              FROM augmented_data.order_cycles_{crm_id} AS "a"
                       INNER JOIN (SELECT DISTINCT crm_id, order_id
                                   FROM crm_global.orders_{crm_id}
                                   WHERE is_recurring > '0') AS "b"
                                  ON b.crm_id = a.crm_id AND b.order_id = a.order_id
              WHERE decline_reason IS NULL
                AND retry_attempt_count IS NULL) AS "a"
            WHERE temp_cpa_orders.crm_id = a.crm_id
            AND temp_cpa_orders.customer_id = a.customer_id;
            UPDATE temp_cpa_orders
            SET pending = FALSE::boolean
            FROM (SELECT DISTINCT a.crm_id, a.order_id
              FROM temp_cpa_orders AS "a"
                       LEFT JOIN (SELECT DISTINCT crm_id, order_id
                                  FROM processing.recurring_orders
                                  WHERE processing_status = '0') AS "b" ON b.crm_id = a.crm_id AND b.order_id = a.order_id
              WHERE a.pending IS TRUE
                AND b.order_id IS NULL) AS "a"
            WHERE temp_cpa_orders.pending IS TRUE AND temp_cpa_orders.crm_id = a.crm_id AND temp_cpa_orders.order_id = a.order_id ;
            UPDATE temp_cpa_orders
            SET d_pending = TRUE
            FROM cpa_decline_salvage_recurring AS "a"
            WHERE temp_cpa_orders.crm_id = a.crm_id
            AND temp_cpa_orders.order_id = a.order_id;
            UPDATE temp_cpa_orders
            SET d_pending = FALSE::boolean
            FROM ( SELECT DISTINCT a.crm_id, a.order_id FROM temp_cpa_orders AS "a" LEFT JOIN ( SELECT DISTINCT crm_id, order_id FROM processing.recurring_orders WHERE processing_status = '0' ) AS "b" ON b.crm_id = a.crm_id AND b.order_id = a.order_id WHERE a.d_pending IS TRUE AND b.order_id IS NULL ) AS "a"
            WHERE temp_cpa_orders.d_pending IS TRUE AND temp_cpa_orders.crm_id = a.crm_id AND temp_cpa_orders.order_id = a.order_id ;
            UPDATE temp_cpa_orders
            SET processor = a.processor,
            mcc       = a.mcc,
            corp      = a.corporation_name,
            mid_id    = a.mid_id,
            mid_number = a.mid_number
            FROM (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id, a.order_id, b.processor, b.mcc, b.mid_id, b.mid_number, b.corporation_name
              FROM crm_global.orders_{crm_id} AS "a"
                       INNER JOIN (SELECT DISTINCT ON ( a.crm_id, a.gateway_id ) a.crm_id,
                                                                                 a.gateway_id,
                                                                                 a.mid_id,
                                                                                 a.mid_number,
                                                                                 b.processor,
                                                                                 a.mcc,
                                                                                 c.corporation_name
                                   FROM (SELECT DISTINCT ON ( crm_id, gateway_id ) crm_id, gateway_id, mid_id, mid_number, mcc
                                         FROM ui_54407332_clients.steps
                                        ) AS "a"
                                            INNER JOIN (SELECT DISTINCT mid_id, processor, corp_id
                                                        FROM ui_54407332_clients.mids) AS "b" ON b.mid_id = a.mid_id
                                            INNER JOIN ui_54407332_clients.corps AS "c" ON c.corp_id = b.corp_id) AS "b"
                                  ON b.crm_id = a.crm_id AND b.gateway_id = a.gateway_id) AS "a"
            WHERE temp_cpa_orders.crm_id = a.crm_id
            AND temp_cpa_orders.order_id = a.order_id;
            UPDATE temp_cpa_orders
            SET bin = cc_first_6
            FROM (SELECT DISTINCT ON ( crm_id, order_id ) crm_id, order_id, cc_first_6
              FROM crm_global.orders_{crm_id}
              WHERE cc_first_6 IS NOT NULL) AS "a"
            WHERE temp_cpa_orders.crm_id = a.crm_id
            AND temp_cpa_orders.order_id = a.order_id;
            
            UPDATE temp_cpa_orders
            SET is_cascade = 'yes'
            FROM (SELECT DISTINCT a.crm_id, a.customer_id
              FROM temp_cpa_orders AS "a"
                       INNER JOIN temp_cpa_orders AS "b" ON b.crm_id = a.crm_id AND b.order_id = a.parent_id
              WHERE a.processor <> b.processor AND a.cap_fill IS FALSE) AS "cascade"
            WHERE temp_cpa_orders.crm_id = cascade.crm_id
            AND temp_cpa_orders.customer_id = cascade.customer_id;
            UPDATE temp_cpa_orders
            SET sub_affid = a.sub_affiliate
            FROM (SELECT a.crm_id, a.ancestor_id, a.sub_affiliate
              FROM (SELECT a.crm_id,
                           b.ancestor_id,
                           first_value(a.sub_affiliate)
                           over ( PARTITION BY b.ancestor_id ORDER BY a.time_stamp ASC ) AS "sub_affiliate"
                    FROM crm_global.orders_{crm_id} AS "a"
                             INNER JOIN augmented_data.order_cycles_{crm_id} AS "b"
                                        ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                    WHERE a.sub_affiliate IS NOT NULL) AS "a"
              GROUP BY a.crm_id, a.ancestor_id, a.sub_affiliate) AS "a"
            WHERE temp_cpa_orders.crm_id = a.crm_id
            AND temp_cpa_orders.ancestor_id = a.ancestor_id;
            UPDATE temp_cpa_orders
            SET gateway_date_added = a.date_added FROM (
                SELECT DISTINCT ON ( crm_id, gateway_id ) crm_id, gateway_id, date_added FROM ui_54407332_clients.gateway_settings
                                                       ) AS "a"
            WHERE temp_cpa_orders.crm_id = a.crm_id AND temp_cpa_orders.gateway_id = a.gateway_id;
            
            UPDATE reporting.cpa_orders
            SET crm_id                  = tc.crm_id,
            customer_id             = tc.customer_id,
            order_id                = tc.order_id,
            parent_id               = tc.parent_id,
            ancestor_id             = tc.ancestor_id,
            native_order_id         = tc.native_order_id,
            vertical                = tc.vertical,
            campaign_class          = tc.campaign_class,
            offer_id                = tc.offer_id,
            offer                   = tc.offer,
            provider                = tc.provider,
            affid                   = tc.affid,
            subaffid                = tc.subaffid,
            decline_reason          = tc.decline_reason,
            order_total             = tc.order_total,
            refund_amount           = tc.refund_amount,
            amount_refunded_to_date = tc.amount_refunded_to_date,
            total_refund            = tc.total_refund,
            is_chargeback           = tc.is_chargeback,
            bc_inferred             = tc.bc_inferred,
            step                    = tc.step,
            attempt_count           = tc.attempt_count,
            retry_attempt_count     = tc.retry_attempt_count,
            acquisition_date        = tc.acquisition_date,
            time_stamp              = tc.time_stamp,
            processing_cost         = tc.processing_cost,
            chargeback_cost         = tc.chargeback_cost,
            product_cost            = tc.product_cost,
            alert_cost              = tc.alert_cost,
            cpa                     = tc.cpa,
            prepaid_campaign        = tc.prepaid_campaign,
            order_diverted          = tc.order_diverted,
            saves                   = tc.saves,
            bin_pause               = tc.bin_pause,
            order_provider          = tc.order_provider,
            pp_customer             = tc.pp_customer,
            block_customer          = tc.block_customer,
            step_2_salvaged         = tc.step_2_salvaged,
            step_1_with_2_salvaged  = tc.step_1_with_2_salvaged,
            pending                 = tc.pending,
            d_pending               = tc.d_pending,
            customer_pending        = tc.customer_pending,
            cc_type                 = tc.cc_type,
            processor               = tc.processor,
            mid_id                  = tc.mid_id,
            gateway_date_added      = tc.gateway_date_added,
            corp                    = tc.corp,
            bin                     = tc.bin,
            extended_date           = tc.extended_date,
            last_modified           = tc.last_modified,
            mcc                     = tc.mcc,
            forecast_approval       = tc.forecast_approval,
            is_cascade              = tc.is_cascade,
            sub_affid               = tc.sub_affid,
            domain                  = tc.domain,
            include_in_r            = tc.include_in_r,
            cap_fill                = tc.cap_fill,
            mid_number              = tc.mid_number
            FROM (SELECT a.crm_id,
                     a.acquisition_date,
                     a.order_id,
                     a.customer_id,
                     a.parent_id,
                     a.ancestor_id,
                     a.native_order_id,
                     a.vertical,
                     a.campaign_class,
                     a.offer_id,
                     a.offer,
                     a.provider,
                     a.affid,
                     a.subaffid,
                     a.decline_reason,
                     a.order_total,
                     a.refund_amount,
                     a.amount_refunded_to_date,
                     a.total_refund,
                     a.is_chargeback,
                     a.bc_inferred,
                     a.step,
                     a.attempt_count,
                     a.retry_attempt_count,
                     a.time_stamp,
                     a.processing_cost,
                     a.chargeback_cost,
                     a.product_cost,
                     a.alert_cost,
                     a.cpa,
                     a.prepaid_campaign,
                     a.order_diverted,
                     a.saves,
                     a.bin_pause,
                     a.order_provider,
                     a.pp_customer,
                     a.block_customer,
                     a.step_2_salvaged,
                     a.step_1_with_2_salvaged,
                     a.pending,
                     a.d_pending,
                     a.customer_pending,
                     a.cc_type,
                     a.processor,
                     a.mid_id,
                     a.gateway_date_added,
                     a.corp,
                     a.bin,
                     a.extended_date,
                     a.last_modified,
                     a.mcc,
                     a.forecast_approval,
                     a.is_cascade,
                     a.sub_affid,
                     a.domain,
                     a.include_in_r,
                     a.cap_fill,
                     a.mid_number
              FROM temp_cpa_orders AS "a"
                       INNER JOIN reporting.cpa_orders AS "b" ON b.crm_id = a.crm_id AND b.order_id = a.order_id) AS "tc"
            WHERE cpa_orders.crm_id = tc.crm_id
            AND cpa_orders.order_id = tc.order_id
            AND cpa_orders.crm_id = '{crm_id}';
            {f"DELETE FROM reporting.cpa_orders where crm_id='{crm_id}';" if overwrite else ""}
            INSERT INTO reporting.cpa_orders (crm_id,
                                          acquisition_date,
                                          order_id,
                                          customer_id,
                                          parent_id,
                                          ancestor_id,
                                          native_order_id,
                                          vertical,
                                          campaign_class,
                                          offer_id,
                                          offer,
                                          provider,
                                          affid,
                                          subaffid,
                                          decline_reason,
                                          order_total,
                                          refund_amount,
                                          amount_refunded_to_date,
                                          total_refund,
                                          is_chargeback,
                                          bc_inferred,
                                          step,
                                          attempt_count,
                                          retry_attempt_count,
                                          time_stamp,
                                          processing_cost,
                                          chargeback_cost,
                                          product_cost,
                                          alert_cost,
                                          cpa,
                                          prepaid_campaign,
                                          order_diverted,
                                          saves,
                                          bin_pause,
                                          order_provider,
                                          pp_customer,
                                          block_customer,
                                          step_2_salvaged,
                                          step_1_with_2_salvaged,
                                          pending,
                                          d_pending,
                                          customer_pending,
                                          cc_type,
                                          processor,
                                          mid_id,
                                          gateway_date_added,
                                          corp,
                                          bin,
                                          extended_date,
                                          last_modified,
                                          mcc,
                                          forecast_approval,
                                          is_cascade,
                                          sub_affid,
                                          domain,
                                          include_in_r,
                                          cap_fill,
                                          mid_number) (SELECT tc.crm_id,
                                                            tc.acquisition_date,
                                                            tc.order_id,
                                                            tc.customer_id,
                                                            tc.parent_id,
                                                            tc.ancestor_id,
                                                            tc.native_order_id,
                                                            tc.vertical,
                                                            tc.campaign_class,
                                                            tc.offer_id,
                                                            tc.offer,
                                                            tc.provider,
                                                            tc.affid,
                                                            tc.subaffid,
                                                            tc.decline_reason,
                                                            tc.order_total,
                                                            tc.refund_amount,
                                                            tc.amount_refunded_to_date,
                                                            tc.total_refund,
                                                            tc.is_chargeback,
                                                            tc.bc_inferred,
                                                            tc.step,
                                                            tc.attempt_count,
                                                            tc.retry_attempt_count,
                                                            tc.time_stamp,
                                                            tc.processing_cost,
                                                            tc.chargeback_cost,
                                                            tc.product_cost,
                                                            tc.alert_cost,
                                                            tc.cpa,
                                                            tc.prepaid_campaign,
                                                            tc.order_diverted,
                                                            tc.saves,
                                                            tc.bin_pause,
                                                            tc.order_provider,
                                                            tc.pp_customer,
                                                            tc.block_customer,
                                                            tc.step_2_salvaged,
                                                            tc.step_1_with_2_salvaged,
                                                            tc.pending,
                                                            tc.d_pending,
                                                            tc.customer_pending,
                                                            tc.cc_type,
                                                            tc.processor,
                                                            tc.mid_id,
                                                            tc.gateway_date_added,
                                                            tc.corp,
                                                            tc.bin,
                                                            tc.extended_date,
                                                            tc.last_modified,
                                                            tc.mcc,
                                                            tc.forecast_approval,
                                                            tc.is_cascade,
                                                            tc.sub_affid,
                                                            tc.domain,
                                                            tc.include_in_r,
                                                            tc.cap_fill,
                                                            tc.mid_number
                                                     FROM temp_cpa_orders AS "tc"
                                                              LEFT JOIN reporting.cpa_orders AS "b"
                                                                        ON b.crm_id = tc.crm_id AND b.order_id = tc.order_id
                                                     WHERE b.order_id IS NULL);

            """
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        cur.close()
        conn.close()
        raise e
