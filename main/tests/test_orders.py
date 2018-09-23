import unittest
from unittest import TestCase
from views.orders import order_id,orderlist, OnlineRestuarant

class OnlineRestuarantTest(unittest.TestCase):

    def test_welcome(self):
        self.assertTrue(True)

    def test_get_orders(self):
        if orderlist == []:
            raise ValueError("orders not found")
        else:
            self.assertTrue(True)

    def test_not_found(self):
        pass

if __name__ == '__main__':
    unittest.main()
