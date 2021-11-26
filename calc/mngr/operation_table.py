"""
operation_table.py

Operation table gateway.
"""


from mngr.table import Table
from mngr.log_table import LogTable


class OperationTable(Table):

    log_table = LogTable()

    def log(self, operation_id, message):
        try:
            self.log_table.insert(operation_id, message)
        except:
            raise RuntimeError("Could not log")

    def select(self, name=None):
        try:
            cursor = self.get_cursor()
            if name is None:
                sql = "select * from operation"
                cursor.execute(sql)
            else:
                sql = "select * from operation where name = ?"
                cursor.execute(sql, (name))
            return cursor.fetchall()
        except:
            raise RuntimeError("Could not select from table")

    def insert(self, name, func):
        try:
            cursor = self.get_cursor()
            sql = "insert into operation values (?, ?, ?)"
            cursor.execute(sql, (None, name, func))
            self.commit()
            self.log(cursor.lastrowid, "Operation inserted")
            return True
        except:
            self.close_connection()
            raise RuntimeError("Could not insert into table")

    def update(self, id, name, func):
        try:
            cursor = self.get_cursor()
            sql = "update operation set name = ?, func = ? where id = ?"
            cursor.execute(sql, (name, func, id))
            self.commit()
            self.log(id, "Operation updated")
            return True
        except:
            self.close_connection()
            raise RuntimeError("Could not insert into table")

    def delete(self, id):
        try:
            cursor = self.get_cursor()
            sql = "delete from operation where id = ?"
            cursor.execute(sql, (id))
            self.commit()
            self.log(id, "Operation deleted")
            return True
        except:
            self.close_connection()
            raise RuntimeError("Could not delete from table")
