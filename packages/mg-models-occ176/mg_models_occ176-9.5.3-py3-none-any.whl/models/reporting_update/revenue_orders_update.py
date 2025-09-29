
def run(db, work_mem='16GB', **kw):
    conn = db.engine.raw_connection()
    cur = conn.cursor()
    try:
       # Update Continuity info
        cur.execute(f"SET LOCAL work_mem = '{work_mem}';")
        cur.execute(f"""
        DROP TABLE IF EXISTS ui_revenue_transactions_without_ancestor_temp;
        CREATE TEMP TABLE ui_revenue_transactions_without_ancestor_temp ON COMMIT DROP AS (
            SELECT /*DISTINCT ON ( a.crm_id, a.order_id )*/ a.crm_id, a.customer_id, a.order_id, a.ancestor_id, a.parent_id, a.bc_inferred, a.retry_attempt_count, a.attempt_count, a.step, a.first_affiliate 
            FROM augmented_data.order_cycles AS "a" 
            INNER JOIN ( SELECT DISTINCT crm_id, order_id FROM reporting.ui_revenue_transactions WHERE ancestor_id IS NULL ) AS "b" ON b.crm_id = a.crm_id AND b.order_id::text = a.order_id::text
        );
        UPDATE reporting.ui_revenue_transactions
        SET ancestor_id = a.ancestor_id,
            parent_id = a.parent_id,
            bc_inferred         = a.bc_inferred,
            retry_attempt_count = a.retry_attempt_count,
            attempt_count       = a.attempt_count,
            step                = a.step,
            affid               = a.first_affiliate
        FROM ui_revenue_transactions_without_ancestor_temp AS "a"
        WHERE ui_revenue_transactions.crm_id = a.crm_id
          AND ui_revenue_transactions.order_id::text = a.order_id::text
          AND ui_revenue_transactions.ancestor_id IS NULL;
        UPDATE reporting.ui_revenue_transactions
        SET ancestor_id = a.order_id,
            parent_id = a.order_id,
            bc_inferred         = a.bc_inferred,
            retry_attempt_count = a.retry_attempt_count,
            attempt_count       = a.attempt_count,
            step                = a.step,
            affid               = a.first_affiliate
        FROM ui_revenue_transactions_without_ancestor_temp AS "a"
        WHERE ui_revenue_transactions.crm_id = a.crm_id
          AND ui_revenue_transactions.order_id::text = a.order_id::text
          AND ui_revenue_transactions.ancestor_id IS NULL
        AND a.customer_id = '0';
                
        """)
        conn.commit()
        # Campaign Class
        cur.execute(f"SET LOCAL work_mem = '{work_mem}';")
        cur.execute(f"""
            DROP TABLE IF EXISTS ui_revenue_transactions_campaign_class;
            CREATE TEMP TABLE ui_revenue_transactions_campaign_class ON COMMIT DROP AS (
                        SELECT b.crm_id,
                                   b.order_id,
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
                                           INNER JOIN ui_54407332_offers.offers AS "b" ON b.offer_id = a.offer_id) AS "a"
                                     LEFT JOIN (SELECT DISTINCT ON (a.crm_id, a.order_id ) a.crm_id, a.order_id, campaign_id
                                                FROM augmented_data.order_cycles AS "a"
                                                         INNER JOIN (SELECT DISTINCT crm_id, order_id
                                                                     FROM reporting.ui_revenue_transactions
                                                                     WHERE vertical IS NULL) AS "b"
                                                                    ON b.crm_id = a.crm_id AND b.order_id::text = a.order_id::text) AS "b"
                                               ON b.crm_id = a.crm_id AND b.campaign_id = a.campaign_id);
            UPDATE reporting.ui_revenue_transactions
            SET campaign_class = a.class,
                vertical       = a.vertical,
                offer          = a.name,
                offer_id       = a.offer_id
            FROM ui_revenue_transactions_campaign_class AS "a"
            WHERE ui_revenue_transactions.crm_id = a.crm_id
              AND ui_revenue_transactions.order_id::text = a.order_id::text
              AND ui_revenue_transactions.vertical IS NULL;
        """)
        conn.commit()
        # Update the Gateway ID
        cur.execute(f"SET LOCAL work_mem = '{work_mem}';")
        cur.execute(f"""
                    UPDATE reporting.ui_revenue_transactions
                    SET gateway_id = a.gateway_id
                    FROM (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id, a.order_id, a.gateway_id 
                    FROM crm_global.orders AS "a" 
                    INNER JOIN reporting.ui_revenue_transactions AS "b" 
                    ON b.crm_id = a.crm_id AND b.order_id::integer = a.order_id::integer AND b.gateway_id IS NULL) AS "a"
                    WHERE ui_revenue_transactions.crm_id = a.crm_id
                      AND ui_revenue_transactions.order_id::text = a.order_id::text
                      AND ui_revenue_transactions.gateway_id IS NULL;
        """)
        conn.commit()
        # Update Corp and Mid Info
        cur.execute(f"SET LOCAL work_mem = '{work_mem}';")
        cur.execute(f"""
                    UPDATE reporting.ui_revenue_transactions
                    SET mid_id     = a.mid_id,
                        processor  = a.processor,
                        corp       = a.corporation_name,
                        close_date = a.close_date,
                        date_added = a.date_added
                    
                    FROM (SELECT a.crm_id, a.gateway_id, a.mid_id, a.close_date, a.date_added, b.processor, c.corporation_name
                          FROM (SELECT DISTINCT ON ( a.crm_id, a.gateway_id ) a.crm_id, a.gateway_id, a.mid_id, a.close_date, b.date_added
                                FROM ui_54407332_clients.steps AS "a"
                                LEFT JOIN ui_54407332_clients.gateway_settings AS "b" ON b.crm_id = a.crm_id AND b.gateway_id = a.gateway_id ) AS "a"
                                   INNER JOIN ui_54407332_clients.mids AS "b" ON b.mid_id = a.mid_id
                                   INNER JOIN ui_54407332_clients.corps AS "c" ON c.corp_id = b.corp_id) AS "a"
                    WHERE ui_revenue_transactions.crm_id = a.crm_id
                      AND ui_revenue_transactions.gateway_id::integer = a.gateway_id::integer
                      AND ui_revenue_transactions.mid_id IS NULL;
          """)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        cur.close()
        conn.close()
        raise e
