from flask import Flask, request, jsonify, json, make_response, Response
from app.models import Order, orderlist

app = Flask(__name__)


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
         href="https://fastfood-fast-api-heroku.herokuapp.com/api/v1/">
         next page</a>
        </div>
        '''

    @app.route("/api/v1/", methods=["GET"])
    def welcome():

        '''
            This is the first page
        '''

        return make_response(jsonify({"message": "You are most welcome!"}))

    @app.route("/api/v1/orders", methods=["GET"])
    def get_orders():

        '''
         Retrive/get existing data(orders) from a list
        '''
        response = Order.get_all_orders()
        return response

    @app.route("/api/v1/orders/<int:order_id>", methods=["GET"])
    def get_order(order_id):

        '''
            Retrive/get a single data(order) from a list
        '''
        response = Order.get_order_by_id(order_id)
        return response

    @app.route("/api/v1/orders", methods=["POST"])
    def add_order():

        '''
            send/post data(an order) to a list
        '''
        response = Order.create_order()
        return response

    @app.route("/api/v1/orders/<int:order_id>", methods=["PUT"])
    def edit_order(order_id):

        '''
            change/edit existing data(an order) in a list
        '''
        response = Order.change_order_status(order_id)
        return response

    @app.route("/api/v1/orders/<int:order_id>", methods=["DELETE"])
    def remove_order(order_id):

        '''
            Remove/delete data(an order) from a list
        '''
        response = Order.delete_order(order_id)
        return response

    @app.errorhandler(404)
    def not_found(e):
        return '', 404
