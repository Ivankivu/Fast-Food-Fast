
from flask import Flask, json, jsonify, request, Response
import unittest
from unittest import TestCase

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

    def TearDown():

    def test_get_all_orders(self):
   
    # def test_get_order(self):

    # def test_orderid(self):
    
    # def test_default_status(self):
    
    # def test_Food_value(self):
   

    # def test_amount_value(self):
   
    # def test_item_posted(self):
   
    # def test_food_empty_string(self):


    # def test_ii_post_order(self):
