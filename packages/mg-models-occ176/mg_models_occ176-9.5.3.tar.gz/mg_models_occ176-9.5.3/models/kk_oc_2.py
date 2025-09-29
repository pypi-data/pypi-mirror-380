cur.execute("""SET LOCAL WORK_MEM = '4GB';""")
#THIS IS WHERE THE CUSTOMERS TO TABLE THING IS CREATED TO JOIN OFF IRRELEVANT CUSTOMERS TO THE UPDATE
if customer_ids:
    cur.execute(f"""CREATE TEMP TABLE customers_to_table on commit drop as (select unnest(ARRAY [customer_ids]::numeric[]) as customer_id);""")

cur.execute(f"""CREATE TEMP TABLE temp_cycle_full
(
    crm_id                   text,
    order_id                 numeric                 not null
        constraint temp_cycle_full_pk
            primary key,
    bc_raw                   numeric,
    bc_inferred              numeric,
    bc_increment             integer,
    attempt_increment        integer,
    attempt_decrement        integer,
    attempt_count            integer,
    retry_attempt_count      integer,
    real_attempt_count       integer,
    real_retry_attempt_count integer,
    last_child               numeric,
    real_last_child          numeric,
    parent_id                numeric,
    campaign_id              numeric,
    customer_id              numeric,
    insert_time              timestamp default now() not null,
    decline_reason           text,
    time_stamp               timestamp,
    acquisition_date         timestamp,
    step                     numeric,
    first_affiliate          text,
    adv_portfolio            text,
    existing                 boolean,
    ancestor_id              numeric,
    source                   text,
    ignore_in_reporting      boolean
)
    ON COMMIT DROP;""")



cur.execute(f"""CREATE TEMP TABLE orders_array ON COMMIT DROP AS (
    SELECT DISTINCT ON ( a.transaction_id ) a.transaction_id                             AS "order_id",
                                            a.customer_id,
                                            a.date_created                               AS "time_stamp",

                                            '{self.crm_id}'                                   AS "crm_id",
                                            a.source_value1                              AS "affiliate",
                                            CASE
                                                WHEN a.response_type = 'SUCCESS' AND a.order_type = 'NEW_SALE' THEN NULL::text
                                                ELSE a.response_text END                 AS "decline_reason",
                                            coalesce(step_1.step, step_1_1.step)         AS "step",
                                            coalesce(step_1.offer_id, step_1_1.offer_id) AS "offer_id",
                                            a.billing_cycle_number                       AS "billing_cycle",
                                            b.campaign_id,
                                            c.product_id,
                                            d.campaign_product_id,
                                            step_1.step                                  AS "step_1",
                                            step_1_1.step                                AS "step_2",
                                            coalesce(e.decrement_attempt_count, '0')     AS "decrement_attempt_count"
    FROM {self.crm_id}.transactions AS "a"
             INNER JOIN customers_to_table AS x ON x.customer_id = a.customer_id
             INNER JOIN {self.crm_id}.orders AS "b" ON b.order_id = a.order_id
             INNER JOIN {self.crm_id}.transaction_items AS "c" ON c.transaction_id = a.transaction_id
             INNER JOIN {self.crm_id}.products AS "d" ON d.campaign_product_id = c.product_id
             LEFT JOIN ui_54407332_offers.offer_globals AS "step_1"
                       ON step_1.crm_id = '{self.crm_id}' AND step_1.charge_product_id = d.product_id
             LEFT JOIN ui_54407332_offers.offer_globals AS "step_1_1"
                       ON step_1_1.crm_id = '{self.crm_id}' AND step_1_1.rebill_product_id = d.product_id
             LEFT JOIN augmented_data.order_cycles AS e
                       ON e.crm_id = '{self.crm_id}' AND e.order_id = a.transaction_id
    WHERE a.txn_type = 'SALE'
      AND a.card_type <> 'TESTCARD');""")



cur.execute("""alter table orders_array
    add constraint orders_array_pkey
        primary key (order_id);""")



