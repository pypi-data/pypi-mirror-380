import pandas as pd
from models.reports.dependencies import ALERT_PROVIDERS, get_first_dom, now, today, _get_interval_date, get_cast, get_order_by, get_filters, format_group_by


def inactive_report(db, group_by=[], filters={}, reporting_query=False, order_by=False, inc_test_cc=False, **kwargs):
    f_whr = get_filters(filters, translate={'corp': 'corporation_name', 'is_cascade': 'is_dead_mid_cascade'},
                        prefix="WHERE")
    sdate, edate = reporting_query['start_date'], reporting_query['end_date']
    qry = f"""
        SELECT c.corporation_name,
       b.mid_number,
       a.destination_gateway::int::text                AS gateway_id,
       a.crm_id,
       b.close_date::text,
       d.enabled::TEXT as "is_enabled",
       c.daily_available                    AS daily_available_cap,
       c.monthly_available                  AS monthly_available_cap,
       c.daily_transaction_cap - c.used_dtc AS available_daily_transaction_cap,
       e.available_tc                       AS available_trailing30_cap,
       a.total_inactive::int::text,
       a.dead_mid_cascade::int::text,
       a.total_inactive_visa::int::text,
       a.total_inactive_master::int::text,
       a.total_inactive_discover::int::text

        FROM (SELECT a_1.crm_id,
             a_1.destination_gateway,
             count(1)                                                       AS total_inactive,
             count(1) FILTER (WHERE a_1.is_dead_mid_cascade = '1'::numeric)::int AS dead_mid_cascade,
             count(1) FILTER (WHERE a_1.cc_type = 'master'::text)           AS total_inactive_master,
             count(1) FILTER (WHERE a_1.cc_type = 'visa'::text)             AS total_inactive_visa,
             count(1) FILTER (WHERE a_1.cc_type = 'discover'::text)         AS total_inactive_discover
      FROM processing.recurring_orders a_1
      WHERE a_1.active IS FALSE
        AND a_1.retry_date IS NULL
      GROUP BY a_1.crm_id, a_1.destination_gateway) a
         JOIN (SELECT DISTINCT ON (steps.crm_id, steps.gateway_id) steps.crm_id,
                                                                   steps.gateway_id,
                                                                   steps.mid_number,
                                                                   steps.mid_id,
                                                                   steps.step,
                                                                   steps.close_date
               FROM ui_54407332_clients.steps) b ON b.crm_id = a.crm_id AND b.gateway_id = a.destination_gateway
         JOIN processing.cap c ON c.mid_id = b.mid_id::numeric AND c.step = b.step
         JOIN  (SELECT mid_id,step, available_tc from processing.trailing_cap) e on e.mid_id=b.mid_id and e.step=b.step
         JOIN ui_54407332_clients.gateway_settings d
              ON d.crm_id = a.crm_id AND d.gateway_id::numeric = a.destination_gateway
-- {f_whr}
        ORDER BY c.corporation_name, b.mid_number, a.destination_gateway, a.crm_id;
    """

    return pd.read_sql(qry, db.engine)

