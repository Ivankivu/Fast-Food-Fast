from flask import Flask, request, jsonify, json, make_response, Response
from app.database.server import DBConnection
from app.models.orders import Order
from app.models.users import User
import logging
from app import app


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

        pass

    @app.route("/orders/", methods=["GET"])
    def get_orders():

        pass

    @app.route("/orders/<int:order_id>", methods=['GET'])
    def get_order():

        pass

    @app.route("/users/orders/<user_name>", methods=["GET"])
    def order_history(user_name):

        pass

    @app.route("/users/orders/<order_id>", methods=['PUT'])
    def order_change():

        pass
