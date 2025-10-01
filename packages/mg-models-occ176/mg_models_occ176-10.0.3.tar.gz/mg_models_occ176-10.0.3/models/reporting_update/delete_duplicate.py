def run(db, work_mem='16GB'):
    conn = db.engine.raw_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"SET local work_mem = '{work_mem}';")
        cur.execute("""CREATE TEMP TABLE ui_revenue_transactions_duplicates ON COMMIT DROP AS 
        ( SELECT crm_id, order_id, type, max(update_time_stamp) AS "max_update" FROM reporting.ui_revenue_transactions 
        GROUP BY crm_id, order_id, type HAVING count( 1 ) > '1' ) ;
        """)
        cur.execute("""
        DELETE
        FROM reporting.ui_revenue_transactions USING ui_revenue_transactions_duplicates AS "a"
        WHERE a.crm_id = ui_revenue_transactions.crm_id
          AND a.order_id = ui_revenue_transactions.order_id
          AND a.type = ui_revenue_transactions.type
          AND ui_revenue_transactions.update_time_stamp < a.max_update;
        """)
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        cur.close()
        conn.close()
        raise e
