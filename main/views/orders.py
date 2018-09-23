from flask import Flask, request, jsonify, json, make_response, Response, abort, make_response
<<<<<<< HEAD
from main.controllers.new_order import Order


app = Flask(__name__)

orderlist = Order(12,'oio',455,True).list_order()

class OnlineRestuarant():
    

=======

app = Flask(__name__)

JSON_MIME_TYPE = 'application/json'

orderlist = [
                {'order_id': 10,'Food': 'Rice', 'Amount': 1500, 'Available': False},
                    {'order_id': 12, 'Food': 'matooke', 'Amount': 3000, 'Available': True}
                ]
Available = bool
Amount = float
order_id = int
food = str
order  = "order"

{"order" : {"order_id": order_id, 
                        "Food": food, 
                        "Amount": Amount, 
                        "Available": Available
                            }}

class OnlineRestuarant():

    def find_order(order, order_id):
        for order in orderlist:
            if int(order['order_id']) == order_id:
                return order


    def json_response(data='', status=200, headers=None):
        headers = headers or {}
        if 'Content-Type' not in headers:
            headers['Content-Type'] = JSON_MIME_TYPE

        return make_response(data, status, headers)
    
>>>>>>> 70838b1f4833eb716d3a0920b1da4995ae9e804a
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

<<<<<<< HEAD
        
        return jsonify({'orders':orderlist}), 200

    @app.route("/api/v1/orders/<int:order_id>", methods=["GET"])
    def get_order(order_id):
        
        if orderlist == []:
            return "orders not found", 404

        ods =[order for order in orderlist if order['order_id'] == order_id]
        if not ods:
            return jsonify({"error": "no match found"})

        return jsonify({'order':ods[0]}), 200

    @app.route("/api/v1/orders", methods=["POST"])
    def add_order(order_id):
        data = request.get_json()
        for data in orderlist:
            if data['order_id'] == order_id:
                return jsonify({'error':"already exists"})
        order = {
                'order_id':data['order_id'],
                'Food':data['Food'],
                'amount':data['amount'],
                'available':data['available']
                }
        orderlist.append(order)
        return jsonify({'orderlist': orderlist}), 201

    @app.route("/api/v1/orders/<int:order_id>", methods=["PUT"])
    def edit_order(order_id):
        data = request.get_json()
        order1 = {
                'order_id':data['order_id'],
                'Food':data['Food'],
                'amount':data['amount'],
                'available':data['available']
                }
        ods =[order for order in orderlist if order['order_id'] == order_id]
        ods[0]['available'] = data['available']
        ods[0] = order1
        return jsonify({'orderlist': orderlist}), 200

    @app.route("/api/v1/orders/<int:order_id>", methods=["DELETE"])
    def remove_order(order_id):
       od =[order for order in orderlist if order['order_id'] == order_id]
       if not od:
           return jsonify({'error':'order does not exist'})

       orderlist.remove(od[0])
       return jsonify({'orderlist': orderlist}),200
=======
        response = Response(
            json.dumps(orderlist), status=200)
        return response
>>>>>>> 70838b1f4833eb716d3a0920b1da4995ae9e804a

    @app.errorhandler(404)
    def not_found(e):
        return '', 404

if __name__ == '__main__':
    app.run(debug=True)
<<<<<<< HEAD

=======
>>>>>>> 70838b1f4833eb716d3a0920b1da4995ae9e804a
