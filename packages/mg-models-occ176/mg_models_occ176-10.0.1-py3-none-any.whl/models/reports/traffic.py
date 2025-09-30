import pandas as pd
from .dependencies import now, today, _get_interval_date, get_cast, get_order_by, get_filters, format_group_by


def traffic_by_offer(db, reporting_query,  filters={}, group_by=[], order_by=False,  **kwargs):
    f_whr = get_filters(filters,  'b.',  translate={'offer':  'name'}, prefix="WHERE")
    start_date, end_date = reporting_query['start_date'], reporting_query['end_date']
    #group_by = format_group_by(group_by)
    qry = f"""
        SELECT b.name AS "Offer",
       a."Clicks",
       a."Views",
       a."Bounce %%",
       a."Intent %%",
       a."CVR %%",
       a."Scrub %%"
       FROM (SELECT a_1.offer_id,
         count(DISTINCT a_1.click_id) FILTER (WHERE a_1.page = 'landing_page'::text)    AS "Clicks",
             count(DISTINCT a_1.click_id) FILTER (WHERE a_1.event = 'page_visit_api'::text) AS "Views",
             (count(DISTINCT a_1.click_id)::numeric -
              count(DISTINCT a_1.click_id) FILTER (WHERE a_1.event = 'page_visit_api'::text)::numeric) /
             NULLIF(count(DISTINCT a_1.click_id), '0'::bigint)::numeric                     AS "Bounce %%",
             count(DISTINCT a_1.click_id)
             FILTER (WHERE a_1.page = 'checkout'::text AND a_1.event = 'click_submit'::text)::numeric /
             NULLIF(count(DISTINCT a_1.click_id), '0'::bigint)::numeric                     AS "Intent %%",
             count(DISTINCT a_1.click_id)
             FILTER (WHERE a_1.page = 'checkout'::text AND b_1.click_id IS NOT NULL)::numeric /
             NULLIF(count(DISTINCT a_1.click_id), '0'::bigint)::numeric                     AS "CVR %%",
             count(DISTINCT a_1.click_id)
             FILTER (WHERE a_1.page = 'checkout'::text AND b_1.click_id IS NOT NULL AND b_1.is_network IS TRUE AND
                           b_1.saved = '1'::numeric)::numeric / NULLIF(count(DISTINCT a_1.click_id)
                                                                       FILTER (WHERE a_1.page = 'checkout'::text AND b_1.click_id IS NOT NULL)::numeric,
                                                                       '0'::numeric)        AS "Scrub %%"
        FROM bro_clicks.clicks a_1
               LEFT JOIN (SELECT DISTINCT ON (conversions.provider, conversions.click_id) conversions.provider,
                                                                                          conversions.click_id,
                                                                                          conversions.is_network,
                                                                                          conversions.saved,
                                                                                          CASE
                                                                                              WHEN conversions.is_network IS TRUE AND conversions.saved = '0'::numeric
                                                                                                  THEN conversions.cpa
                                                                                              ELSE '0'::numeric
                                                                                              END AS cpa
                          FROM bro_clicks.conversions
                          WHERE conversions.time_stamp >= '{start_date}'::date::timestamp without time zone
                            AND conversions.time_stamp <= '{end_date}'::date::timestamp without time zone
                            AND conversions.step = '1'::numeric
                            AND conversions.decline_reason IS NULL) b_1
                         ON b_1.provider = a_1.provider AND b_1.click_id = a_1.click_id
        WHERE a_1.time_stamp >= '{start_date}'::date::timestamp without time zone
            AND a_1.time_stamp <= '{end_date}'::date::timestamp without time zone
            AND (a_1.event = ANY (ARRAY ['page_visit'::text, 'page_visit_api'::text, 'click_submit'::text]))
            AND (a_1.page = ANY (ARRAY ['landing_page'::text, 'checkout'::text]))
            AND lower(a_1.provider) <> 'test'::text
             
        GROUP BY a_1.offer_id
        ORDER BY (count(DISTINCT a_1.click_id)) DESC) a
         JOIN ui_54407332_offers.offers b ON b.offer_id::numeric = a.offer_id
         {f_whr}
         
    """
    return pd.read_sql(qry, db.engine)


def traffic_by_provider(db, reporting_query, group_by=[], filters={},order_by=False,**kwargs):
    f_whr = get_filters(filters,  'a.')
    start_date, end_date = reporting_query['start_date'], reporting_query['end_date']
    #group_by = format_group_by(group_by)
    qry = f"""
        SELECT lower(a.provider)                                                          AS "Provider",
       count(DISTINCT a.click_id)                                                 AS "Clicks",
       count(DISTINCT a.click_id) FILTER (WHERE a.event = 'page_visit_api'::text) AS "Views",
       (count(DISTINCT a.click_id)::numeric -
        count(DISTINCT a.click_id) FILTER (WHERE a.event = 'page_visit_api'::text)::numeric) /
       NULLIF(count(DISTINCT a.click_id), '0'::bigint)::numeric                   AS "Bounce %%",
       count(DISTINCT a.click_id) FILTER (WHERE a.page = 'checkout'::text AND a.event = 'click_submit'::text)::numeric /
       NULLIF(count(DISTINCT a.click_id), '0'::bigint)::numeric                   AS "Intent %%",
       count(DISTINCT a.click_id) FILTER (WHERE a.page = 'checkout'::text AND b.click_id IS NOT NULL)::numeric /
       NULLIF(count(DISTINCT a.click_id), '0'::bigint)::numeric                   AS "CVR %%",
       count(DISTINCT a.click_id)
       FILTER (WHERE a.page = 'checkout'::text AND b.click_id IS NOT NULL AND b.is_network IS TRUE AND
                     b.saved = '1'::numeric)::numeric /
       NULLIF(count(DISTINCT a.click_id) FILTER (WHERE a.page = 'checkout'::text AND b.click_id IS NOT NULL)::numeric,
              '0'::numeric)                                                       AS "Scrub %%"
       FROM bro_clicks.clicks a
         LEFT JOIN (SELECT DISTINCT ON (conversions.provider, conversions.click_id) conversions.provider,
                                                                                    conversions.click_id,
                                                                                    conversions.is_network,
                                                                                    conversions.saved,
                                                                                    CASE
                                                                                        WHEN conversions.is_network IS TRUE AND conversions.saved = '0'::numeric
                                                                                            THEN conversions.cpa
                                                                                        ELSE '0'::numeric
                                                                                        END AS cpa
                    FROM bro_clicks.conversions
                    WHERE conversions.time_stamp >= '{start_date}'::date::timestamp without time zone
                      AND conversions.time_stamp <= '{end_date}'::date::timestamp without time zone
                      AND conversions.step = '1'::numeric
                      AND conversions.decline_reason IS NULL) b ON b.provider = a.provider AND b.click_id = a.click_id
        WHERE a.time_stamp >= '{start_date}'::date::timestamp without time zone
          AND a.time_stamp <= '{end_date}'::date::timestamp without time zone
          AND (a.event = ANY (ARRAY ['page_visit'::text, 'page_visit_api'::text, 'click_submit'::text]))
          AND (a.page = ANY (ARRAY ['landing_page'::text, 'checkout'::text]))
          AND lower(a.provider) <> 'test'::text
          {f_whr}
        GROUP BY (lower(a.provider))
        ORDER BY (count(DISTINCT a.click_id)) DESC;
        
    """

    return pd.read_sql(qry, db.engine)