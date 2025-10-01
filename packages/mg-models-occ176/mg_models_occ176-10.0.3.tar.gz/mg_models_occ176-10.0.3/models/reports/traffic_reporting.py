import pandas as pd


def count_clicks(db, start_ts, end_ts):
    qry = f"""
        select
            count(1) as total_clicks
        from bro_clicks.click_funnel_2
        where time_stamp_x::date between '{start_ts}' and '{end_ts}'
    """
    df = pd.read_sql(qry, db)
    return df


def count_loaded(db, start_ts, end_ts):
    qry = f"""
        select 
            count(1) as total_loaded
        from bro_clicks.click_funnel_2
        where time_stamp_x::date between '{start_ts}' and '{end_ts}'
    """
    df = pd.read_sql(qry, db)
    return df



def provider_count(db, start_ts, end_ts):
    qry = f"""
        select
            provider,
            count(1) as provider_clicks
        from bro_clicks.click_funnel_2
        where time_stamp_x::date between '{start_ts}' and '{end_ts}'
        group by provider
    """
    df = pd.read_sql(qry, db)
    return df


def test(db):
    qry = """select click_id from bro_clicks.clicks limit 1"""
    df = pd.read_sql(qry, db)
    return df


def binary_variates(db, start_ts, end_ts):
    qry = f"""
        select
            sum(case when is_always_show_mc_total = 1 then 1 else 0 end)  as always_show_mc_total_1,
            sum(case when is_always_show_mc_total = 0 then 1 else 0 end)  as always_show_mc_total_0,
            sum(case when is_auto_play = 1 then 1 else 0 end)  as is_auto_play_1,
            sum(case when is_auto_play = 0 then 1 else 0 end)  as is_auto_play_0,
            sum(case when is_show_loading = 1 then 1 else 0 end) as is_show_loading_1,
            sum(case when is_show_loading = 0 then 1 else 0 end) as is_show_loading_0,
            sum(case when is_show_loading_mc_promo = 1 then 1 else 0 end) as is_show_loading_mc_promo_1,
            sum(case when is_show_loading_mc_promo = 0 then 1 else 0 end) as is_show_loading_mc_promo_0,
            sum(case when is_show_mc_promo_popup = 1 then 1 else 0 end) as is_show_mc_promo_popup_1,
            sum(case when is_show_mc_promo_popup = 0 then 1 else 0 end) as is_show_mc_promo_popup_0,
            sum(case when is_show_mc_promo_card = 1 then 1 else 0 end) as is_show_mc_promo_card_1,
            sum(case when is_show_mc_promo_card = 0 then 1 else 0 end) as is_show_mc_promo_card_0,
            sum(case when is_show_multiple_mc_promos = 1 then 1 else 0 end) as is_show_multiple_mc_promos_1,
            sum(case when is_show_multiple_mc_promos = 0 then 1 else 0 end) as is_show_multiple_mc_promos_0,
            sum(case when is_show_original_price = 1 then 1 else 0 end) as is_show_original_price_1,
            sum(case when is_show_original_price = 0 then 1 else 0 end) as is_show_original_price_0,
            sum(case when is_show_tos_disclaimer = 1 then 1 else 0 end) as is_show_tos_disclaimer_1,
            sum(case when is_show_tos_disclaimer = 0 then 1 else 0 end) as is_show_tos_disclaimer_0,
            sum(case when is_st = 1 then 1 else 0 end) as is_st_1,
            sum(case when is_st = 0 then 1 else 0 end) as is_st_0,
            sum(case when is_stp_t = 1 then 1 else 0 end) as is_stp_t_1,
            sum(case when is_stp_t = 0 then 1 else 0 end) as is_stp_t_0
        from bro_clicks.click_funnel_2
        where approved = 1
        and time_stamp_x::date between '{start_ts}' and '{end_ts}';
    """
    df = pd.read_sql(qry, db)
    return df


