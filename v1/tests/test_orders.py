import unittest
from flask import Flask, jsonify
from unittest import TestCase
from v1.views.orders import OnlineRestuarant, orderlist


class OnlineRestuarantTest(unittest.TestCase):

    def test_welcome(self):
        self.assertTrue(True)

    def test_get_orders(self):
        if orderlist == []:
            raise ValueError("orders not found")
        else:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
