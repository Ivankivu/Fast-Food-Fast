from flask import Flask, jsonify, request

orderlist = []


class Order:

    """new order creation"""

    def __init__(self, order_id=0, Food="fish", amount=3000, status="pending"):
        self.order_id = order_id
        self.Food = Food
        self.amount = amount
        self.status = status
        self.order = {
            "Food": Food,
            "amount": amount,
            "status": status,
            "order_id": order_id
        }

    def validate_json(json):
        if not json or not hasattr(json, orderlist):
            raise NoJsonException()

    def get_order_list():
        return jsonify(orderlist), 201

    def get_all_orders():

        if orderlist == []:
            return jsonify({"error": "orders not found"}), 404
        else:
            return jsonify({'orderlist': orderlist}), 200

    def create_order():
        amount = 0
        data = request.get_json()
        if len(data['Food']) == 0:
            return jsonify({"error": "food should not be empty"}), 404

        if data['Food'].isspace():
            return jsonify({"error": "food should not be empt spaces"}), 404
        if not isinstance(data['amount'], int):
            return jsonify({"error": "amount should be integer"}), 404
        order = {
            'Food': data['Food'],
            'amount': data['amount']
            }
        data['order_id'] = len(orderlist)+1
        order_id = data['order_id']
        order.update({'order_id': data['order_id']})
        data['status'] = "pending"
        order.update({'status': data['status']})
        orderlist.append(order)
        return jsonify({'orderlist': orderlist}), 201

    def get_order_by_id(order_id):
        if orderlist == []:
            return jsonify({"error": "orders not found"}), 404

        orders = [order for order in orderlist
                  if order['order_id'] == order_id]
        if not orders:
            return jsonify({"error": "no match found"}), 404

        return jsonify({'order': orders[0]}), 200

    def change_order_status(order_id):

        data = request.get_json()
        order1 = {
            'Food': data['Food'],
            'amount': data['amount'],
            'status': data['status']
        }
        if orderlist == []:
            return jsonify({"Error": "No orders found"})
        ods = [order for order in orderlist
               if order['order_id'] == order_id]
        ods[0]['status'] = data['status']
        ods[0] = order1
        return jsonify({'orderlist': order1}), 200

    def delete_order(order_id):

        od = [order for order in orderlist
              if order['order_id'] == order_id]
        if not od:
            return jsonify({'error': 'order does not exist'}), 404

        orderlist.remove(od[0])
        return jsonify({'orderlist': orderlist}), 200
