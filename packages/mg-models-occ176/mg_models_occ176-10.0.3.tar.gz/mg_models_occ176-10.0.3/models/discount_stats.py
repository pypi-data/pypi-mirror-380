import pandas as pd


def ds_discount_model(db, rebill_price, crm_id):
    df = pd.read_sql(f"""
          select b.customer_id,
         c.step,
         b.order_id,
         b.time_stamp,
         b.order_total,
         c.attempt_count,
         c.decline_reason,
         {rebill_price}::numeric rebill_price
         -- from processing.test_customers a
                   from crm_global.orders b --on b.crm_id = '{crm_id}' and a.customer_id = b.customer_id --and a.test_type = 'discount_nsf_no_cascade'
                   inner join augmented_data.order_cycles c
                              on c.order_id = b.order_id and c.crm_id = b.crm_id and c.attempt_count > 0 and c.crm_id  ='{crm_id}'  and c.crm_id='{crm_id}'
          where order_total::numeric < ({rebill_price-3})::numeric
          order by customer_id, step, time_stamp;    

      """, db.engine)
    df['discount_pct'] = 1 - pd.np.round(df.order_total / df.rebill_price, 2)
    df[['pct_bin', 'prc_bin']] = 0
    for i in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        df.loc[(df.pct_bin == 0) & (df.discount_pct <= i / 100), 'pct_bin'] = i / 100
        df.loc[(df.prc_bin == 0) & (df.order_total <= i), 'prc_bin'] = i
    df = df.set_index(['customer_id', 'step', 'order_id'], drop=False).sort_index(0)
    df['discount_attempt'] = df.groupby(level=[0, 1]).cumcount()
    df[['approved', 'declined']] = pd.Series([0, 0]).values
    df['revenue'] = df.order_total
    df.loc[df.decline_reason.isna(), 'approved'] = 1
    df.loc[~df.decline_reason.isna(), ['declined', 'revenue']] = pd.Series([1, float(0)]).values
    return df
