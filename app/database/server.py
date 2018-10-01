import psycopg2
import os
from config import app_config
from pprint import pprint


class DBConnection(object):

    def __enter_(self):

        try:

            self.conn = psycopg2.connect(
                database='fastfood',
                user='postgres',
                password='andela',
                host='localhost',
                port='5432')
            print('Opened database successfully')
            self.cursor = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)

    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