cur.execute("""UPDATE orders_array
    SET decrement_attempt_count = '1'
    FROM (SELECT decline_reason FROM augmented_data.decline_reason_decrement) AS a
    WHERE lower(orders_array.decline_reason) = lower(a.decline_reason)
      AND orders_array.decline_reason IS NOT NULL
      AND orders_array.decrement_attempt_count = '0';""")


cur.execute(f"""INSERT INTO temp_cycle_full (crm_id, order_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                             attempt_count,
                             retry_attempt_count, parent_id, campaign_id, customer_id, insert_time,
                             decline_reason,
                             time_stamp, acquisition_date, step, first_affiliate, adv_portfolio, existing,
                             attempt_decrement) (
    SELECT a.crm_id,
           a.order_id,
           a.billing_cycle::smallint,
           CASE WHEN a.customer_id = '0' THEN '0' ELSE e.b_c END::smallint,
           NULL::smallint,
           NULL::smallint,
           NULL::smallint,
           NULL::smallint,
           NULL::bigint,
           a.campaign_id,
           a.customer_id,
           a.time_stamp,
           a.decline_reason,
           a.time_stamp::timestamp with time zone,
           e.acquisition_date,
           e.step::smallint,
           e.affiliate::text,
           CASE WHEN e.offer_id IS NULL THEN 'undefined'::text ELSE e.offer_id::text END,
           CASE WHEN b.order_id IS NULL THEN FALSE::boolean ELSE TRUE::boolean END,
           a.decrement_attempt_count
    FROM orders_array AS a
             LEFT JOIN (SELECT max(order_id) AS order_id
                        FROM augmented_data.order_cycles
                        WHERE crm_id = '{self.crm_id}'
                        GROUP BY order_id) AS b
                       ON (b.order_id = a.order_id)
             LEFT JOIN (SELECT a.customer_id,
                               a.step,
                               a.order_id,
                               (sum(a.b_c)
                                OVER ( PARTITION BY a.customer_id, a.offer_id, a.step ORDER BY a.time_stamp ASC)) AS b_c,
                               e.time_stamp_to_acquisition_date                                                   AS acquisition_date,
                               e.affiliate,
                               a.offer_id
                        FROM (SELECT a.customer_id,
                                     a.step,
                                     a.order_id,
                                     a.incrementer,
                                     a.offer_id,
                                     a.campaign_id,
                                     (lag(a.incrementer, '1'::smallint, '0'::smallint)
                                      OVER ( PARTITION BY a.customer_id, a.offer_id, a.step ORDER BY a.time_stamp ASC)) AS b_c,
                                     a.time_stamp
                              FROM (SELECT a.customer_id,
                                           a.step,
                                           a.order_id,
                                           b.decline_reason,
                                           CASE
                                               WHEN b.decline_reason IS NULL THEN '1'::smallint
                                               ELSE '0'::smallint END AS incrementer,
                                           a.offer_id,
                                           a.time_stamp,
                                           a.campaign_id

                                    FROM orders_array AS a
                                             LEFT JOIN (SELECT DISTINCT ON (order_id) order_id, decline_reason
                                                        FROM orders_array) AS b
                                                       ON (b.order_id = a.order_id)
                                    ORDER BY a.customer_id, a.step, a.order_id) AS a) AS a
                                 LEFT JOIN (SELECT a.customer_id,
                                                   a.order_id,
                                                   a.affiliate,
                                                   a.time_stamp AS time_stamp_to_acquisition_date
                                            FROM orders_array AS a
                                                     INNER JOIN (SELECT DISTINCT ON ( orders.order_id, orders.customer_id ) orders.order_id,
                                                                                                                            orders.customer_id
                                                                 FROM orders_array AS orders
                                                                          INNER JOIN (SELECT customer_id, min(order_id) AS "order_id"
                                                                                      FROM orders_array
                                                                                      WHERE decline_reason IS NULL
                                                                                      GROUP BY customer_id)
                                                                     AS "b"
                                                                                     on b.customer_id = orders.customer_id and b.order_id = orders.order_id
                                            ) AS b
                                                                ON (b.order_id = a.order_id)) AS e
                                           ON (e.customer_id = a.customer_id)) AS e
                       ON (e.order_id = a.order_id)
);""")

