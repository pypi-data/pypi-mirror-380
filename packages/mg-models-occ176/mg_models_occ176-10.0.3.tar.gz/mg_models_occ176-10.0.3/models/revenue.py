import pandas as pd


def report(db, start_date, end_date, crm_id=False):
    if crm_id and not isinstance(crm_id, list):
        crm_id = [crm_id]
    return pd.read_sql(
        f"""
             SELECT sum(a.order_total) AS "revenue"
            FROM crm_global.orders AS "a"
            WHERE a.decline_reason IS NULL
            AND a.time_stamp >= '{start_date}'
            AND a.time_stamp <= '{end_date}' 
            { f"AND a.crm_id = any ARRAY::{crm_id}" if crm_id else ""}
        """
    )
