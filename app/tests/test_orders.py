
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

    def test_get_all_orders(self):
        order_list = []
        orders = self.client.get(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps({'order': self.order})
        )
        return orders
        self.assertEqual(404, orders.status_code)

    def test_get_order(self):
        order = self.client.get(
            '/users/orders/<int:order_id>',
            content_type='application/json',
            data=json.dumps(self.order)
        )
        return order
        self.assertEqual(404, order.status_code)

    def test_home(self):
        content = self.client.get(
            '/',
            content_type='application/json',
            data=json.dumps(self.order_list)
        )
        self.assertEqual(200, content.status_code)

    def test_orderid(self):
        self.assertEqual(self.amount, 3000,
                         msg='ID is Invalid')

    def test_default_status(self):
        self.assertEqual(self.status, 'pending',
                         msg='not default status.')

    def test_Food_value(self):
        self.Order.Food = "fish"
        self.assertEqual(self.Food, "fish",
                         msg='not food item')

    def test_amount_value(self):
        self.Order.amount
        self.assertEqual(self.amount, 3000,
                         msg='false amount.')

    def test_item_posted(self):
        self.order_list = []
        orders = self.client.post(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps(self.order)
        )
        self.assertEqual(orders.status_code, 201)
        self.assertIn("pending", str(orders.data))

    def test_food_empty_string(self):
        self.order = {
            "Food": "",
            "amount": 1500
        }
        order1 = self.client.post(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps(self.order)
        )
        self.assertEqual(order1.status_code, 404)
        self.assertIn("food should not be empty", str(order1.data))

    def test_ii_post_order(self):

        order_list = []
        order1 = self.client.post(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps(self.order)
        )
        self.order = {
            "Food": "Rice",
            "amount": 1500,
            "status": "pending",
            "order_id": 9
        }

        order_list.append(self.order)
        self.assertEqual(201, order1.status_code)

        self.assertIn('"order_id":1', str(order1.data))

    def test_edit_order(self):

        order_list = []
        order = self.client.post(
            '/api/v1/orders/<int:order_id>',
            content_type='application/json',
            data=json.dumps(self.order)
        )
        order1 = {
            "Food": "Rice",
            "amount": 1500,
            "status": "pending",
            "order_id": 9
        }

    def test_welcome(self):
        content = self.client.get(
            '/api/v1/',
            content_type='application/json',
            data=json.dumps(self.order)
        )
        self.assertTrue(True)


class OrderTest(unittest.TestCase):

    def test_orderlist(self):
        self.orderlist = [
                        {
                            'order_id': 9,
                            'Food': 'Rice',
                            'amount': 1500,
                            'status': 'pending'}]
        if self.orderlist is None:
            raise ValueError("list is empty")