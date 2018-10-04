import psycopg2
import os
from pprint import pprint
from app.config import app_config
from .tables import MyTables


class DBConnection():

    def __enter__(self):
        try:
            # if app_config['testing']:
            #     self.conn = psycopg2.connect("dbname = 'test_db', user = 'postgres' host = 'localhost' password = 'andela' port = '5432'")
            #     self.cursor = self.conn.cursor()
            #     return self.cursor
            # else:
            self.conn = psycopg2.connect("dbname = 'fastfood' user = 'postgres' host = 'localhost' password = 'andela' port = '5432'")
            
            self.cursor = self.conn.cursor()

            # tables = MyTables().create_tables()
            # return tables

            return self.cursor
        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)
            cursor.execute(command % self.table_name)
            self.conn.commit()
            print("Table_orders created successfully")
        
    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
