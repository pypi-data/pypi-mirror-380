
def run(db, crm_id, max_timestamp, **kw):
    conn = db.engine.raw_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"""
            create temp table zero_orders on commit drop as select crm_id, order_id, month_date from crm_global.orders where order_total::numeric > 0 and crm_id='{crm_id}' and gateway_id=1;
            update crm_global.orders up set order_total='0.00 'from zero_orders dn where dn.crm_id = up.crm_id and dn.order_id = up.order_id and up.month_date = dn.month_date;
            drop table zero_orders;

            drop table if exists rdr_{crm_id};
            drop table if exists rdr_cb360_{crm_id};
            create temp table rdr_{crm_id} as (select distinct on (crm_id, order_id) crm_id,
                                                                    order_id,
                                                                    rep_last_modified,
                                                                    parse_arr[1]                refund_date,
                                                                    trim(parse_arr[3])::numeric amount_refunded_to_date
                              from (select crm_id,
                                           native_order_id::int       as                             order_id,
                                           regexp_split_to_array(trim(split_part(note, 'refunded on', 2)),
                                                                 ' ') as                             parse_arr,
                                           (now() - Interval '4 hours')::timestamp without time zone rep_last_modified
                                    from crm_global.employee_notes
                                    where note ilike '%%rdr%%refunded on%%'
                                      and crm_id = '{crm_id}'
                                      and date_time >= '{max_timestamp}'::timestamp
                                      ) a
                              where trim(parse_arr[3])::numeric is not null);


            alter table rdr_{crm_id}
                add primary key (crm_id, order_id);


            update crm_global.orders up
            set amount_refunded_to_date=rdr.amount_refunded_to_date,
                rep_last_modified=rdr.rep_last_modified,
                refund_date=rdr.refund_date::date,
                is_recurring=0
            from rdr_{crm_id} as rdr
            where rdr.crm_id = up.crm_id
              and rdr.order_id = up.order_id;

            create temp table rdr_cb360_{crm_id} as select b.crm_id, b.order_id, b.order_total amount_refunded_to_date, a.date_time::date refund_date
            from (
                    select distinct on (crm_id, native_order_id::int) crm_id, native_order_id, date_time from crm_global.employee_notes
                    where crm_id = '{crm_id}' and note ilike '%CB360%' and note ilike '%rdr%'
            ) a
            inner join (
            select crm_id, order_id, order_total
            from crm_global.orders where crm_id='{crm_id}') b on b.order_id = a.native_order_id::int and b.crm_id = a.crm_id;

              update crm_global.orders up
            set amount_refunded_to_date=rdr.amount_refunded_to_date,
                rep_last_modified=(now() - Interval '4 hours')::timestamp without time zone,
                refund_date=rdr.refund_date::date
            from rdr_cb360_{crm_id} as rdr
            where rdr.crm_id = up.crm_id
              and rdr.order_id = up.order_id;

        --- PARSE AND UPDATE CHARGEBACKS CB360

            drop table if exists cbs_cb360_{crm_id};
            create temp table cbs_cb360_{crm_id} as
            select b.crm_id,
                   b.customer_id,
                   b.order_id,
                   a.date_time::date as refund_date,
                   0 as is_recurring,
                    (now() - Interval '4 hours')::timestamp without time zone rep_last_modified,
                   nullif(split_part(split_part(a.note, 'in the amount of $', 2), ' ',1), '')::numeric as amount_refunded_to_date
            from (select distinct on (crm_id, native_order_id) crm_id, native_order_id::int as order_id, note, date_time
                  from crm_global.employee_notes
                  where note ilike '%CHARGEBACK360%' and crm_id='{crm_id}') a
                     inner join crm_global.orders b on b.crm_id = a.crm_id and b.order_id = a.order_id
                  where b.amount_refunded_to_date <> nullif(split_part(split_part(a.note, 'in the amount of $', 2), ' ',1), ' ')::numeric;


                 update crm_global.orders up
                set amount_refunded_to_date=cbs.amount_refunded_to_date,
                    is_recurring = cbs.is_recurring,
                    rep_last_modified=(now() - Interval '4 hours')::timestamp without time zone,
                    refund_date=cbs.refund_date::date
                from cbs_cb360_{crm_id} as cbs
                where cbs.crm_id = up.crm_id
                  and cbs.order_id = up.order_id;
        
        """)

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        cur.close()
        conn.close()
        raise e