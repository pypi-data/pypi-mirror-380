
def run(db, crm_id, max_timestamp, work_mem='16GB', **kw):
    is_not_new = db.engine.execute(f"select count(1) from reporting.ui_revenue_transactions where crm_id='{crm_id}' LIMIT 1").scalar()
    con = db.engine.raw_connection()
    cur = con.cursor()

    try:
        cur.execute(
            f"""
                SET LOCAL WORK_MEM = '{work_mem}';
                SET LOCAL timezone = 'America/Toronto';
            """
        )
        cur.execute(
            f"""
            DROP TABLE IF EXISTS  updated_order_ids;
            CREATE TEMP TABLE updated_order_ids AS (SELECT DISTINCT crm_id, customer_id, order_id
                                             FROM crm_global.orders_{crm_id}
                                             WHERE rep_last_modified >= '{max_timestamp}'::timestamp);

            """
        )
        # GET CPA FROM ASSIGNED CPA
        cur.execute(f"""DROP TABLE IF EXISTS cpa_{crm_id}""")

        cur.execute(
            f"""
                CREATE TEMP TABLE cpa_{crm_id} ON COMMIT DROP
                AS (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id,
                                                                a.order_id,
                                                                date_trunc('DAY', a.acquisition_date) /*+ interval '1 day'*/ AS "date",
                                                                coalesce(a.cpa, '0'::numeric)                                AS "cpa"
                    FROM reporting.assigned_cpa_orders AS "a"
                    LEFT JOIN (select crm_id, order_id from reporting.ui_revenue_transactions where type='cpa') AS "b" ON b.crm_id = a.crm_id AND b.order_id::int = a.order_id::int
                    WHERE a.crm_id = '{crm_id}' and b.order_id is NULL
                      --AND a.acquisition_date > '{max_timestamp}'::date
                      
                      );
               """
        )
        # INSERT CPA -REVENUE
        cur.execute(
            f"""
             INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp)
                    (SELECT crm_id,
                            order_id AS "order_id",
                            date     AS "date",
                            - cpa    AS "value",
                            'cpa'    AS "type",
                            now()    AS "update_time_stamp"
                     FROM cpa_{crm_id})
                ON CONFLICT ( crm_id, order_id, type, date )
                    DO UPDATE SET value             = EXCLUDED.value,
                                  update_time_stamp = EXCLUDED.update_time_stamp;
            """
        )


        # CREATE THE ALERT COSTS
        # TODO: Loop through the Alert providers in to provide cases and translate into join keys
        cur.execute(f"DROP TABLE IF EXISTS  revenue_alerts_{crm_id};")
        cur.execute(f"""
            CREATE TEMP TABLE revenue_alerts_{crm_id} ON COMMIT DROP
            AS (SELECT '{crm_id}'                AS "crm_id",
                       a.order_id,
                       b.alert_provider,
                       min(a.date_time)::date    AS "date",
                       sum(b.alert_fee)::numeric AS "alert_cost",
                       now()                     AS "update_time_stamp"
                FROM (SELECT a.order_id,
                             b.is_rdr,
                             max(b.date_time)
                                 AS date_time,
            
                               (CASE WHEN b.is_rdr =1 then 'rdr' else 'ethoca' end) as alert_provider
                      FROM (SELECT a.crm_id,
                                   a.order_id,
                                   a.order_total,
                                   a.amount_refunded_to_date,
                                   a.native_order_id
                            FROM crm_global.orders_{crm_id} AS "a"
                            WHERE rep_last_modified >= '{max_timestamp}'::timestamp) AS "a"
                               INNER JOIN (SELECT native_order_id,
                                                  max(date_time)                                                             AS date_time,
                                                  max(CASE WHEN note ~~* '%%rdr%%' THEN '1'::integer ELSE '0'::integer END)    AS is_rdr -- max(CASE WHEN note ~~* '%%ethoca%%' THEN '1'::integer ELSE '0'::integer END) AS is_ethoca
            
                                           FROM crm_global.employee_notes AS "a"
                                           WHERE crm_id = '{crm_id}'
                                             AND (note ~~* '%%CB360%%' or note ILIKE '%%alert%%')
                                           GROUP BY native_order_id) AS "b"
                                          ON b.native_order_id::integer = a.order_id::integer
                      GROUP BY a.order_id, b.is_rdr) AS "a"
                inner join reporting.alert_providers b on a.alert_provider = b.alert_provider
                GROUP BY a.order_id, b.alert_provider);
        """)
        cur.execute(f"""
            INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp, alert_provider)
                (SELECT crm_id,
                        order_id     AS "order_id",
                        date         AS "date",
                        - alert_cost AS "value",
                        'alert'      AS "type",
                        update_time_stamp,
                        alert_provider
                 FROM revenue_alerts_{crm_id})
            ON CONFLICT ( crm_id, order_id, type, date )
                DO UPDATE SET value             = EXCLUDED.value,
                              update_time_stamp = EXCLUDED.update_time_stamp,
                              alert_provider = EXCLUDED.alert_provider;
        """)

        # CREATE CHARGEBACK COSTS
        cur.execute(f"""DROP TABLE IF EXISTS revenue_cb_{crm_id}""")
        cur.execute(f"""
            CREATE TEMP TABLE revenue_cb_{crm_id} ON COMMIT DROP
                AS (SELECT DISTINCT ON ( crm_id, order_id ) crm_id,
                                            order_id,
                                            chargeback_date::date       AS "date",
                                            '35'::numeric AS "cost",
                                            order_total::numeric AS "order_total"
                                            FROM crm_global.orders_{crm_id}
                                            WHERE is_chargeback = '1'
                                            AND rep_last_modified >= '{max_timestamp}'::timestamp);
        
        """)
        cur.execute(f"""
                        INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp)
                        (SELECT crm_id,
                                order_id  AS "order_id",
                                date      AS "date",
                                - cost    AS "value",
                                'cb_cost' AS "type",
                                now()     AS "update_time_stamp"
                         FROM revenue_cb_{crm_id})
                         ON CONFLICT ( crm_id, order_id, type, date )
                        DO UPDATE SET value             = EXCLUDED.value,
                                      update_time_stamp = EXCLUDED.update_time_stamp;
            
        """)
        cur.execute(f"""
                              INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp)
                              (SELECT crm_id,
                                      order_id  AS "order_id",
                                      date      AS "date",
                                      - order_total    AS "value",
                                      'cb_amount' AS "type",
                                      now()     AS "update_time_stamp"
                               FROM revenue_cb_{crm_id})
                               ON CONFLICT ( crm_id, order_id, type, date )
                              DO UPDATE SET value             = EXCLUDED.value,
                                            update_time_stamp = EXCLUDED.update_time_stamp;

              """)

        # Refunds
        cur.execute(f"""DROP TABLE IF EXISTS revenue_refund_{crm_id}""")

        cur.execute(f"""
            CREATE TEMP TABLE revenue_refund_{crm_id} ON COMMIT DROP
                AS (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id,
                                                                a.order_id,
                                                                coalesce(refund_date::date, time_stamp::date)    AS "date",
                                                                coalesce(amount_refunded_to_date, refund_amount) AS "refund_amount",
                                                                b.alert_provider
                FROM crm_global.orders_{crm_id} AS "a"
                LEFT JOIN (select crm_id, order_id, alert_provider from revenue_alerts_{crm_id} where alert_provider is not NULL) AS "b" on b.crm_id = a.crm_id and b.order_id::int = a.order_id::int
                
                    WHERE coalesce(amount_refunded_to_date, refund_amount) > '0'
                      AND is_chargeback < '1'
                
                      AND a.rep_last_modified >= '{max_timestamp}'::timestamp);
                INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp, alert_provider)
                    (SELECT crm_id,
                            order_id        AS "order_id",
                            date            AS "date",
                            - refund_amount AS "value",
                            'refund'        AS "type",
                            now()           AS "update_time_stamp",
                            alert_provider
                     FROM revenue_refund_{crm_id})
                ON CONFLICT ( crm_id, order_id, type, date )
                    DO UPDATE SET value             = EXCLUDED.value,
                                  update_time_stamp = EXCLUDED.update_time_stamp,
                                  alert_provider = EXCLUDED.alert_provider;
        """)
        cur.execute(f"""
            INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp)
            (SELECT crm_id,
                    order_id        AS "order_id",
                    date            AS "date",
                    - refund_amount AS "value",
                    'refund'        AS "type",
                    now()           AS "update_time_stamp"
             FROM revenue_refund_{crm_id})
                ON CONFLICT ( crm_id, order_id, type, date )
                    DO UPDATE SET value             = EXCLUDED.value,
                                  update_time_stamp = EXCLUDED.update_time_stamp;
        """)

        # REVENUE (POSITIVE REVENUE)
        cur.execute(f"""DROP TABLE IF EXISTS revenue_revenue_{crm_id}""")
        cur.execute(f"""
                    CREATE TEMP TABLE revenue_revenue_{crm_id} ON COMMIT DROP
                    AS (SELECT DISTINCT ON ( crm_id, order_id ) crm_id,
                                                                order_id,
                                                                time_stamp::date                                                        AS "date",
                                                                CASE WHEN (decline_reason IS NULL and gateway_id <> '1') THEN order_total ELSE '0'::numeric END AS "revenue"
                        FROM crm_global.orders_{crm_id}
                        WHERE decline_reason IS NULL
                          AND rep_last_modified >= '{max_timestamp}'::timestamp);""")
        cur.execute(f"""
            INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp)
            (SELECT crm_id,
                    order_id  AS "order_id",
                    date      AS "date",
                    revenue   AS "value",
                    'revenue' AS "type",
                    now()     AS "update_time_stamp"
             FROM revenue_revenue_{crm_id}
             WHERE revenue > '0')
                ON CONFLICT ( crm_id, order_id, type, date )
                    DO UPDATE SET value             = EXCLUDED.value,
                                  update_time_stamp = EXCLUDED.update_time_stamp;
        """)
        cur.execute(f"""
            DROP TABLE IF EXISTS  ui_gateways_processor;
            CREATE TEMP TABLE ui_gateways_processor ON COMMIT DROP
            AS (SELECT b.crm_id,
                       b.gateway_id,
                       a.mid_id,
                       a.processor,
                       a.authorization_fee,
                       a.approved_transaction_cost,
                       CASE
                           WHEN a.processor ILIKE '%%flex%%charge%%' THEN '0.30'::numeric
                           WHEN a.processor ILIKE '%%virtual%%' THEN '0'::numeric
                           ELSE  '0.10'::numeric END AS "processing_cost"
                FROM ui_54407332_clients.mids AS "a"
                         INNER JOIN (SELECT DISTINCT ON ( crm_id, gateway_id ) crm_id, gateway_id, mid_id
                                     FROM ui_54407332_clients.steps) AS "b" ON b.mid_id = a.mid_id
                WHERE b.crm_id = '{crm_id}');
            
            ALTER TABLE ui_gateways_processor
                ADD CONSTRAINT crm_id_gateway_id_pk PRIMARY KEY (crm_id, gateway_id);
            
            DROP TABLE IF EXISTS revenue_transaction_costs_{crm_id};            
            CREATE
                TEMP TABLE revenue_transaction_costs_{crm_id} ON COMMIT DROP
            AS (SELECT DISTINCT ON ( a.crm_id, order_id ) a.crm_id,
                                                          order_id,
                                                          time_stamp::date          AS "date",
                                                          CASE
                                                              WHEN (decline_reason IS NULL and gateway_id <> '1') 
                                                                  THEN order_total * '0.10'::numeric
                                                              ELSE '0'::numeric END AS "reserve",
                                                          CASE
                                                              WHEN (decline_reason IS NULL and gateway_id <> '1')
                                                                  THEN order_total::numeric
                                                              ELSE '0'::numeric END AS "processing_cost",
                                                          CASE
                                                              WHEN (gateway_id <> '1')
                                                                THEN '0.35'::numeric 
                                                            ELSE '0'::numeric END AS "transaction_cost",
                                                          a.gateway_id
                FROM crm_global.orders_{crm_id} AS "a"
                WHERE rep_last_modified >= '{max_timestamp}'::timestamp);
            
            UPDATE revenue_transaction_costs_{crm_id}
            SET processing_cost = revenue_transaction_costs_{crm_id}.processing_cost::numeric * '0.1'::numeric
            /*FROM ui_gateways_processor AS "b"
            WHERE revenue_transaction_costs_{crm_id}.crm_id = b.crm_id
            AND revenue_transaction_costs_{crm_id}.gateway_id::text = b.gateway_id::text*/;
        """)
        cur.execute(f"""
            INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp)
                (SELECT crm_id,
                        order_id   AS "order_id",
                        date       AS "date",
                        - reserve  AS "value",
                        'reserves' AS "type",
                        now()      AS "update_time_stamp"
                 FROM revenue_transaction_costs_{crm_id}
                 WHERE reserve <> '0'
                   AND reserve IS NOT NULL)
            ON CONFLICT ( crm_id, order_id, type, date )
                DO UPDATE SET value             = EXCLUDED.value,
                              update_time_stamp = EXCLUDED.update_time_stamp;
        """)
        cur.execute(f"""            
            INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp)
                (SELECT crm_id,
                        order_id          AS "order_id",
                        date              AS "date",
                        - processing_cost AS "value",
                        'processing_cost' AS "type",
                        now()             AS "update_time_stamp"
                 FROM revenue_transaction_costs_{crm_id}
                 WHERE processing_cost <> '0'
                   AND processing_cost IS NOT NULL)
            ON CONFLICT ( crm_id, order_id, type, date )
                DO UPDATE SET value             = EXCLUDED.value,
                              update_time_stamp = EXCLUDED.update_time_stamp;
        """)
        cur.execute(
            f"""
            INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp)
                (SELECT crm_id,
                        order_id           AS "order_id",
                        date               AS "date",
                        - transaction_cost AS "value",
                        'transaction_cost' AS "type",
                        now()              AS "update_time_stamp"
                 FROM revenue_transaction_costs_{crm_id}
                 WHERE transaction_cost <> '0'
                   AND transaction_cost IS NOT NULL)
            ON CONFLICT ( crm_id, order_id, type, date )
                DO UPDATE SET value             = EXCLUDED.value,
                              update_time_stamp = EXCLUDED.update_time_stamp;
            
            """)
        cur.execute(f"""
            DROP TABLE IF EXISTS cog_cost;
            CREATE TEMP TABLE cog_cost ON COMMIT DROP
            AS (SELECT a.crm_id,
                       a.order_id,
                       'product_cost'                                                                 AS "type",
                       b.sku,
                       b.product_id,
                       c.cost_of_goods,
                       b.shipping_date,
                       d.order_id                                                                     AS "entered",
                       a.time_stamp,
                    /*coalesce(*/(- (c.cost_of_goods::NUMERIC + CASE
                                                                    WHEN step = '1'
                                                                        THEN '4.25'::numeric + '1'::numeric
                                                                    WHEN step > '1'
                                                                        THEN '0.25'::numeric
                                                                    ELSE '0'::numeric END))/*, '0')*/ AS "value"
                FROM (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id,
                                                                  a.order_id,
                                                                  a.step,
                                                                  a.time_stamp
                      FROM augmented_data.order_cycles_{crm_id} AS "a"
                               INNER JOIN updated_order_ids uci
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
                                     WHERE a.decline_reason IS NULL
                                       AND a.shippable = '1'
                                       AND a.rep_last_modified >= '{max_timestamp}'::timestamp) AS "b"
                                    ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                         LEFT JOIN (SELECT DISTINCT ON ( crm_id, sku ) crm_id, sku, cost_of_goods
                                    FROM crm_global.products
                                    WHERE cost_of_goods::numeric > '0'
                                        /*AND cost_of_goods::numeric < '10'*/
                                      AND cost_of_goods IS NOT NULL) AS "c"
                                   ON c.crm_id = b.crm_id AND c.sku = b.sku
                         LEFT JOIN (SELECT DISTINCT crm_id, order_id
                                    FROM reporting.ui_revenue_transactions
                                    WHERE type = 'product_cost') AS "d"
                                   ON d.crm_id = a.crm_id AND d.order_id::text = a.order_id::text);
        """)
        cur.execute(f"""
            DELETE
            FROM cog_cost
            WHERE cost_of_goods IS NULL
            /*OR entered IS NOT NULL*/;
            """)
        cur.execute(f"""
            UPDATE cog_cost
            SET shipping_date = time_stamp::date
            WHERE shipping_date = 'Not Shipped';
            """)
        cur.execute(f"""
            UPDATE cog_cost
            SET shipping_date = date_trunc('MONTH', shipping_date::date) + interval '1 day';
            """)
        cur.execute(f"""
            INSERT INTO reporting.ui_revenue_transactions (crm_id, order_id, date, value, type, update_time_stamp)
                (SELECT crm_id,
                        order_id         AS "order_id",
                        time_stamp::date AS "date",
                        - abs(value)     AS "value",
                        'product_cost'   AS "type",
                        now()            AS "update_time_stamp"
                 FROM cog_cost
                 WHERE value < '0'::numeric)
            ON CONFLICT ( crm_id, order_id, type, date )
                DO UPDATE SET value             = EXCLUDED.value,
                              update_time_stamp = EXCLUDED.update_time_stamp;
        """)

        cur.execute(f"""           
           
            DROP TABLE IF EXISTS ui_revenue_transactions_without_ancestor_temp;
            CREATE TEMP TABLE ui_revenue_transactions_without_ancestor_temp ON COMMIT DROP
            AS (SELECT DISTINCT ON ( a.crm_id, a.customer_id, a.order_id ) a.crm_id,
                                                                a.customer_id,
                                                                a.order_id,
                                                                a.ancestor_id,
                                                                a.parent_id,
                                                                a.bc_inferred,
                                                                a.retry_attempt_count,
                                                                a.attempt_count,
                                                                a.step,
                                                                a.first_affiliate,
                                                                a.campaign_id
                FROM augmented_data.order_cycles AS "a"
                         INNER JOIN (SELECT DISTINCT crm_id, order_id
                                     FROM reporting.ui_revenue_transactions
                                     WHERE crm_id = '{crm_id}'
                                       AND update_time_stamp = now()
                                       AND ancestor_id IS NULL) AS "b"
                                    ON b.crm_id = a.crm_id AND b.order_id::text = a.order_id::text);
        """)

        cur.execute("ALTER TABLE ui_revenue_transactions_without_ancestor_temp ADD PRIMARY KEY (crm_id, order_id)")
        cur.execute(f"""
            UPDATE reporting.ui_revenue_transactions
            SET ancestor_id          = a.ancestor_id,
                parent_id            = a.parent_id,
                bc_inferred          = a.bc_inferred,
                retry_attempt_count  = a.retry_attempt_count,
                attempt_count        = a.attempt_count,
                step                 = a.step,
                affid                = a.first_affiliate,
                ancestor_campaign_id = a.campaign_id
            FROM ui_revenue_transactions_without_ancestor_temp AS "a"
            WHERE ui_revenue_transactions.crm_id = a.crm_id
              AND ui_revenue_transactions.order_id::text = a.order_id::text
              AND ui_revenue_transactions.ancestor_id IS NULL;
              """)
        cur.execute(f"""
            UPDATE reporting.ui_revenue_transactions
            SET ancestor_id          = a.order_id,
                parent_id            = a.order_id,
                bc_inferred          = a.bc_inferred,
                retry_attempt_count  = a.retry_attempt_count,
                attempt_count        = a.attempt_count,
                step                 = a.step,
                affid                = a.first_affiliate,
                ancestor_campaign_id = a.campaign_id
            FROM ui_revenue_transactions_without_ancestor_temp AS "a"
            WHERE ui_revenue_transactions.crm_id = a.crm_id
              AND ui_revenue_transactions.order_id::text = a.order_id::text
              AND ui_revenue_transactions.ancestor_id IS NULL
              AND a.customer_id = '0';
        """)
        cur.execute(f"""
            DROP TABLE IF EXISTS ui_revenue_transactions_campaign_class_{crm_id};
            CREATE
                TEMP TABLE ui_revenue_transactions_campaign_class ON COMMIT DROP
            AS (SELECT a.crm_id,
                       a.campaign_id,
                       a.class,
                       a.name,
                       a.offer_id,
                       a.vertical
                FROM (SELECT a.crm_id,
                             a.campaign_id,
                             a.class,
                             b.name,
                             b.offer_id,
                             b.vertical
                      FROM ui_54407332_offers.campaigns AS "a"
                               INNER JOIN ui_54407332_offers.offers AS "b" ON b.offer_id = a.offer_id) AS "a");
            """)
        cur.execute(f"""
            UPDATE reporting.ui_revenue_transactions
            SET campaign_class = a.class,
                vertical       = a.vertical,
                offer          = a.name,
                offer_id       = a.offer_id
            FROM ui_revenue_transactions_campaign_class AS "a"
            WHERE ui_revenue_transactions.crm_id = a.crm_id
              AND ui_revenue_transactions.ancestor_campaign_id = a.campaign_id
              AND ui_revenue_transactions.update_time_stamp = now()
              AND ui_revenue_transactions.vertical IS NULL;
              """)
        cur.execute(f"""            
            DROP TABLE IF EXISTS crm_gateway_temp;
            CREATE TEMP TABLE crm_gateway_temp ON COMMIT DROP
            AS (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id, a.order_id, a.gateway_id
                FROM crm_global.orders AS "a"
                         INNER JOIN reporting.ui_revenue_transactions AS "b"
                                    ON b.crm_id = a.crm_id AND b.order_id::integer = a.order_id::integer AND
                                       b.gateway_id IS NULL AND a.crm_id = '{crm_id}'
                                        AND a.rep_last_modified >= '{max_timestamp}'::timestamp);
            """)
        #cur.execute(f"""ALTER TABLE crm_gateway_temp ADD PRIMARY KEY (crm_id, order_id);""")
        cur.execute(f"""
            UPDATE reporting.ui_revenue_transactions
            SET gateway_id = a.gateway_id
            FROM crm_gateway_temp AS "a"
            WHERE ui_revenue_transactions.crm_id = a.crm_id
              AND ui_revenue_transactions.order_id::text = a.order_id::text
              ANd ui_revenue_transactions.update_time_stamp = now()
              AND ui_revenue_transactions.gateway_id IS NULL;
              """)
        cur.execute(f"""            
            DROP TABLE IF EXISTS crm_gateway_mid_temp;
            CREATE TEMP TABLE crm_gateway_mid_temp ON COMMIT DROP
            AS (SELECT a.crm_id, a.gateway_id, a.mid_id, a.mid_number, a.close_date, a.date_added, b.processor, c.corporation_name
                FROM (SELECT DISTINCT ON ( a.crm_id, a.gateway_id ) a.crm_id, a.gateway_id, a.mid_number, a.mid_id, a.close_date, b.date_added
                      FROM ui_54407332_clients.steps AS "a"
                               LEFT JOIN ui_54407332_clients.gateway_settings AS "b"
                                         ON b.crm_id = a.crm_id AND b.gateway_id = a.gateway_id) AS "a"
                         INNER JOIN ui_54407332_clients.mids AS "b" ON b.mid_id = a.mid_id
                         INNER JOIN ui_54407332_clients.corps AS "c" ON c.corp_id = b.corp_id);
           
            UPDATE reporting.ui_revenue_transactions
            SET mid_id     = a.mid_id,
                mid_number = a.mid_number,
                processor  = a.processor,
                corp       = a.corporation_name,
                close_date = a.close_date,
                date_added = a.date_added
            FROM crm_gateway_mid_temp AS "a"
            WHERE ui_revenue_transactions.crm_id = a.crm_id
              AND ui_revenue_transactions.gateway_id:: integer = a.gateway_id:: integer
              AND ui_revenue_transactions.update_time_stamp = now()
              AND ui_revenue_transactions.mid_id IS NULL
              AND ui_revenue_transactions.crm_id = '{crm_id}';
              
              
        
        """)
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        con.rollback()
        con.close()
        raise e

