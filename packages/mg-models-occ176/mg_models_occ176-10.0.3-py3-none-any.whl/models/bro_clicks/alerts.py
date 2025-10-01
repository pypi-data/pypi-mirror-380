from models.db import Db, pd, np
import datetime as dt
from models import config


class InitialsCCType(Db):
    alert_thresholds = None

    def __init__(self, db):
        Db.__init__(self, db, 'alerts', 'initials_cc_type')
        self.set_constraint('initials_cc_type_pk', ['cc', 'crm_id'])
        self.model = None

    @staticmethod
    def now():
        return dt.datetime.now() - dt.timedelta(hours=config.timeOffset)

    @staticmethod
    def today():
        return InitialsCCType.now().date()

    def get_model(self, test_val=False):
        self.model = pd.read_sql(
            f"""
            select cur.*, prev.remaining_mtd_cap as prev_remaining_mtd, prev.alert_level  from (
            SELECT  crm_id,
                    'master' as cc,
                   sum(monthly_initial_cap)                                          AS total_mtd_cap,
                   sum(initial_count_mtd)                                            AS mtd_initials,
                   sum(monthly_initial_cap) - sum(load_balancer_2.initial_count_mtd) AS remaining_mtd_cap
            FROM bro_clicks.load_balancer_2
            WHERE load_balancer_2.date >= '{self.today()}'
             AND exclude_cc_types not ilike '%%master%%'
              AND step = '1'::numeric       
              AND gateway_id <> '1'::numeric
               AND router_id = '1'::numeric
            GROUP BY crm_id
            UNION ALL 

            SELECT  crm_id,
                    'visa' as cc,
                   sum(visa_monthly_cap)                                          AS total_mtd_cap,
                   sum(visa_count_mtd)                                            AS mtd_initials,
                   sum(visa_monthly_cap) - sum(load_balancer_2.visa_count_mtd) AS remaining_mtd_cap
            FROM bro_clicks.load_balancer_2
            WHERE load_balancer_2.date >= '{self.today()}'
             -- AND load_balancer_2.crm_id = 'crm_ll_2'::text
             AND exclude_cc_types not ilike '%%visa%%'
              AND step = '1'::numeric       
              AND gateway_id <> '1'::numeric
               AND router_id = '1'::numeric
            GROUP BY crm_id) cur
            left join alerts.initials_cc_type as prev on cur.cc = prev.cc;

            """,
            self.engine
        ).fillna(0)

        self.get_alert_levels()
        if test_val:
            self.model.remaining_mtd_cap = test_val
        return self.model

    def set(self):
        if not hasattr(self, 'model') or self.model is None:
            self.get_model()
        self.set_alert_levels()
        self.upsert(self.model)

    def get_alert_levels(self):
        if self.alert_thresholds is None:
            self.alert_thresholds = [int(v[0]) for v in self.engine.execute(
                f"""select * from {self.schema}.initials_cc_type_thresholds order by threshold::int desc """)]
            return self.alert_thresholds

    def _next_alert_level(self, value):
        return self._find_trigger_level(value, 0)

    def _find_trigger_level(self, value, idx_offset=0):

        for i in range(len(self.alert_thresholds)):
            if i == len(self.alert_thresholds) - 1 and value <= self.alert_thresholds[i]:
                return self.alert_thresholds[len(self.alert_thresholds) - 1]
            elif value < self.alert_thresholds[i] and value > self.alert_thresholds[i + 1]:
                try:
                    v = self.alert_thresholds[i + 1 + idx_offset]
                    return v
                except:
                    pass
        return self.alert_thresholds[0]

    def set_alert_levels(self):
        self.get_alert_levels()
        if 'trigger_level' not in self.model.columns:
            self.get_alert_triggers()
        self.model.alert_level = self.model.remaining_mtd_cap.apply(lambda x: self._next_alert_level(x))

    def get_alert_triggers(self):
        self.model['trigger_level'] = self.model.remaining_mtd_cap.apply(
            lambda x: self._find_trigger_level(x)
        )
        return self.model.loc[(self.model.trigger_level < self.model.alert_level) | (self.model.remaining_mtd_cap < 10)]


