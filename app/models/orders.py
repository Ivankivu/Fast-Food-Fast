from flask import Flask, jsonify, request, make_response
import logging
from app.database.server import DBConnection
from app import app
from app.models.users import User


class Order(object):

    """new order creation"""

    def __init__(self, user_name=str, food_type=str, qty=int, order_id=int):

        """
            This method acts as a constructor
            for our class, its used to initialise class attributes
        """
        DBConnection.__init__(self)
        self.user_name = user_name
        self.food_type = food_type
        self.qty = qty
        self.order_id = order_id

    def create_order(self):

        data = request.get_json()
        self.user_name = data['user_name']
        self.food_type = data['food_type']
        self.qty = data['qty']

        try:
            with DBConnection() as cursor:
                sql = '''
                INSERT INTO orders(user_name, food_type, qty)
                 VALUES(%s, %s,%s)'''
                cursor.execute(sql, (self.user_name, self.food_type, self.qty))
                return make_response(jsonify(
                 {"message": "Successfully registered"}), 201)  

        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)
     
    def get_all_orders():

        try:
            with DBConnection() as cursor:
                sql = "SELECT * FROM orders food_type;"
                cursor.execute(sql)
                menu = cursor.fetchall()
                return menu

        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    def get_order_by_id(order_id):
        try:
            with DBConnection() as cursor:
                sql = "select row_to_json(row) from (SELECT * FROM users user_email) row;"
                cursor.execute(sql)
                menu = cursor.fetchall()
                return jsonify(menu)

        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

    def get_order_history(self):

        data = request.get_json()
        
        try:
            with DBConnection() as cursor:
                self.user_name = data['user_name']
                sql = ("SELECT order_id, food_type, user_name, created_timestamp, status from orders where user_name = %s" % self.user_name)
                cursor.execute(sql, (self.user_name))
                history = cursor.fetchall()
                return make_response(jsonify({'order-history': history}))

        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

    def change_order_status():
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT * FROM orders WHERE order_id = %s AND status = %s", (order_id, status))

                if not cursor.fetchone():
                    return make_response(jsonify({"message": "Status doesn't exist"}), 400)

                sql = "UPDATE orders SET status_type = %s where status = %s AND qtn_id = %s"

                cursor.execute(sql, (order_id, status))
                return jsonify({"message": "Reply Edited successfully"})
        except Exception as e:
            raise e
