import psycopg2
import os
from pprint import pprint
from ..config import app_config


class DBConnection():

    def __enter__(self):
        try:
            self.conn = psycopg2.connect("dbname = 'fastfood' user = 'postgres' host = 'localhost' password = 'andela' port = '5432'")
            self.cursor = self.conn.cursor()
            return self.cursor
        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)

    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
