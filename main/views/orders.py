from flask import Flask, request, jsonify, json, make_response, Response, abort

from search import  JSON_MIME_TYPE, find_order, order_id, orderlist, Amount,food, Available, order

app = Flask(__name__)

class OnlineRestuarant():
    
    @app.route("/", methods=["GET"])
    def Home():
        return '''
        <div style="text-align:center;"><h2 style="font-size:70px;"> <span style="color:orange;">Fast Food Fast</span> Delivery app -API</h2>
        </div><div style="text-align:center;"><a style="margin-top:400px;text-decoration:none;border:1px solid orange;border-radius:15px;padding:50px;" href="https://fastfood-fast-api-heroku.herokuapp.com/api/v1/">next page</a>
        </div>
        '''
        
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
