from flask import Flask, request, jsonify, make_response, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
import logging
from app.database.server import DBConnection
import re


class User(object):

    def __init__(self, user_id=int, user_name=str, user_email=str, user_password=str):
        DBConnection.__init__(self)
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        

    # @property
    # def password(self):
    #     return self._password

    # @password.setter
    # def password(self, pwd):
    #     if not pwd:
    #         raise Exception("Field can't be empty")
    #     if len(pwd) < 8 or len(pwd) > 12:
    #         raise Exception(
    #             "Weak password. Password must be 8 characters long")
    #     if not re.search(r'[0-9]', pwd):
    #         raise Exception(
    #             'Weak password. Password should have atleast one integer')
    #     if pwd.isupper() or pwd.islower() or pwd.isdigit():
    #         raise Exception(
    #             'Very Weak password')
    #     self._password = pwd

    # @property
    # def email(self):
    #     return self._email

    # @email.setter
    # def email(self, value):
    #     if not value:
    #         raise Exception("Email field can't be empty")
    #     if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", value):
    #         raise ValueError('Enter Valid Email i.e "example@gmail.com"')
    #         self._email = value

    # @property
    # def username(self):
    #     return self._username

    # @username.setter
    # def username(self, value):
    #     if not value:
    #         raise Exception("Field can't be empty")
    #     if len(value) <= 2:
    #         raise Exception("Name too short.")
    #     if re.compile('[!@#$%^&*:;?><.0-9]').match(value):
    #         raise ValueError("Invalid characters")

    #     self._user_name = value

    def adduser(self):
        data = request.get_json()
        self.user_name = data['user_name']
        self.user_email = data['user_email']
        self.user_password = generate_password_hash(data['user_password'], method='sha256')

        sql = '''INSERT INTO  users(user_name, user_email, user_password) VALUES(%s, %s, %s)'''
        try:
            with DBConnection() as cursor:
                if len(data['user_name']) == 0:
                    return jsonify({"error": "username should not be empty"}), 404

                if len(data['user_email']) == 0:
                        return jsonify(
                            {"error": "email should not be empty"}), 404

                if len(data['user_password']) == 0:
                        return jsonify(
                            {"error": "password should not be empty"}), 404

                if data['user_name'].isspace():
                        return jsonify(
                            {"error": "username should not be empt spaces"}), 404

                if data['user_email'].isspace():
                        return jsonify(
                            {"error": "email should not be empt spaces"}), 404

                if data['user_password'].isspace():
                        return jsonify(
                            {"error": "password should not be empt spaces"}), 404

                cursor.execute("SELECT * FROM users WHERE user_email = '%s'" % self.user_email)
                if cursor.fetchone():
                    return make_response(jsonify({"message": "Email already in use"}), 409)
                else:
                    cursor.execute(sql, (self.user_name, self.user_email, self.user_password))
                    response = cursor.execute("SELECT * FROM users WHERE user_email = '%s'" % self.user_email)
                return make_response(jsonify({"message": "Account Successfully registered"}), 201)
                
        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

    def get_all_users(user_email):
        try:
            with DBConnection() as cursor:
                sql = "select row_to_json(row) from (SELECT * FROM users user_email) row;"
                cursor.execute(sql)
                menu = cursor.fetchall()
                return jsonify(menu)

        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

    