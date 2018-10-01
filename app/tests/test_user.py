import unittest
from config import app_config


class UserTestCase(unittest.TestCase):

    def setUp(self):
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)
