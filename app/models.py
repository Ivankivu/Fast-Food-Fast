from flask import Flask, jsonify, request

orderlist = []


class Order:

    """new order creation"""
    increment = 0

    def __init__(self, order_id, food, amount, status):

        order.increment += 1
        self.order_id = order_id.increment
        self.food = food
        self.amount = amount
        self.status = status

    def validate_json(json):
        if not json or not hasattr(json, orderlist):
            raise NoJsonException()

    def get_order_list():
        return jsonify(orderlist)

    def create_order():
        data = request.get_json()
        order = {
            'order_id': data['order_id'],
            'Food': data['Food'],
            'amount': data['amount'],
            'status': data['status']
        }

        for order in orderlist:
            if order['order_id'] == data['order_id']:
                return jsonify({'Alert!!': "already exists"})
            elif order['status'] != data['pending']:
                return jsonify({"Messege": "set status to 'pending'"})
        orderlist.append(order)
        return jsonify({'orderlist': orderlist}), 201

    def get_all_orders():

        if orderlist == []:
            return jsonify({"error": "orders not found"}), 404
        else:
            return jsonify(orderlist), 200

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
            'order_id': data['order_id'],
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
        return jsonify({'orderlist': orderlist}), 200

    def delete_order(order_id):

        od = [order for order in orderlist
              if order['order_id'] == order_id]
        if not od:
            return jsonify({'error': 'order does not exist'}), 404

        orderlist.remove(od[0])
        return jsonify({'orderlist': orderlist}), 200
