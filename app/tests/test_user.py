
from flask import Flask, json, jsonify, request, Response
import unittest

from app.models.users import User
from app.models.menu import MenuModel
from app.database.server import DBConnection
from app.models.orders import Order
from app.views.orderviews import OnlineRestuarant, app
from ..config import app_config


class UserTestCase(BaseTestCse):

    def test_spaces_in_username(self):
            """
            Test username has no spaces between characters
            """
            with self.client:
                result = self.signup(
                    "     ", "Ivan@gmail.com", "kansanga", "1246575", "user")
                self.assertEqual(result.status_code, 400)
