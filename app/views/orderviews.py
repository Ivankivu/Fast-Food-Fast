from flask import Flask, request, jsonify, json, make_response, Response, Blueprint
from app.database.server import DBConnection
from app.models.orders import Order
from app.models.users import User
import logging

from app import app

orders = Blueprint('orders', __name__)


class OnlineRestuarant():

    @app.route("/", methods=["GET"])
    def Home():
        return '''
        <div style="text-align:center;"><h2 style="font-size:70px;">
        <span style="color:orange;">Fast Food Fast</span>
         Delivery app -API</h2>
        </div><div style="text-align:center;">
        <a style="margin-top:400px;text-decoration:none;
        border:1px solid orange;border-radius:15px;padding:50px;"
         href="https://http://127.0.0.1:5000/signup">
         next page</a>
        </div>
        '''

    @app.route("/users/orders", methods=['POST'])
    def add_order():
        
        response = Order().create_order()
        return response

    @app.route("/orders/", methods=["GET"])
    def get_orders():

        response = Order.get_all_orders()
        return response

    @app.route("/orders/<order_id>", methods=["GET"])
    def get_order(order_id):

        response = Order.get_order_by_id()
        return response

    @app.route("/users/orders/<user_name>", methods=["GET"])
    def order_history(user_name):

        response = Order.get_order_history(user_name)
        return response

    @app.route("/users/orders/<order_id>", methods=['PUT'])
    def order_change():

        response = Order.change_order_status()
        return response
