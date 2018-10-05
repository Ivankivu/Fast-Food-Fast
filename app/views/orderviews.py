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
    def __init__(self, user_name=str, food_type=str, qty=int, order_id=int):

        """
            This method acts as a constructor
            for our class, its used to initialise class attributes
        """

        self.user_name = user_name
        self.food_type = food_type
        self.qty = qty
        self.order_id = order_id

    @app.route("/users/orders", methods=['POST'])
    def add_order():

        response = Order.create_order()
        return response

    @app.route("/orders/", methods=["GET"])
    def get_orders():

        response = Order.get_all_orders()
        return jsonify({"Available orders": response})

    @app.route("/orders/<order_id>", methods=['POST', 'GET'])
    def get_order(order_id):

        response = Order.get_order_by_id(order_id)
        # if not response:
        #     return jsonify({"message": "No order found"}), 404
        return jsonify({"Order":response})

    @app.route("/users/orders/<user_name>", methods=["GET"])
    def order_history(user_name):

        response = Order.get_order_history(user_name)
        return response

    @app.route("/users/orders/<order_id>", methods=['PUT'])
    def order_change():

        response = Order.change_order_status()
        return response
