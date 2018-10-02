from flask import Flask, jsonify, request, make_response
from app.database.server import DBConnection
import logging
from app import app


class Order(DBConnection):

    """new order creation"""

    def create_order(user_name, food_type, qty):

        data = request.get_json()
        user_name = data['user_name']
        food_type = data['food_type']
        qty = data['qty']

        try:
            with DBConnection() as cursor:
                sql = '''INSERT INTO orders(user_name, food_type, qty) VALUES(%s, %s,%s)'''
                cursor.execute(sql, (user_name, food_type, qty))
                return make_response(jsonify({"message": "Order submitted"}), 201)

        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)
