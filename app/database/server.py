import psycopg2
import os
from pprint import pprint
from app.config import app_config


class DBConnection():

    def __enter__(self):
        try:
            self.conn = psycopg2.connect("dbname='d3oceli53i6eg7' user='hscqqcrrhcgcpn' host='ec2-54-235-90-0.compute-1.amazonaws.com' password='30b46f80b9e83ac37a9fca1545fdda836058d1e73f52a7723fb51d77af4dc3a1' port='5432'")
            self.cursor = self.conn.cursor()
            return self.cursor
        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)

    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
