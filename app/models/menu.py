from flask import Flask, make_response, jsonify, request, json
import logging
from app.database.server import DBConnection


class MenuModel():

    def addnewfood(food_type, food_price):
        data = request.get_json()
        food_type = data['food_type']
        food_price = data['food_price']

        try:
            with DBConnection() as cursor:
                sql = '''INSERT INTO menu(food_type, food_price) VALUES(%s, %s)'''
                cursor.execute("SELECT * FROM menu WHERE food_type = '%s'" % food_type)
                cursor.execute(sql, (food_type, food_price))
                cursor.execute("SELECT * FROM menu WHERE food_type = '%s'" % food_type)
                return make_response(jsonify({"message": "Successfully Added to menu"}), 201)

        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

    def getmenu():

        try:
            with DBConnection() as cursor:
                sql = "select row_to_json(row) from (SELECT * FROM menu food_type) row;"
                cursor.execute(sql)
                menu = cursor.fetchall()
                return jsonify(menu)
                # return make_response(jsonify({"message": "Successfully Added to menu"}), 201)

        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)