from flask import Flask

orderlist = [
                {'order_id': 10, 'Food': 'Rice', 'amount': 1500, 'avialable': False},

                    {'order_id': 12, 'Food': 'matooke', 'amount': 3000, 'available': True}
                ]

id = 0


class Order:

    """new order creation"""

    def __init__(self, order_id, food, amount, available):
        self.order_id = Order.get_id
        self.food = food
        self.amount = amount
        self.available = available



    def get_id(self):
        if len(orderlist) == 0:
            id = len(orderlist) + 1
        else:
            id = id + 1
        return id

    def list_order(self):
        orderlist = [
                        {'order_id': 9, 'Food': 'Rice', 'amount': 1500, 'available': 'pending'},
                            {'order_id': 4, 'Food': 'matooke', 'amount': 3000, 'available': 'delivered'}
                        ]
        return orderlist
