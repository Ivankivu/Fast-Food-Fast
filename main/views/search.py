from flask import make_response

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

def find_order(order, order_id):
    for order in orderlist:
        if int(order['order_id']) == order_id:
            return order


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)