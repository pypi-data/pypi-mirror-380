import datetime as dt


class TablePartitioner:

    def __init__(self, crm_id, schema, table, date_col_name, *partitions, **kw):
        self.crm_id = crm_id
        self.table = table
        self.schema = schema
        self.dc_name = date_col_name
        if not len(partitions):
            self.partitions = ['crm', 'year', 'month']
        else:
            self.partitions = partitions

        self.query = ""

    @staticmethod
    def crm_partition(crm_id: str, schema: str, table: str, date_col_name: str, **kw):
        return f"""
            create table if not exists {schema}.{table}_{crm_id}
            partition of {schema}.{table}
            FOR VALUES IN ('{crm_id}')
            partition by RANGE ({date_col_name});
        """

    @staticmethod
    def year_partition(crm_id: str, schema: str, table: str, date_col_name: str, year: int, **kw):
        start = dt.datetime(year=int(year), month=1, day=1).date()
        end = start.replace(year=int(year)+1)
        return f"""
            create table if not exists {schema}.{table}_{crm_id}_{year}
            partition of {schema}.{table}_{crm_id}
            FOR VALUES FROM ('{start}') TO ('{end}')
            partition by RANGE ({date_col_name});
        """

    @staticmethod
    def month_partition(crm_id: str, schema: str, table: str, date_col_name: str, year: int, month: int, **kw):
        month = int(month)
        year = int(year)
        start = dt.datetime(year=year, month=month, day=1).date()

        if month == 12:
            end = start.replace(year=year+1, month=1)
        else:
            end = start.replace(month=month+1)

        return f"""
            create table if not exists {schema}.{table}_{crm_id}_{year}_{month}
            partition of {schema}.{table}_{crm_id}_{year}
            FOR VALUES FROM ('{start}') TO ('{end}');
          --  partition by RANGE ({date_col_name});
        """

    def append_query(self, text):
        self.query += text
        return self

    def gen_query(self, year: [int] = None):
        if not year:
            year = [int(dt.datetime.now().date().year)]
        if 'crm' in self.partitions:
            self.append_query(self.crm_partition(self.crm_id, self.schema, self.table, self.dc_name))
        if 'year' in self.partitions:
            if not isinstance(year, (list, tuple)):
                year = [year]
            for y in year:
                self.append_query(
                    self.year_partition(self.crm_id, self.schema, self.table, self.dc_name, y))
                if 'month' in self.partitions:
                    for i in range(1, 13):
                        self.append_query(
                            self.month_partition(self.crm_id, self.schema, self.table, self.dc_name, y, i))
        return self

    def execute(self, db, query=None):
        conn = db.engine.raw_connection()
        cur = conn.cursor()
        try:
            cur.execute(query if query else self.query)
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            conn.rollback()
            try:
                cur.close()
            except:
                pass
            try:
                conn.close()
            except:
                pass
            raise e

    @classmethod
    def new_crm(cls, crm_id, schema, table, date_col_name, *partitions, year: [int] = None, **kw):
        if crm_id not in partitions and len(partitions):
            partitions = ['crm_id'] + list(partitions)
        return cls(crm_id, schema, table, date_col_name, *partitions).gen_query(year)

    @classmethod
    def new_year(cls, crm_id, schema, table, date_col_name, year: [int], *partitions):
        if not len(partitions):
            partitions = ['year', 'month']
        return cls(crm_id, schema, table, date_col_name, *partitions).gen_query(year)





