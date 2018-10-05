
from flask import Flask, json, jsonify, request, Response
import unittest
from unittest import TestCase
from app.models.users import User
from app.models.menu import MenuModel

from app.models.orders import Order
from app.views.orderviews import OnlineRestuarant, app
from ..config import app_config


class OnlineRestuarantTest(unittest.TestCase):

    def SetUp(self):
        app.config.from_object(app_config["testing"])
        return app
        self.client = app.test_client(self)
        self.food_type = Order().food_type
        self.user_name = Order().user_name
        self.qty = Order().qty

    def setUp(self):
        app.config.from_object(app_config["testing"])
        return app

    def test_get_order_list(self):

        orders = self.client.get(
            '/users/orders',
            content_type='application/json',
            data=json.dumps({'order': self.orders})
        )
        self.assertEqual(404, orders.status_code)