cur.execute("""UPDATE temp_cycle_full
SET parent_id = a.parent_id
FROM (SELECT a.order_id, CASE WHEN a.bc_inferred = '0' THEN a.order_id ELSE b.order_id END AS parent_id
      FROM (SELECT order_id, bc_inferred, customer_id, step, campaign_id, adv_portfolio FROM temp_cycle_full) AS a
               LEFT JOIN (SELECT order_id,
                                 customer_id,
                                 step,
                                 adv_portfolio,
                                 campaign_id,
                                 bc_inferred + '1' AS bc_inferred
                          FROM temp_cycle_full
                          WHERE decline_reason IS NULL) AS b
                         ON (b.customer_id = a.customer_id AND b.step = a.step AND
                             b.bc_inferred = a.bc_inferred AND b.adv_portfolio = a.adv_portfolio /*AND
                                             b.campaign_id = a.campaign_id*/)
     ) AS a
WHERE temp_cycle_full.order_id = a.order_id;""")



cur.execute("""UPDATE temp_cycle_full
SET ancestor_id = a.ancestor
FROM (SELECT customer_id, step, adv_portfolio, min(order_id) AS ancestor
      FROM temp_cycle_full
      WHERE decline_reason IS NULL
      GROUP BY customer_id, step, adv_portfolio) AS a
WHERE temp_cycle_full.customer_id = a.customer_id
  AND temp_cycle_full.step = a.step
  AND temp_cycle_full.adv_portfolio = a.adv_portfolio;""")


cur.execute("""UPDATE temp_cycle_full
SET attempt_count      = a.attempt,
    real_attempt_count = a.non_attempt
FROM (SELECT orders.order_id,
             CASE
                 WHEN orders.bc_inferred = '1' THEN
                         (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2' -
                         (sum(orders.attempt_decrement)
                          OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                 ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1' -
                      (sum(orders.attempt_decrement)
                       OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC ))
                 END AS attempt,
             CASE
                 WHEN orders.bc_inferred = '1' THEN
                         (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '2'
                 ELSE (dense_rank() OVER ( PARTITION BY orders.parent_id ORDER BY orders.order_id ASC)) - '1'
                 END AS non_attempt
      FROM temp_cycle_full AS orders) AS a
WHERE temp_cycle_full.order_id = a.order_id;""")

cur.execute("""UPDATE temp_cycle_full
SET attempt_count = '0'
WHERE attempt_count < '0';""")

cur.execute("""UPDATE temp_cycle_full
SET real_last_child = a.last_child
FROM (SELECT parent_id, max(order_id) AS last_child FROM temp_cycle_full GROUP BY parent_id) AS a
WHERE a.parent_id = temp_cycle_full.order_id;""")



cur.execute("""UPDATE temp_cycle_full
SET last_child = a.last_child
FROM (SELECT parent_id, max(order_id) AS last_child
      FROM temp_cycle_full
      WHERE attempt_decrement = '0'
      GROUP BY parent_id) AS a
WHERE a.parent_id = temp_cycle_full.order_id;""")



cur.execute("""UPDATE temp_cycle_full
SET retry_attempt_count = a.retry_attempt_count
FROM (SELECT orders.order_id,
             a.attempt_count      AS retry_attempt_count,
             a.real_attempt_count AS real_retry_attempt_count

      from temp_cycle_full AS orders
               LEFT JOIN (SELECT min(parent_id)                                      AS start_id,
                                 bc_inferred,
                                 adv_portfolio,
                                 customer_id,
                                 step,
                                 count(attempt_count) - '1' - sum(attempt_decrement) AS attempt_count,
                                 count(attempt_count) - '1'                          AS real_attempt_count
                          FROM temp_cycle_full
                          WHERE order_id <> parent_id
                          GROUP BY adv_portfolio, customer_id, step, bc_inferred) AS a
                         ON (a.customer_id = orders.customer_id AND a.adv_portfolio = orders.adv_portfolio AND
                             a.start_id = orders.order_id)
      WHERE a.start_id IS NOT NULL) AS a
WHERE temp_cycle_full.order_id = a.order_id;""")

