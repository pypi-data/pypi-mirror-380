from models.db import Db, pd
from hashlib import sha256
import json


class ReportingAlerts(Db):
    def __init__(self, db, account_id='54407332'):
        Db.__init__(self, db, 'reporting', 'custom_alerts')
        self.set_constraint('reporting_pkey', ['name'])

    def set_alert(self, name, structure, is_custom=True, alert_time='2025-01-01'):
        try:
            self.engine.execute(f"""
                INSERT INTO {self.schema}.{self.table}
                    (name, is_custom, structure, alert_time)
                    VALUES (%s::TEXT, %s::BOOL, %s::jsonb, %s::timestamp)
                ON CONFLICT (name)  DO UPDATE SET is_custom = excluded.is_custom, structure = excluded.structure

            """, [name, is_custom, json.dumps(structure), alert_time])
        except Exception as e:
            print(str(e))
            return False
        return True


