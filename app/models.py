from flask import Flask

orderlist = []

id = 0


class Order:

    """new order creation"""

    def __init__(self, order_id, food, amount, status):
        self.order_id = Order.get_id
        self.food = food
        self.amount = amount
        self.status = status

    def get_id(self):
        if len(orderlist) == 0:
            id = len(orderlist) + 1
        else:
            id = id + 1
        return id

    def list_order(self):
        orderlist = [
                        {
                            'order_id': 9,
                            'Food': 'Rice',
                            'amount': 1500,
                            'status': 'pending'},
                        {
                            'order_id': 4,
                            'Food': 'matooke',
                            'amount': 3000,
                            'status': 'delivered'}
                        ]
        return orderlist
