from flask import Flask, request, jsonify, json, make_response


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

    @app.route("/api/orders/<order_id>/", methods=["POST"])
    def add_order():
        order = {"Order_id": request.json["order_id"], "Type": request.json[Type], "Amount": request.json["name"]}
        for order_id in order:
            if order["order_id"] == order_id:
                return "order already exists"
            
        orderlist.append(order.json())
        return jsonify({"order": order}), 200

if __name__ == '__main__':
    app.run(debug=True)
