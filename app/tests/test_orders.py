import unittest
from unittest import TestCase
from app.views import OnlineRestuarant, app
from config import app_config
from app.models import orderlist, Order
from flask import Flask, json, jsonify


class OnlineRestuarantTest(unittest.TestCase):

    def setUp(self):
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)
        self.order = {
            "Food": "Rice",
            "amount": 1500,
            "status": "pending",
            "order_id": 9
        }

    def test_get_all_orders(self):
        order_list = []
        orders = self.client.get(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps({'order': self.order})
        )
        return orders
        self.assertEqual(201, orders.status_code)

    def test_ii_post_order(self):

        order_list = []
        order1 = self.client.post(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps(self.order)
        )
        order = {
            "Food": "Rice",
            "amount": 1500,
            "status": "pending",
            "order_id": 9
        }

        order_list.append(order)
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


if __name__ == '__main__':
    unittest.app()