def loaded_cvr(db, start_ts, end_ts):
    qry = f"""
        select
           x             as approved,
           n             as loaded_clicks,
           intervals.p   as conversion_rate,
           se            as stand_err
        from (select rates.*,
                     sqrt(p * (1 - p) / n) as se
              from (select conversions.*,
                           x / n::float as p
                    from (select
                                 count(1)                                      as n,
                                 sum(case when approved = 1 then 1 else 0 end) as x
                          from bro_clicks.click_funnel_2
                          where client_loaded = 1 and
                          time_stamp_x::date between '{start_ts}' and '{end_ts}'
                          ) as conversions) as rates) as intervals;
    """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def cvr(db, start_ts, end_ts):
    qry = f"""
            select
               x             as approved,
               n             as all_clicks,
               intervals.p   as conversion_rate,
               se            as stand_err
            from (select rates.*,
                         sqrt(p * (1 - p) / n) as se
                  from (select conversions.*,
                               x / n::float as p
                        from (select
                                     count(1)                                      as n,
                                     sum(case when approved = 1 then 1 else 0 end) as x
                              from bro_clicks.click_funnel_2
                              where time_stamp_x::date between '{start_ts}' and '{end_ts}'
                              ) as conversions) as rates) as intervals;
        """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def intent(db, start_ts, end_ts):
    qry = f"""
            select
               x             as click_submitted,
               n             as all_clicks,
               intervals.p   as intent_rate,
               se            as stand_err
            from (select rates.*,
                         sqrt(p * (1 - p) / n) as se
                  from (select conversions.*,
                               x / n::float as p
                        from (select
                                     count(1)                                      as n,
                                     sum(case when click_submit = 1 then 1 else 0 end) as x
                              from bro_clicks.click_funnel_2
                              where time_stamp_x::date between '{start_ts}' and '{end_ts}'
                              ) as conversions) as rates) as intervals;
        """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def loaded_intent(db, start_ts, end_ts):
    qry = f"""
            select
               x             as click_submitted,
               n             as loaded_clicks,
               intervals.p   as intent_rate,
               se            as stand_err
            from (select rates.*,
                         sqrt(p * (1 - p) / n) as se
                  from (select conversions.*,
                               x / n::float as p
                        from (select
                                     count(1)                                      as n,
                                     sum(case when click_submit = 1 then 1 else 0 end) as x
                              from bro_clicks.click_funnel_2
                              where time_stamp_x::date between '{start_ts}' and '{end_ts}'
                              and client_loaded = 1
                              ) as conversions) as rates) as intervals;
        """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def bounce_rate(db, start_ts, end_ts):
    qry = f"""
                select
                   x             as loaded_clicks,
                   n             as all_clicks,
                   intervals.p   as bounce_rate,
                   se            as stand_err
                from (select rates.*,
                             sqrt(p * (1 - p) / n) as se
                      from (select conversions.*,
                                   x / n::float as p
                            from (select
                                         count(1) as n,
                                         sum(case when client_loaded = 1 then 1 else 0 end) as x
                                  from bro_clicks.click_funnel_2
                                  where time_stamp_x::date between '{start_ts}' and '{end_ts}'
                                  ) as conversions) as rates) as intervals;
            """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def steps(db, start_ts, end_ts):
    qry = f"""                                                                                                                     
    select
        sum(case when page like '%%checkout%%' and event = 'click_submit' and approved = 1 then 1 else 0 end) as step_1,
        sum(case when page like '%%upsell'     and event = 'click_submit' and approved = 1 then 1 else 0 end) as step_2_upsell,
        sum(case when event = 'click_submit_page_order_1' and approved = 1 then 1 else 0 end) as step_3_upsell_1,
        sum(case when event = 'click_submit_page_order_2' and approved = 1 then 1 else 0 end) as step_4_upsell_2,
        sum(case when event = 'click_submit_page_order_3' and approved = 1 then 1 else 0 end) as step_5_upsell_3,
        sum(case when event = 'click_submit_page_order_4' and approved = 1 then 1 else 0 end) as step_6_upsell_4,
        sum(case when event = 'click_submit_page_order_5' and approved = 1 then 1 else 0 end) as step_7_upsell_5,
        sum(case when event = 'click_submit_page_order_6' and approved = 1 then 1 else 0 end) as step_8_upsell_6,
        sum(case when event = 'click_submit_page_order_7' and approved = 1 then 1 else 0 end) as step_9_upsell_7,
        sum(case when page like '%%thank%%'    and event = 'client_loaded' then 1 else 0 end) as step_10_thanks
    from (select page, event, approved, time_stamp, time_stamp_x
          from bro_clicks.clicks
          inner join
              (select click_id, approved, time_stamp_x
               from bro_clicks.click_funnel_2
               where time_stamp_x between '{start_ts}'
                   and '{end_ts}') as a
          on a.click_id = clicks.click_id ) as b
    where time_stamp between '{start_ts}' and '{end_ts}'
      and time_stamp::date = time_stamp_x::date;
    """
    db = pd.read_sql(qry, db)
    return db


