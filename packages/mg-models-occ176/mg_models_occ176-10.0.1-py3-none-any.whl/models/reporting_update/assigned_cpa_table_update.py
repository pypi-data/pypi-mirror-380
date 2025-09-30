#TODO ADD CPA MULTIPLIER
def run(db, *crm_ids, min_acquisition_date='2022-05-01', overwrite=False):
    con = db.engine.raw_connection()
    cur = con.cursor()
    _in_crm_ids = "','".join(crm_ids)

    try:
        cur.execute(
            f"""
            DROP TABLE IF EXISTS assigned_cpa_orders_pre;
            CREATE TEMP TABLE assigned_cpa_orders_pre
            (
                crm_id           TEXT NOT NULL,
                order_id         TEXT NOT NULL,
                offer_id         NUMERIC,
                provider         TEXT,
                affiliate        TEXT,
                step             NUMERIC,
                acquisition_date TIMESTAMP,
                cpa              NUMERIC,
                credit           NUMERIC,
                CONSTRAINT assigned_cpa_orders_pk
                    PRIMARY KEY (crm_id, order_id)
            );
            SET LOCAL work_mem = '16GB';
            SET local timezone = 'America/Toronto';


            INSERT INTO assigned_cpa_orders_pre (crm_id, order_id, offer_id, provider, affiliate, step,
                                     acquisition_date, cpa) (SELECT DISTINCT ON ( a.crm_id, a.order_id ) a.crm_id,
                                                                                                    a.order_id,
                                                                                                    b.offer_id,
                                                                                                    lower(coalesce(d.provider_map, a.c1)),
                                                                                                    a.affiliate,
                                                                                                    a.step,
                                                                                                    a.acquisition_date,
                                                                                                    a.cpa
                                                        FROM (SELECT a.crm_id,
                                                                     a.order_id,
                                                                     a.campaign_id,
                                                                     a.step,
                                                                     coalesce(c.ancestor_acquisition_date, a.acquisition_date) AS "acquisition_date",
                                                                     a.bc_inferred,
                                                                     a.decline_reason,
                                                                     a.month_date,
                                                                     b.email_address,
                                                                     b.is_test_cc,
                                                                     b.cc_type,
                                                                     b.c1,
                                                                     b.affiliate,
                                                                     b.opt::numeric * coalesce(d.cpa_multiplier, 100)::numeric  AS "cpa"
                                                              FROM augmented_data.order_cycles AS "a"
                                                                       INNER JOIN (SELECT DISTINCT ON ( crm_id, order_id ) crm_id,
                                                                                                                           order_id,
                                                                                                                           c1,
                                                                                                                           gateway_id,
                                                                                                                           affiliate,
                                                                                                                           cc_type,
                                                                                                                           email_address,
                                                                                                                           is_test_cc,
                                                                                                                           month_date,
                                                                                                                           opt
                                                                                   FROM crm_global.orders
                                                                                   WHERE decline_reason IS NULL AND crm_id IN ('{_in_crm_ids}') AND opt ~ '^[0-9]+(\.[0-9]+)?$') AS "b"
                                                                                  ON b.crm_id = a.crm_id AND b.order_id = a.order_id /*AND b.month_date = a.month_date*/
                                                                       LEFT JOIN (SELECT a.crm_id,
                                                                                         a.ancestor_id,
                                                                                         a.ancestor_acquisition_date
                                                                                  FROM (SELECT crm_id,
                                                                                               ancestor_id,
                                                                                               min(time_stamp) AS "ancestor_acquisition_date"
                                                                                        FROM augmented_data.order_cycles
                                                                                        WHERE decline_reason IS NULL AND crm_id IN ('{_in_crm_ids}')
                                                                                        GROUP BY crm_id, ancestor_id) AS "a") AS "c"
                                                                                 ON c.crm_id = a.crm_id AND c.ancestor_id = a.ancestor_id
                                                                       LEFT JOIN (SELECT crm_id, cpa_multiplier FROM ui_54407332_clients.instance_data WHERE crm_id IN ('{_in_crm_ids}')) as "d"
                                                                                ON d.crm_id = a.crm_id
                                                              WHERE a.month_date > '{min_acquisition_date}'::date
                                                                AND upper(b.cc_type) <> 'TESTCARD'
                                                                AND b.email_address NOT ILIKE '%%test%%'
                                                                AND b.is_test_cc = '0'
                                                                AND a.crm_id IN ('{_in_crm_ids}')
                                                                AND a.bc_inferred = '0'
                                                                AND a.step = '1'
                                                               
                                                                AND a.decline_reason IS NULL) AS "a"
                                                                 INNER JOIN ui_54407332_offers.campaigns AS "b"
                                                                            ON b.crm_id::text = a.crm_id::text AND
                                                                               b.campaign_id::text = a.campaign_id::text
                                                                 LEFT JOIN reporting.provider_map AS "d" ON lower(d.provider) = lower(a.c1)
                                                                 LEFT JOIN reporting.assigned_cpa_orders AS "e"
                                                                           ON e.crm_id = a.crm_id AND e.order_id::text = a.order_id::text
                                                        WHERE b.class = 'provider'
                                                          AND e.order_id IS NULL
                                                          AND a.acquisition_date > '{min_acquisition_date}'::date/*
                                                          AND lower(coalesce(d.provider_map, c.c1)) = 'intelligent media'*/);
            {f"DELETE FROM reporting.assigned_cpa_orders where crm_id IN ('{_in_crm_ids}');" if overwrite else ""}
            INSERT INTO reporting.assigned_cpa_orders (crm_id, order_id, offer_id, provider, affiliate, step,
               acquisition_date, cpa, credit) (SELECT a.crm_id,
                                                      a.order_id,
                                                      a.offer_id,
                                                      a.provider,
                                                      a.affiliate,
                                                      a.step,
                                                      a.acquisition_date,
                                                      a.cpa,
                                                      a.credit
                                               FROM assigned_cpa_orders_pre AS "a"
                                                        LEFT JOIN reporting.assigned_cpa_orders AS "b"
                                                                  ON b.crm_id = a.crm_id AND b.order_id = a.order_id
                                               WHERE b.order_id IS NULL);

                DROP TABLE assigned_cpa_orders_pre;
            """
        )
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        con.rollback()
        cur.close()
        con.close()
        raise e
