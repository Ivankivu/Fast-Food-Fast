
from app.DB.server import DBConnection
import psycopg2
import unittest
import json
from app import app, app_config
from app.models.users import User


class BaseTestCase(unittest.TestCase):

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)
        with DBConnection() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS users(ser_id serial PRIMARY KEY,record_timestamp timestamp default current_timestamp,user_name text not null,user_email text not null,user_password  varchar(50) not null)")
            cursor.execute("CREATE TABLE IF NOT EXISTs menu(reply_id SERIAL PRIMARY KEY, qtn_id INT NOT NULL, user_id INT NOT NULL, reply_desc VARCHAR(100) NOT NULL, preffered BOOLEAN NOT NULL DEFAULT FALSE)")
            cursor.execute("CREATE TABLE IF NOT EXISTs orders(CREATE TABLE IF NOT EXISTS orders(order_id serial PRIMARY KEY,created_timestamp timestamp default current_timestamp,order_type text not null,user_id int REFERENCES USERS (user_id),status_type  text not null REFERENCES status (status_type),amount int not null)")
            cursor.execute("CREATE TABLE IF NOT EXISTS status(status_id serial PRIMARY KEY,record_timestamp timestamp default current_timestamp,status_type text not null)")
    
    def tearDown(self):
        """
        Method to droP tables after the test is run
        """
        with DBConnection() as cursor:
            cursor.execute("DROP TABLE IF EXISTS users CASCADE")
            cursor.execute("DROP TABLE IF EXISTS orders CASCADE")
            cursor.execute("DROP TABLE IF EXISTS menu CASCADE")
            cursor.execute("DROP TABLE IF EXISTS status CASCADE")