import psycopg2
import os
from pprint import pprint
from app.config import app_config
# from .tables import MyTables


class DBConnection():

    def __enter__(self):
        try:
            if app_config['production']:
                self.conn = psycopg2.connect(str(os.getenv("DATABASE_URL")))
                self.cursor = self.conn.cursor()
                return self.cursor
                print("Database connection successful")
            else:
                self.conn = psycopg2.connect(str(os.getenv("DATABASE_URL1")))
                self.cursor = self.conn.cursor()
                return self.cursor
                print("Database created successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)

            tables = MyTables()
            self.cursor.execute(tables)

    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()