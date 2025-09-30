
def run(db, *crm_ids, **kw):
    conn = db.engine.raw_connection()
    cur = conn.cursor()
    if not len(crm_ids):
        raise Exception('Must pass at least 1 crm_id')
    try:
        cur.execute(f"""
            INSERT INTO ui_filter_values.affid (filter_display_value, filter_query_value) (SELECT DISTINCT affiliate, affiliate
                                                                                   FROM crm_global.orders AS "a"
                                                                                            LEFT JOIN ui_filter_values.affid AS "b" ON b.filter_query_value = a.affiliate
                                                INNER JOIN ui_filter_values.crm_id AS c ON c.filter_query_value = a.crm_id
                                                                                   WHERE b.filter_query_value IS NULL
                                                                                     AND a.affiliate IS NOT NULL);
            INSERT INTO ui_filter_values.vertical (filter_display_value, filter_query_value) (SELECT DISTINCT a.vertical, a.vertical
                                                                                              FROM ui_54407332_offers.offers AS "a"
                                                                                                       LEFT JOIN ui_filter_values.vertical AS "b" ON b.filter_query_value = a.vertical
            --											INNER JOIN ui_filter_values.crm_id AS c ON c.filter_query_value = a.crm_id
                                                                                              WHERE b.filter_query_value IS NULL);
            INSERT INTO ui_filter_values.corp (filter_display_value, filter_query_value) (SELECT a.corporation_name, a.corporation_name
                                                                                          FROM (SELECT DISTINCT corporation_name
                                                                                                FROM ui_54407332_clients.corps
                                                                                                WHERE corporation_name IS NOT NULL AND archived IS FALSE) AS "a"
                                                                                                   LEFT JOIN ui_filter_values.corp AS "b"
                                                                                                             ON b.filter_query_value = a.corporation_name
                                                                                          WHERE b.filter_query_value IS NULL);
            INSERT INTO ui_filter_values.offer (filter_display_value, filter_query_value) (SELECT DISTINCT name, name
                                                                                           FROM ui_54407332_offers.offers AS "a"
                                                                                                    LEFT JOIN ui_filter_values.offer AS "b" ON b.filter_query_value = a.name
            --											INNER JOIN ui_filter_values.crm_id AS c ON c.filter_query_value = a.crm_id
                                                                                           WHERE b.filter_query_value IS NULL);
            INSERT INTO ui_filter_values.mid_number (filter_display_value, filter_query_value) (SELECT DISTINCT coalesce(b.filter_display_value, a.mid_number ), a.mid_number
                                                                                  FROM ui_54407332_clients.steps AS "a"
                                                                                           LEFT JOIN ui_filter_values.mid_number AS "b" ON b.filter_query_value = a.mid_number
											   INNER JOIN ui_filter_values.crm_id AS c ON c.filter_query_value = a.crm_id
                                                                                  WHERE b.filter_query_value IS NULL AND a.mid_number IS NOT NULL);
            INSERT INTO ui_filter_values.processor (filter_display_value, filter_query_value) (SELECT DISTINCT coalesce( b.filter_display_value, a.processor ), a.processor
                                                                                  FROM ui_54407332_clients.mid_template AS "a"
                                                                                	LEFT JOIN ui_filter_values.processor AS "b" ON b.filter_query_value = a.processor
                                                                                  WHERE b.filter_query_value IS NULL);
            """)
        conn.commit()
        # CRM SPECIFIC
        for c in crm_ids:
            qry = f"""
                INSERT INTO ui_filter_values.provider (filter_display_value, filter_query_value) (SELECT DISTINCT c1, c1
                                                                                  FROM crm_global.orders_{c} AS "a"
                                                                                           LEFT JOIN ui_filter_values.provider AS "b" ON b.filter_query_value = a.c1
											   INNER JOIN ui_filter_values.crm_id AS c ON c.filter_query_value = a.crm_id
                                                                                  WHERE c1 IS NOT NULL
                                                                                    AND b.filter_query_value IS NULL);
            """
            try:
                cur.execute(qry)
                conn.commit()
            except Exception as ex:
                conn.rollback()
                print(f'Filter Insert Error on crm {c} - error: {str(ex)}')
        cur.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        cur.close()
        conn.close()
        raise e