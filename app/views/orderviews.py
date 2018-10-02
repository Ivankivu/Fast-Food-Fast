from flask import Flask, request, jsonify, json, make_response, Response
from app.models.orders import Order, orderlist

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

    @app.route("/orders/", methods=["GET"])
    def get_orders():

        response = Order.get_all_orders()
        return response

    @app.route("/api/v1/orders/<int:order_id>", methods=["GET"])
    def get_order(order_id):

        response = Order.get_order_by_id(order_id)
        return response

    @app.route("/api/v1/orders", methods=["POST"])
    def add_order():

        response = Order.create_order()
        return response

    @app.route("/api/v1/orders/<int:order_id>", methods=["PUT"])
    def edit_order(order_id):

        response = Order.change_order_status(order_id)
        return response

    @app.route("/api/v1/orders/<int:order_id>", methods=["DELETE"])
    def remove_order(order_id):

        response = Order.delete_order(order_id)
        return response

    @app.errorhandler(404)
    def not_found(e):
        return '', 404
