from flask import Flask, request, jsonify, make_response
import logging
from app.database.server import DBConnection


class User(DBConnection):

    def adduser(user_name, user_email, user_password):

        data = request.get_json()
        user_name = data['user_name']
        user_email = data['user_email']
        user_password = data['user_password']

        sql = '''INSERT INTO  users(user_name, user_email, user_password) VALUES(%s, %s, %s)'''
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT * FROM users WHERE user_email = '%s'" % user_email)
                if len(data['user_name']) == 0:
                    return jsonify({"error": "username should not be empty"}), 404
                if len(data['user_email']) == 0:
                    return jsonify({"error": "Email should not be empty"}), 404
                if len(data['user_password']) == 0:
                    return jsonify({"error": "Password should not be empty"}), 404

                if data['user_name'].isspace():
                    return jsonify({"error": "Username should not have empty spaces"}), 404
                if data['user_email'].isspace():
                    return jsonify({"error": "Email should not have empty spaces"}), 404
                if data['user_password'].isspace():
                    return jsonify({"error": "Password should not have empty spaces"}), 404

                if not isinstance(data['user_name'], str):
                    return jsonify({"error": "user_name should be a string"}), 404

                if not isinstance(data['user_email'], str):
                    return jsonify({"error": "user_email should be  a string"}), 404
                    
                if cursor.fetchone():
                    return make_response(jsonify({"message": "Email already in use"}), 409)
                else:
                    cursor.execute(sql, (user_name, user_email, user_password))
                    cursor.execute("SELECT * FROM users WHERE user_email = '%s'" % user_email)
                return make_response(jsonify({"message": "Successfully registered"}), 201)
                
        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)
