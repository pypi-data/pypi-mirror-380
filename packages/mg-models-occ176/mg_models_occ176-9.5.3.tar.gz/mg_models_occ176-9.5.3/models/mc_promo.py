from models.db import Db
import datetime as dt
from threading import Thread, Lock
import pandas as pd


class McPromoOptimizer(Db):
    _models = {}
    _last_update_time = {}
    _mod_locks = {}
    update_interval = 180

    def __init__(self, db, keys=['affid', 'provider', 'global', 'offer_id']):
        Db.__init__(self, db, 'mcpp_optimization', 'mc_promo_popup_agg')
        self._keys = keys
        self.refresh_models()

    @staticmethod
    def _join(*t):
        for th in t:
            try:
                th.join()
            except:
                pass
        return []

    @staticmethod
    def _mod_lock(key):
        if key not in McPromoOptimizer._mod_locks:
            McPromoOptimizer._mod_locks[key] = Lock()
        return McPromoOptimizer._mod_locks[key]

    def _check_update(self, key):
        return key not in self._last_update_time or dt.datetime.now() > (self._last_update_time[key] + dt.timedelta(seconds=self.update_interval))

    def _refresh_model(self, key, force_refresh=False):
        if force_refresh or self._check_update(key):
            if self._mod_lock(key).acquire(timeout=0.001):
                try:
                    McPromoOptimizer._models[key] = pd.read_sql(f"""
                        SELECT * from {self.schema}.{key}_{self.table}
                    """, self.engine)
                    McPromoOptimizer._last_update_time[key] = dt.datetime.now()
                except Exception as e:
                    print(str(e))
                finally:
                    self._mod_lock(key).release()

    def refresh_models(self):
        threads = []
        for k in self._keys:
            if self._check_update(k):
                t = Thread(target=self._refresh_model, args=(k, True))
                t.setDaemon(True)
                t.start()
                threads.append(t)
        self._join(*threads)

    @property
    def models(self):
        self.refresh_models()
        return self._models

    def __getitem__(self, item):
        return self.models[item]
