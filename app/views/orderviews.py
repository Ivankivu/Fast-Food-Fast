from flask import Flask, request, jsonify, json, make_response, Response
from app.database.server import DBConnection
import logging
from app.models.orders import Order
from app import app


class OnlineRestuarant(DBConnection):

    @app.route("/", methods=["GET"])
    def Home():
        return '''
        <div style="text-align:center;"><h2 style="font-size:70px;">
        <span style="color:orange;">Fast Food Fast</span>
         Delivery app -API</h2>
        </div><div style="text-align:center;">
        <a style="margin-top:400px;text-decoration:none;
        border:1px solid orange;border-radius:15px;padding:50px;"
         href="https://fastfood-fast-api-heroku.herokuapp.com/users/orders">
         next page</a>
        </div>
        '''

    @app.route("/users/orders", methods=["POST"])
    def add_order():

        data = request.get_json()
        user_name = data['user_name']
        food_type = data['food_type']
        qty = data['qty']

        response = Order.create_order(user_name, food_type, qty)
        return response
