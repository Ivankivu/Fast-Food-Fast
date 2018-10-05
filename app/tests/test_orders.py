
from flask import Flask, json, jsonify, request, Response
from app.tests.base import BaseTestCase
from app.models.users import User
from app.models.menu import MenuModel
from app.database.server import DBConnection
from app.models.orders import Order
from app.views.orderviews import OnlineRestuarant, app
from ..config import app_config
import http.client


class OnlineRestuarantTest(BaseTestCase):

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
    
    def test_setupOrder(self):
        order = self.client.get(
            '/users/orders',
            content_type='application/json',
            data=json.dumps({self, 'user_name', 'food_type', 'qty'}))

        self.assertTrue(404, orders.status_code)

    def test_get_order_list(self, order_id, user_name, qty):
        data = {
                'order_id': order_id,
                'user_name': user_name,
                'qty': qty
                }

        orders = self.client.get(
        
            '/users/orders',
            content_type='application/json',
            data=json.dumps(data)
        )
        self.assertEqual(orders.status_code), 404

    def test_add_order(self, user_name, qty, food_type):
        """
        Method for posting a question
        """
        data = {
                "food_type": food_type,
                "qty": qty,
                "user_name": user_name
            }

        order = self.client.post(
            '/users/orders',
            data=json.dumps(data),
            content_type='application/json'
        )
        assertEqual(order.status_code), 404

    def test_menu_post(self, food_type, food_price):
            """
            Define post attributes and route
            """
            data = {
                "food_typel": food_type,
                "food_price": food_price
            }
            return self.client.post(
                '/menu',
                content_type="application/json",
                data=json.dumps(data)
                )