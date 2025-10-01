import pandas as pd
from models.reports.dependencies import ALERT_PROVIDERS, get_first_dom, now, today, _get_interval_date, get_cast, \
    get_order_by, get_filters, format_group_by


def impact_report(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, **kwargs):
    vals = initials_report(db, group_by, filters, reporting_query, order_by, inc_test_cc, discount_refunds_xcls=False, **kwargs)
    imp = vals.copy()[['crm_id', 'total', 'prepaid', 'scrubbed', 'bin delay', 'paid']]

    imp['total impact'] = ((imp.scrubbed + imp['bin delay'] + imp.prepaid) / imp.total * 100).round(3)
    msk = imp.prepaid != 0
    imp.loc[msk, 'prepaid'] = (imp.loc[msk, 'prepaid'] / imp.loc[msk, 'total'] * 100).round(3)
    msk = imp.scrubbed != 0
    imp.loc[msk, 'scrubbed'] = (imp.loc[msk, 'scrubbed'] / imp.loc[msk, 'total'] * 100).round(3)
    msk = imp['bin delay'] != 0
    imp.loc[msk, 'bin delay'] = (imp.loc[msk, 'bin delay'] / imp.loc[msk, 'total'] * 100).round(3)
    msk = imp.paid != 0
    imp.loc[msk, 'paid'] = (imp.loc[msk, 'paid'] / imp.loc[msk, 'total'] * 100).round(3)
    imp = imp.rename(columns={'prepaid': 'PP', 'scrubbed': 'All', 'bin delay': 'PP Pause', 'paid': 'Networks'})
    return imp


def initials_report(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, discount_refunds_xcls=True, **kwargs):
    f_whr = get_filters(filters)
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    group_by = format_group_by(group_by)
    ps_w = "campaign_class in('provider', 'saves')"
    ps_bd = "campaign_class in('provider', 'saves', 'block')"
    grp = ','.join(group_by)
    xl_clause = ""
    if discount_refunds_xcls:
        xl_clause = f"""
             and b.is_recurring = 1
             and (b.amount_refunded_to_date is not null and b.refund_amount is not null)
             and b.is_test_cc = 0
             and b.is_blacklisted =0
            and b.is_chargeback =0
        """


    qry = f"""
             SELECT {grp},
             count(distinct(order_id)) filter(where decline_reason is null) "total",
             count(distinct(order_id)) filter(where {ps_w} and decline_reason is null) "daily initials",
             count(distinct(order_id)) filter(where campaign_class = 'provider' and decline_reason is null) "paid",
             count(distinct(order_id)) filter(where campaign_class = 'saves' and decline_reason is null) "scrubbed",
             count(distinct(order_id)) filter(where campaign_class = 'block' and decline_reason is null) "bin delay",
             count(distinct(order_id)) filter(where campaign_class = 'prepaid' and decline_reason is null) "prepaid",    
             round(coalesce(nullif(count(distinct(order_id)) filter(where cc_type ilike 'master%%' and {ps_w} )::numeric, '0') / (count(distinct(order_id)) filter(where {ps_w}))::numeric * 100, '0'),2) as "mc%%",  
             round(coalesce(nullif(count(distinct order_id) filter(where campaign_class = 'block' and decline_reason is null), '0')::numeric / (count(distinct order_id) filter (where {ps_bd}))::numeric  * 100, '0'), 2) as "bin delay%%",                          
             round(coalesce(nullif(count(distinct order_id) filter(where campaign_class = 'saves' and decline_reason is null), '0')::numeric / (count(distinct order_id) filter(where {ps_w}))::numeric * 100, '0'), 2) as "scrub%%"                          
             FROM
            (
            select b.crm_id, b.order_id, b.affid, class as campaign_class, b.decline_reason, cc_type
            from augmented_data.order_cycles a 
            inner join crm_global.orders b on a.order_id=b.order_id and a.crm_id=b.crm_id and a.month_date =b.month_date and a.month_date >= '{sdate}'::date
            inner join (select * from ui_54407332_offers.campaigns ) c on b.crm_id = c.crm_id  and c.campaign_id=b.campaign_id /*and c.class in('provider', 'saves')*/
           /* left join (select crm_id, cc_first_6 from ui_54407332_bins.bin_delay where coalesce(duration_days, 0) >0 ) d on d.crm_id =b.crm_id and d.cc_first_6 =b.cc_first_6*/
            where a.step = 1
                and b.order_total > 0                
                and a.decline_reason is null
                {xl_clause}
                and a.bc_inferred = 0
                and a.month_date >= '{sdate}'
                and a.month_date <  '{edate}' ) a

        GROUP BY {grp}
        ORDER BY  {get_order_by(group_by, group_by)};
    """
    res = pd.read_sql(
        qry,
        db.engine
    )
    return res







