from flask import Flask, request, jsonify, json, make_response, Blueprint

od = Blueprint('orders', __name__)

app = Flask(__name__)

orderlist = ["u can see me"]


class OnlineRestuarant():

    @app.route("/api/v1/", methods=["GET"])
    def welcome():
        return make_response(jsonify({"message": "You are most welcome!"}))

    @app.route("/api/v1/orders", methods=["GET"])
    def get_orders():
        if orderlist == []:
            return "orders not found", 404
        else:
            return make_response(jsonify({"orders": orderlist}), 200)

if __name__ == '__main__':
    app.run(debug=True)
