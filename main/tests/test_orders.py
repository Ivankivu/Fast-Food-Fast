import unittest
from unittest import TestCase
<<<<<<< HEAD
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
        self.order ={ "Food": "Rice",
            "amount": 1500,
            "available": "pending",
            "order_id": 9
        }

    def test_get_all_orders(self):
        orders = self.client.get(
            '/api/v1/orders',
            content_type = 'application/json',
            data = json.dumps(self.order)
        )
       # data = json.loads(orders.data.decode())
        self.assertEqual(orders.available_code,200)
        self.assertIn('"order_id":9',str(orders.data))

    def test_ii_post_order(self):
        order_list = []
        order1 = self.client.post(
            '/api/v1/orders',
            content_type = 'application/json',
            data = json.dumps(self.order)
        )
        order ={ "Food": "Rice",
            "amount": 1500,
            "available": "pending",
            "order_id": 9
        }

        order_list.append(order)
        self.assertEqual(order1.available_code,201)
        self.assertIn('"order_id":9',str(order1.data))

=======
from views.orders import order_id,orderlist, OnlineRestuarant

class OnlineRestuarantTest(unittest.TestCase):

>>>>>>> 70838b1f4833eb716d3a0920b1da4995ae9e804a
    def test_welcome(self):
        self.assertTrue(True)

    def test_get_orders(self):
<<<<<<< HEAD
        raise ValueError("orders not found")
       
=======
        if orderlist == []:
            raise ValueError("orders not found")
        else:
            self.assertTrue(True)
>>>>>>> 70838b1f4833eb716d3a0920b1da4995ae9e804a

    def test_not_found(self):
        pass

if __name__ == '__main__':
    unittest.main()
