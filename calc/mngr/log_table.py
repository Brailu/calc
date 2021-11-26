"""
log_table.py

Log table gateway.
"""


from datetime import datetime
from mngr.table import Table


class LogTable(Table):

    def select(self):
        try:
            cursor = self.get_cursor()
            sql = "select * from log"
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            raise RuntimeError("Coult not select from table")
    
    def insert(self, operation_id, message):
        try:
            cursor = self.get_cursor()
            sql = "insert into log values (?, ?, ?, ?)"
            now = datetime.isoformat(datetime.now())
            cursor.execute(sql, (None, now, operation_id, message))
            self.commit()
            return True
        except:
            self.close_connection()
            raise RuntimeError("Could not insert into table")