# VARIATES
def best_layout_form_combo(db, start_ts, end_ts, err, rows):
    qry = f"""
        select
               layout_version, form,
               x             as approved,
               n             as loaded_clicks,
               intervals.p   as conversion_rate,
               se            as stand_err

        from (select rates.*,
                     sqrt(p * (1 - p) / n) as se
              from (select conversions.*,
                           x / n::float as p
                    from (select
                                 layout_version, form,
                                 count(1)                                      as n,
                                 sum(case when approved = 1 then 1 else 0 end) as x
                          from bro_clicks.click_funnel_2
                          where client_loaded = 1 and
                          time_stamp_x::date >= '{start_ts}' and time_stamp_x::date <= '{end_ts}'
                          group by layout_version, form) as conversions) as rates) as intervals
        where se <= {err} and se > 0
        order by conversion_rate desc
        limit {rows}
    """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def worst_layout_form_combo(db, start_ts, end_ts, err, rows):
    qry = f"""
        select
               layout_version, form,
               x             as approved,
               n             as loaded_clicks,
               intervals.p   as conversion_rate,
               se            as stand_err

        from (select rates.*,
                     sqrt(p * (1 - p) / n) as se
              from (select conversions.*,
                           x / n::float as p
                    from (select
                                 layout_version, form,
                                 count(1)                                      as n,
                                 sum(case when approved = 1 then 1 else 0 end) as x
                          from bro_clicks.click_funnel_2
                          where client_loaded = 1 and
                          time_stamp_x::date between '{start_ts}' and '{end_ts}'
                          group by layout_version, form
                          ) as conversions) as rates) as intervals
        where se <= {err} and se > 0
        order by conversion_rate asc
        limit {rows}
    """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def best_url(db, start_ts, end_ts, err, rows):
    qry = f"""
        select website_domain,
           x            as approved,
           n            as loaded_clicks,
           intervals.p  as conversion_rate,
           se           as stand_err
        from (select rates.*,
               sqrt(p * (1 - p) / n) as se
                from
                    (select
                    conversions.*,
                    x / n::float as p
                    from (
                        select
                            substring(url from '(?:.*://)?(?:www\.)?([^/?]*)') as website_domain,
                            count(1) as n,
                            sum(case when approved = 1 then 1 else 0 end) as x
                        from bro_clicks.click_funnel_2
                        where client_loaded = 1 and
                        time_stamp_x::date between '{start_ts}' and '{end_ts}'
                        group by website_domain) as conversions) as rates) as intervals
        where se <= {err} and se > 0 and website_domain not ilike '%%netlify%%'
        order by conversion_rate desc
    """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def url_provider_combo(db, start_ts, end_ts, err, rows):
    qry = f"""
            select provider, website_domain,
               x            as approved,
               n            as loaded_clicks,
               intervals.p  as conversion_rate,
               se           as stand_err
        from
        (select rates.*,
               sqrt(p * (1 - p) / n) as se
               from
                    (select conversions.*,
                           x / n::float as p
                        from (select
                                provider,
                                substring(url from '(?:.*://)?(?:www\.)?([^/?]*)') as website_domain,
                                count(1) as n,
                                sum(case when approved = 1 then 1 else 0 end) as x
                            from bro_clicks.click_funnel_2
                            where client_loaded = 1
                            and time_stamp_x::date between '{start_ts}' and '{end_ts}'
                            group by provider, website_domain) as conversions) as rates) as intervals
        where website_domain not ilike '%%netlify%%'
        and se <= {err} and se > 0
        order by conversion_rate desc
        limit {rows}
    """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def cta_button_checkout(db, start_ts, end_ts, err, rows):
    qry = f"""
        select 
            cta_button_checkout,
            x as approved,
            n as users,
            intervals.p as conversions_rate,
            se as stand_err
        from (select rates.*,
                    sqrt(p * (1 - p) / n) as se 
              from (select conversions.*,
                           x / n::float as p 
                    from (select cta_button_checkout,
                            count(1) as n,
                            sum(case when approved = 1 then 1 else 0 end) as x
                          from bro_clicks.click_funnel_2
                          where time_stamp_x::date between '{start_ts}' and '{end_ts}'
                          group by cta_button_checkout) as conversions) as rates) as intervals       
        where se <= {err} and se > 0
        order by conversions_rate desc
    """
    df = pd.read_sql(qry, db)
    return df.to_dict('records')


