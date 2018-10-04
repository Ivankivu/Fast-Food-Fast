import psycopg2
import unittest
import json
from app import app, app_config
from app.models.users import User
from app.database.server import DBConnection


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
            cursor.execute("CREATE TABLE IF NOT EXISTs users( user_id SERIAL PRIMARY KEY, record_timestamp timestamp default current_timestamp, user_name VARCHAR(100) NOT NULL, user_email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(12) NOT NULL)")
            cursor.execute("CREATE TABLE IF NOT EXISTs orders(order_id SERIAL PRIMARY KEY, created_timestamp timestamp default current_timestamp, order_type text not null, user_id int REFERENCES USERS (user_id), status_type text REFERENCES status (status_type), amount int not null")
            cursor.execute("CREATE TABLE IF NOT EXISTs menu(menu_id SERIAL PRIMARY KEY, record_timestamp timestamp default current_timestamp, status_type text references status (status_type), food_price int not null)")
            cursor.execute("CREATE TABLE IF NOT EXISTs status(status_id SERIAL PRIMARY KEY, record_timestamp timestamp default current_timestamp, status_type text not null)")

    def tearDown(self):
        """
        when test is done, drop table
        """
        with DBConnection() as cursor:
            cursor.execute("DROP TABLE IF EXISTS users CASCADE")
            cursor.execute("DROP TABLE IF EXISTS orders CASCADE")
            cursor.execute("DROP TABLE IF EXISTS menu CASCADE")
            cursor.execute("DROP TABLE IF EXISTS status CASCADE")
    
    def register_user(self, username, email, password):
        """
        Method for registering a user
        """
        return self.client.post(
            '/auth/signup',
            data=json.dumps(dict(
                username=username,
                email=email,
                password=password
            )
            ),
            content_type='application/json'
        )