# #cur.execute("""SELECT *
# FROM temp_cycle_full WHERE bc_inferred > '0'
# ORDER BY customer_id;""")

# cur.execute("""SELECT a.order_id, a.bc_inferred, b.bc_inferred FROM temp_cycle_full AS "a" LEFT JOIN augmented_data.order_cycles_{self.crm_id} AS "b" ON b.crm_id = a.crm_id AND b.order_id = a.order_id WHERE b.bc_inferred <> a.bc_inferred  ;""")


cur.execute("""INSERT INTO augmented_data.order_cycles (order_id, crm_id, bc_raw, bc_inferred, bc_increment, attempt_increment,
                                         decrement_attempt_count, attempt_count, retry_attempt_count,
                                         real_attempt_count,
                                         real_retry_attempt_count, last_child, real_last_child, parent_id, campaign_id,
                                         customer_id, decline_reason, time_stamp, month_date,
                                         acquisition_date,
                                         step,
                                         first_affiliate, ancestor_id)
    (SELECT DISTINCT ON (order_id) order_id,
                                   crm_id,
                                   bc_raw,
                                   bc_inferred,
                                   bc_increment,
                                   attempt_increment,
                                   attempt_decrement,
                                   attempt_count,
                                   retry_attempt_count,
                                   real_attempt_count,
                                   real_retry_attempt_count,
                                   last_child,
                                   real_last_child,
                                   parent_id,
                                   campaign_id,
                                   customer_id,
                                   decline_reason,
                                   time_stamp,
                                   time_stamp::date,
                                   acquisition_date,
                                   step,
                                   first_affiliate,
                                   ancestor_id
     FROM temp_cycle_full
     WHERE existing IS FALSE);""")



cur.execute("""UPDATE augmented_data.order_cycles
SET crm_id                   = a.crm_id,
    order_id                 = a.order_id,
    bc_raw                   = a.bc_raw,
    bc_inferred              = a.bc_inferred,
    bc_increment             = a.bc_increment,
    attempt_increment        = a.attempt_increment,
    decrement_attempt_count  = a.attempt_decrement,
    attempt_count            = a.attempt_count,
    retry_attempt_count      = a.retry_attempt_count,
    real_attempt_count       = a.real_attempt_count,
    real_retry_attempt_count = a.real_retry_attempt_count,
    last_child               = a.last_child,
    real_last_child          = a.real_last_child,
    parent_id                = a.parent_id,
    campaign_id              = a.campaign_id,
    customer_id              = a.customer_id,
    decline_reason           = a.decline_reason,
    time_stamp               = a.time_stamp,
    acquisition_date         = a.acquisition_date,
    step                     = a.step,
    first_affiliate          = a.first_affiliate,
    ancestor_id              = a.ancestor_id
FROM (SELECT crm_id,
             order_id,
             bc_raw,
             bc_inferred,
             bc_increment,
             attempt_increment,
             attempt_decrement,
             attempt_count,
             retry_attempt_count,
             real_attempt_count,
             real_retry_attempt_count,
             last_child,
             real_last_child,
             parent_id,
             campaign_id,
             customer_id,
             decline_reason,
             time_stamp,
             time_stamp::date as month_date,
             acquisition_date,
             step,
             first_affiliate,
             ancestor_id
      FROM temp_cycle_full
      WHERE existing IS TRUE) AS a
WHERE order_cycles.crm_id = a.crm_id
  AND order_cycles.order_id = a.order_id
  AND order_cycles.month_date = a.month_date;""")


