from flask import Flask, request, jsonify, json, make_response, Response, abort

from .search import  JSON_MIME_TYPE, find_order, order_id, orderlist, Amount,food, Available, order

app = Flask(__name__)

class OnlineRestuarant():
    
    @app.route("/api/v1/", methods=["GET"])
    def welcome():
        return make_response(jsonify({"message": "You are most welcome!"}))

    @app.route("/api/v1/orders", methods=["GET"])
    def get_orders():
        
        if orderlist == []:
            return "orders not found", 404

        response = Response(
            json.dumps(orderlist), status=200)
        return response

    @app.errorhandler(404)
    def not_found(e):
        return '', 404

if __name__ == '__main__':
    app.run(debug=True)
