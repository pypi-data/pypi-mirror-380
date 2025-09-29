from models.db import Db, pd

class InitialRoutes(Db):
    def __init__(self, db, table):
        Db.__init__(self, db, "initial_route", table)
        self.iin_col = 'cc_first_6'

    def _key_check(self, key, **iin):
        if key in self.table:
            try:
                return iin[key] is not None
            except KeyError:
                return False
        return True

    def increment_conversion(self, approved, columns, **iin):
        try:
            _conflict = f""""""
            _whr = ""
            if not self._key_check('mcc', **iin):
                return

            if not self._key_check('cc_level', **iin):
                return

            if not self._key_check('cc_type', **iin):
                return

            if not self._key_check('bank', **iin):
                return

            if not self._key_check(self.iin_col, **iin):
                return

            for c in columns:
                if c in ['processor', 'cc_type', 'cc_first_6', 'mcc', 'cc_level']:
                    if c in list(self.columns()):
                        if _whr:
                            _whr += " and "
                        _whr += f"{c} = '{str(iin[c])}'"
            _set = f""" {"approved = approved+1" if approved else "declined = declined+1"}"""
            qry = f"""
                update {self.schema}.{self.table} 
                set {_set}
                where {_whr}
                returning approved                
            """
           # print(qry)
            val = self.engine.execute(qry).scalar()

            # if val is None:
            #     self.upsert(pd.DataFrame([{**{iin[c] for c in columns}, **{"approved" if approved else "declined": 1}}]))
        except Exception as e:
            print(str(e))

    @classmethod
    def bank_conversion(cls, db):
        cl = cls(db, 'bank_conversion')
        cl.set_constraint('bank_conversion_pk', ['bank', 'processor', 'mcc'])
        return cl

    @classmethod
    def cc_first_6_conversion(cls, db):
        cl = cls(db,'cc_first_6_conversion')
        cl.set_constraint('cc_first_6_conversion_pk', ['cc_first_6', 'processor', 'mcc'])
        return cl

    @classmethod
    def iin_conversion(cls, db):
        cl = cls(db, 'iin_conversion')
        cl.set_constraint('cc_first_6_conversion_pk', ['cc_first_6', 'processor', 'mcc'])
        return cl

    @classmethod
    def cc_type_cc_level_conversion(cls, db):
        cl = cls(db,'cc_type_cc_level_conversion')
        cl.set_constraint('cc_type_cc_level_comparison_pk', ['cc_type', 'cc_level', 'processor'])
        return cl

    @classmethod
    def cc_type_conversion(cls, db):
        cl = cls(db, 'cc_type_conversion')
        cl.set_constraint('cc_type_conversion_pk', ['cc_type', 'processor'])
        return cl

    @classmethod
    def cc_type_mcc_conversion(cls, db):
        cl = cls(db,'cc_type_mcc_conversion')
        cl.set_constraint('cc_type_mcc_conversion_pk', ['cc_type', 'processor', 'mcc'])
        return cl

    @classmethod
    def optimised_orders(cls, db):
        cl = cls(db, 'optimised_orders')
        cl.set_constraint('optimised_orders_pk', ['crm_id', 'order_id'])
        return cl



class ForeignInitialRoutes(Db):
    def __init__(self, db, table, version=1):
        Db.__init__(self, db, f"foreign_initial_route{f'_v{version}' if version >1 else ''}",  table)
        self.iin_name = 'cc_first_8' if version > 1 else 'cc_first_6'
        self.version = version

    def _key_check(self, key, **iin):
        if key in self.table:
            try:
                return iin[key] is not None
            except KeyError:
                return False
        return True

    def increment_conversion(self, approved, columns, **iin):
        try:
            _conflict = f""""""
            _whr = ""
            if not self._key_check('mcc', **iin):
                return

            if not self._key_check('cc_level', **iin):
                return

            if not self._key_check('cc_type', **iin):
                return

            if not self._key_check('bank', **iin):
                return

            if not self._key_check(self.iin_name, **iin):
                return

            for c in columns:
                if c in ['processor', 'cc_type', self.iin_name, 'mcc', 'cc_level', 'campaign_class']:
                    if c == 'campaign_class':
                        if c in ['prepaid', 'block']:
                            c = 'prepaid'
                        else:
                            c = 'paid'
                    if c in list(self.columns()):
                        if _whr:
                            _whr += " and "
                        _whr += f"{c} = '{str(iin[c])}'"
            _set = f""" {"approved = approved+1" if approved else "declined = declined+1"}"""
            qry = f"""
                update {self.schema}.{self.table} 
                set {_set}
                where {_whr}
                returning approved                
            """
           # print(qry)
            val = self.engine.execute(qry).scalar()

            # if val is None:
            #     self.upsert(pd.DataFrame([{**{iin[c] for c in columns}, **{"approved" if approved else "declined": 1}}]))
        except Exception as e:
            print(str(e))

    @classmethod
    def bank_conversion(cls, db):
        cl = cls(db, 'bank_conversion')
        cl.set_constraint('bank_conversion_pkey', ['bank', 'processor', 'mcc', 'campaign_class'])
        return cl

    @classmethod
    def cc_first_6_conversion(cls, db):
        cl = cls(db,'cc_first_6_conversion')
        cl.set_constraint('cc_first_6_conversion_pkey', ['cc_first_6', 'processor', 'mcc', 'campaign_class'])
        return cl

    @classmethod
    def iin_conversion(cls, db):
        cl = cls(db,'iin_conversion')
        cl.set_constraint('iin_conversion_pkey', ['cc_first_6', 'processor', 'mcc', 'campaign_class'])
        return cl


    @classmethod
    def cc_type_cc_level_conversion(cls, db):
        cl = cls(db,'cc_type_cc_level_conversion')
        cl.set_constraint('cc_type_cc_level_conversion_pkey', ['cc_type', 'cc_level', 'processor', 'campaign_class'])
        return cl

    @classmethod
    def cc_type_conversion(cls, db):
        cl = cls(db, 'cc_type_conversion')
        cl.set_constraint('cc_type_conversion_pkey', ['cc_type', 'processor', 'campaign_class'])
        return cl

    @classmethod
    def cc_type_mcc_conversion(cls, db):
        cl = cls(db,'cc_type_mcc_conversion')
        cl.set_constraint('cc_type_mcc_conversion_pkey', ['cc_type', 'processor', 'mcc', 'campaign_class'])
        return cl

    @classmethod
    def optimised_orders(cls, db):
        cl = InitialRoutes(db, 'optimised_orders')
        cl.set_constraint('optimised_orders_pkey', ['crm_id', 'order_id'])
        return cl


class ForeignInitialRoutesV2(ForeignInitialRoutes):
    def __init__(self, db, table):
        ForeignInitialRoutes.__init__(self, db, table, version=2)
        self.iin_name = 'cc_first_8'

    @classmethod
    def iin_conversion(cls, db):
        cl = cls(db, 'iin_conversion')
        cl.set_constraint('iin_conversion_pkey', ['cc_first_8', 'processor', 'mcc', 'campaign_class'])
        return cl
