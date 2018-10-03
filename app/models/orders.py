from flask import Flask, jsonify, request, make_response
import flask
import logging
from app.database.server import DBConnection
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
                if request.method == 'GET':
                    cursor.execute("SELECT distinct food_type, food_price from menu")
                    menu = cursor.fetchall()
                return jsonify({"Menu": menu}), 201

                if len(data['user_name']) == 0:
                    return jsonify({"alert": "insert a food choice"}), 404

                if len(data['food_type']) == 0:
                    return jsonify({"alret": "food should not be empty"}), 404

                # if (data['qty']) == 0:
                #     return jsonify({"error": "food should not be empty"}), 404

                if data['user_name'].isspace():
                    return jsonify({"caution!": "food should not be empt spaces"}), 404

                if data['food_type'].isspace():
                    return jsonify({"caution!": "food should not be empt spaces"}), 404

                # if data['qty'].isspace():
                #     return jsonify({"error": "food should not be empt spaces"}), 404

                if not isinstance(data['user_name'], str):
                    return jsonify({"error": "user_name should be a string"}), 404

                if not isinstance(data['food_type'], str):
                    return jsonify({"error": "Food type should be a string"}), 404
                
                if not isinstance(data['qty'], int):
                    return jsonify({"error": "Quantity should be integer"}), 404

                if data['food_type'] != cursor.fetchone():
                    return jsonify({"message": "food_type not avalilable on the menu"}), 404
                else:
                    sql = '''INSERT INTO orders(user_name, food_type, qty) VALUES(%s, %s,%s)'''
                    cursor.execute(sql, (user_name, food_type, qty))
                return make_response(jsonify({"message": "Order submitted"}), 201)

        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

    def get_all_orders():

        try:
            with DBConnection() as cursor:
                sql = "select row_to_json(row) from (SELECT * FROM orders food_type) row;"
                cursor.execute(sql)
                menu = cursor.fetchall()
                return jsonify(menu)

                # return make_response(jsonify({"message": "Successfully Added to menu"}), 201)

        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)
