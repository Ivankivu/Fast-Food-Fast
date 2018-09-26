from flask import Flask, jsonify, request

orderlist = [
    {
        "Food": "matooke",
        "amount": 1500,
        "order_id": 4,
        "status": "pending"
    },
    {
        "Food": "posho",
        "amount": 1500,
        "order_id": 15,
        "status": "pending"
    }
]


class Order:

    """new order creation"""

    def __init__(self, order_id, food, amount, status):
        self.order_id = order_id
        self.food = food
        self.amount = amount
        self.status = status

    def list_order(self):
        orderlist = []
        return orderlist

    def json_data(self):
        return {
            'order_id': self.order_id,
            'food': self.food,
            'amount': self.amount,
            'status': self.status}

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
        orderlist.append(order)
        return jsonify({'orderlist': orderlist}), 201

    def get_all_orders():

        if orderlist == []:
            return "orders not found", 404
        else:
            return jsonify(orderlist), 200

    def get_order_by_id(order_id):

        if orderlist == []:
            return "orders not found", 404

        ods = [order for order in orderlist if order['order_id'] == order_id]
        if not ods:
            return jsonify({"error": "no match found"})

        return jsonify({'order': ods[0]}), 200

    def change_order_status(order_id):

        data = request.get_json()
        order1 = {
                'order_id': data['order_id'],
                'Food': data['Food'],
                'amount': data['amount'],
                'status': data['status']
                }
        ods = [order for order in orderlist if order['order_id'] == order_id]
        ods[0]['status'] = data['status']
        ods[0] = order1
        return jsonify({'orderlist': orderlist}), 200

    def delete_order(order_id):

        od = [order for order in orderlist if order['order_id'] == order_id]
        if not od:
            return jsonify({'error': 'order does not exist'})

        orderlist.remove(od[0])
        return jsonify({'orderlist': orderlist}), 200
