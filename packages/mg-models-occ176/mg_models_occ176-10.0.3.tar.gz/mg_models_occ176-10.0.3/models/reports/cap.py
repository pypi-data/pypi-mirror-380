import pandas as pd


def ui_cap_report(db, crms=None):
    if crms and not isinstance(crms, list):
        crms = [crms]
    qry = f"""
        select mid_id,
       mid_number,
       step,
       daily_available,
       monthly_available,
       available_tc trailing30_available

      from (select a.*,  b.daily_available, b.monthly_available, c.available_tc
            from (select distinct on (mid_id, step) mid_id, step,  mid_number from ui_54407332_clients.steps 
            where mid_number is not null 
                and step is not null
                {f"and crm_id = Any(ARRAY{crms}::text[])" if crms else "and not archived"}
            ) a
                left join processing.cap b on a.mid_id = b.mid_id and b.step = a.step
                left join processing.trailing_cap c on c.mid_id = a.mid_id and c.step = a.step
       
     ) a;
    """
    df = pd.read_sql(qry, db.engine)
    df[['mid_number', 'step']] = df[['mid_number', 'step']].fillna('')
    df[['daily_available', 'monthly_available', ' trailing30_available']] = df[['daily_available', 'monthly_available', 'trailing30_available']].fillna(0)
    return df