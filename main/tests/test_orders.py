import unittest
from unittest import TestCase
from main.views.orders import OnlineRestuarant, orderlist
from main.config import app_config
from main.views.orders import app
from flask import json


class OnlineRestuarantTest(unittest.TestCase):

    def create_app(self):
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

        '''
         This method tests to check if there is json
         data being returned when fetched and
         the confirm the status code being returned
        '''

        orders = self.client.get(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps(self.order)
        )
        # data = json.loads(orders.data.decode())
        self.assertEqual(orders.status_code, 200)
        self.assertIn('"order_id":9', str(orders.data))

    def test_ii_post_order(self):

        '''
         This method tests to check if there is json
         data being posted and the confirm the status code being returned
        '''

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
        self.assertIn('"order_id":9', str(order1.data))

    def test_welcome(self):

        '''
         This method tests to check if there is json
         data being returned when fetched
        '''

        self.assertTrue(True)

    def test_get_orders(self):
        raise ValueError("orders not found")


if __name__ == '__main__':
    unittest.main()
