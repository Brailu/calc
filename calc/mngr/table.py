"""
table.py

A table gateway.
"""


import sqlite3


class Table():
    
    connection = None
    cursor = None
    table_name = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
        
        return self.connection

    def get_cursor(self):
        return self.get_connection().cursor()

    def commit(self):
        if self.connection:
            self.connection.commit()

    def rollback(self):
        if self.connection:
            self.connection.rollback()

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def select(self, row):
        pass

    def insert(self, id):
        pass

    def update(self, id, row):
        pass

    def delete(self, id):
        pass
