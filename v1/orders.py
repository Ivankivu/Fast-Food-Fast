from flask import Flask, jsonify

restuarant = Flask(__name__)


order = ["u can see me"]


class OnlineRestuarant():

    def __init__(self):
        pass

    @restuarant.route("/api/v1/", methods=["GET"])
    def welcome():
        return jsonify({"message": "You are most welcome!"})

    @restuarant.route("/api/v1/orders", methods=["GET"])
    def get_orders():
        if order == []:
            return "orders not found", 404
        else:
            return jsonify({"orders": order}), 200

    if __name__ == '__main__':
        restuarant.run(debug=True, port=5000)
