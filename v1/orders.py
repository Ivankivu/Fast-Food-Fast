from flask import Flask, jsonify

restuarant = Flask(__name__)


orderlist = ["u can see me"]


class OnlineRestuarant():

    def __init__():
        pass

    @restuarant.route("/api/v1/", methods=["GET"])
    def welcome():
        return jsonify({"message": "You are most welcome!"})

    @restuarant.route("/api/v1/orders", methods=["GET"])
    def get_orders():
        if orderlist == []:
            return "orders not found", 404
        else:
            return jsonify({"orders": orderlist}), 200

    if __name__ == '__main__':
        restuarant.run(debug=True, port=5000)
