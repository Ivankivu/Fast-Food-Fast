from app.database.server import DBConnection
import logging
from flask import Flask, make_response, jsonify


def validate_user():

    try:
        with DBConnection() as cursor:
            cursor.execute("SELECT * FROM users WHERE user_email = '{}'"
                           .format(self.user_email))

            if cursor.fetchone():
                return make_response(jsonify({
                    "message": "Email already in Exists"}), 409)
            else:
                cursor.execute("SELECT * FROM users WHERE user_email = '{}'"
                               .format(self.user_email))
                return make_response(jsonify({
                    "message": "Successfully registered"}), 201)
    except Exception as e:
        logging.error(e)
        return make_response(jsonify({'message': str(e)}), 500)