def times(db, start_ts, end_ts):
    qry = f"""
    select distinct a.click_id,
           start_ts,
           end_ts,
           end_ts - start_ts as time
    from (select clicks.click_id,
                 time_stamp as start_ts
          from bro_clicks.clicks
                   inner join
               (select click_id, approved, time_stamp_x
                from bro_clicks.click_funnel_2
                where time_stamp_x::date between '{start_ts}' and '{end_ts}') as funnel
               on funnel.click_id = clicks.click_id
          where time_stamp between '{start_ts}' and '{end_ts}'
            and event = 'page_visit'
            and approved = 1
            and (page = 'landing_page'
              or page ilike '%%/%%')) as a
        inner join
         (select clicks.click_id,
                 time_stamp as end_ts
          from bro_clicks.clicks
                   inner join
               (select click_id, approved, time_stamp_x
                from bro_clicks.click_funnel_2
                where time_stamp_x::date between '{start_ts}' and '{end_ts}') as funnel
               on funnel.click_id = clicks.click_id
          where time_stamp between '{start_ts}' and '{end_ts}'
            and event = 'click_submit'
            and approved = 1
            and page = 'checkout') as b
         on a.click_id = b.click_id
    where (end_ts - start_ts) > '00:00:00' and (end_ts - start_ts) < '12:00:00'
    order by time desc;    
    """
    df = pd.read_sql(qry, db)
    return df


def web_vitals(db, start_ts, end_ts):
    qry =  f"""
    select event, provider, affid, (event_data->>'value')::numeric as value
    from bro_clicks.clicks
    where event ilike 'web-vital%%' and time_stamp::date between  '{start_ts}' and '{end_ts}' and (event_data->>'value')::numeric is not null
    LIMIT 500;
    """
    df = pd.read_sql(qry, db)
    return df


def error_log(db, start_ts, end_ts):
    qry = f"""
    select a.click_id, error_category, error_type, error_message, page, provider, affid
    from 
        (select click_id, provider, affid, page
        from bro_clicks.clicks
        where time_stamp between '{start_ts}' and '{end_ts}') as b
    left outer join
         (select click_id, error_type, error_message, error_category
        from bro_clicks.error_log
        where server_time_stamp between '{start_ts}' and '{end_ts}') as a 
    on a.click_id = b.click_id;
    """
    df = pd.read_sql(qry, db)
    return df


