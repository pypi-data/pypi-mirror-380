import pandas as pd, numpy as np


def add_scrubber_stats(db, start_date, end_date=False, crm_id=None, not_crm='crm_kk', **kw):
    qry = f"""
        SELECT offer_id, provider, affid, 
            (count(1) filter ( where class = 'prepaid' ))::numeric / coalesce(nullif(count(1), 0), 1)::numeric pub_pp_rate,
            (count(1) filter ( where d.cc_first_6 is not null))::numeric / coalesce(nullif(count(1), 0), 1)::numeric pub_bin_block_rate,
            (count(1) filter ( where e.cc_first_6 is not null ))::numeric / coalesce(nullif(count(1), 0), 1)::numeric pub_bin_delay_rate,  
            (count(1) filter ( where class in('provider', 'saves') and c.cc_type  ilike 'master%%' )::numeric /
            coalesce(nullif(count(1) filter ( where class in('provider', 'saves')), '0'), '1'))::numeric pub_mc_rate
        from (select crm_id, order_id, bc_inferred,campaign_id from augmented_data.order_cycles
                        where crm_id not ilike '{not_crm}%%' and month_date >='{start_date}'::date
                        {f" and month_date <='{end_date}'::date" if end_date else ""} 
                        and bc_inferred=0 and decline_reason is null and step=1) a 
        inner join (select crm_id, campaign_id,offer_id, class from ui_54407332_offers.campaigns 
                         where crm_id not ilike '{not_crm}%%') b on b.campaign_id = a.campaign_id and b.crm_id =a.crm_id
        inner join (select crm_id, order_id, affid, c1 as provider, cc_type, cc_first_6 from crm_global.orders
                        where crm_id not ilike '{not_crm}%%' and month_date >='{start_date}'::date
                             {f" and month_date <='{end_date}'::date" if end_date else ""} 
                            and affid is not null and c1 is not null) c on c.order_id = a.order_id and c.crm_id =a.crm_id
        left join  (select crm_id, bin as cc_first_6 from ui_54407332_bins.bin_blacklist 
                         where crm_id not ilike '{not_crm}%%' and enabled is not null and enabled) d on d.cc_first_6 = c.cc_first_6  and d.crm_id =c.crm_id
        left join  (select crm_id, cc_first_6 from ui_54407332_bins.bin_delay 
                         where crm_id not ilike '{not_crm}%%' and coalesce(duration_days,0) >0) e on e.cc_first_6 = c.cc_first_6 and e.crm_id=c.crm_id

        {f"WHERE a.crm_id = '{crm_id}'" if crm_id else ""}

        group by  offer_id,provider,affid
    """
    # print(qry)
    df = pd.read_sql(qry, db.engine)
    cols = ['pub_pp_rate', 'pub_bin_block_rate', 'pub_bin_delay_rate', 'pub_mc_rate']
    df[cols] = (df[cols] * 100).round(2).astype(str) + '%'
    return df

