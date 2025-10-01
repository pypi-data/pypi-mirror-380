import pandas as pd
from .dependencies import now, today, _get_interval_date, get_cast, get_order_by, get_filters, format_group_by


def revenue(db, start_date, end_date, offset=0, crm_id='all'):
    qry = f"""
            SELECT COALESCE(sum(ui_revenue_transactions.value), '0'::numeric) AS "revenue"
            FROM reporting.ui_revenue_transactions
            WHERE ui_revenue_transactions.date >= {_get_interval_date(start_date, offset)}::date
              AND ui_revenue_transactions.date <= {_get_interval_date(end_date, offset)}::date
              AND ui_revenue_transactions.crm_id = '{crm_id}'::text
              AND ui_revenue_transactions.type = 'revenue'::text;

            """

    res = db.engine.execute(
        qry
    ).scalar()
    return float(res) if res else 0


def approval_by_cycle(db, billing_cycle, start_date, end_date, offset=0, crm_id='all'):
    qry = f"""  SELECT COALESCE(count(
                                    CASE
                                        WHEN cpa_orders.decline_reason IS NULL THEN 1
                                        ELSE NULL::integer
                                        END)::numeric / NULLIF(count(1), '0'::bigint)::numeric,
                            '0'::numeric) AS c_1_natural_approval
            FROM reporting.cpa_orders
            WHERE cpa_orders.acquisition_date >= {_get_interval_date(start_date, offset)}::timestamp without time zone
              AND cpa_orders.acquisition_date <= {_get_interval_date(end_date, offset)}::timestamp without time zone
              AND cpa_orders.crm_id = '{crm_id}'::text
              AND cpa_orders.bc_inferred = '1'::numeric
              AND cpa_orders.attempt_count = 0
              AND cpa_orders.pp_customer = '0'::numeric
              AND cpa_orders.block_customer = '0'::numeric;

        """ if billing_cycle > 0 else f"""
            SELECT count(1) FILTER (WHERE a.count_decline_approved > '0'::bigint)::numeric /
            NULLIF(count(1), '0'::bigint)::numeric AS "C0 Approval"
            FROM (SELECT a_1.email_address,
                         count(DISTINCT a_1.customer_id) FILTER (WHERE a_1.decline_reason IS NULL) AS count_decline_approved
                  FROM crm_global.orders a_1
                           JOIN (SELECT DISTINCT offer_globals.crm_id,
                                                 ARRAY [offer_globals.saves_campaign, offer_globals.provider_campaign] AS include_campigns
                                 FROM ui_54407332_offers.offer_globals
                                 WHERE offer_globals.crm_id = '{crm_id}'::text
                                   AND offer_globals.step = 1) b
                                ON b.crm_id = a_1.crm_id AND (a_1.campaign_id = ANY (b.include_campigns))
                  WHERE a_1.crm_id = '{crm_id}'::text
                    AND a_1.month_date >=  {_get_interval_date(start_date, offset)}::date
                    AND a_1.month_date <=  {_get_interval_date(end_date, offset)}::date
                  GROUP BY a_1.email_address) a;
        """

    res = db.engine.execute(
        qry
    ).scalar()
    return float(res * 100) if res else 0


def steps(db, start_date, end_date, offset=0, crm_id='all'):
    qry = f"""SELECT count(1) AS initials
                FROM reporting.cpa_orders
                WHERE cpa_orders.acquisition_date >= {_get_interval_date(start_date, offset)}::timestamp without time zone
                  AND cpa_orders.acquisition_date <= {_get_interval_date(end_date, offset)}::timestamp without time zone
                  AND cpa_orders.crm_id = '{crm_id}'::text
                  AND cpa_orders.bc_inferred = '0'::numeric
                  AND cpa_orders.step = '1'::numeric
                  AND cpa_orders.refund_amount = '0'::real
                  AND cpa_orders.decline_reason IS NULL
                  AND cpa_orders.pp_customer = '0'::numeric
                  AND cpa_orders.block_customer = '0'::numeric;

        """
    # print(qry)
    res = db.engine.execute(
        qry
    ).scalar()
    return float(res) if res else 0


