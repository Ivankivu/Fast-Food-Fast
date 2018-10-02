from flask import Flask, jsonify, make_response, request, json
import logging
from app.database.server import DBConnection
from app.models.users import User
from app import app


class UserView(User):

    @app.route("/", methods=["GET"])
    def index():
        return '''
        <div style="text-align:center;"><h2 style="font-size:70px;">
        <span style="color:orange;">Fast Food Fast</span>
         Delivery app -API</h2>
        </div><div style="text-align:center;">
        <a style="margin-top:400px;text-decoration:none;
        border:1px solid orange;border-radius:15px;padding:50px;"
         href="https://fastfood-fast-api-heroku.herokuapp.com/api/v1/">
         next page</a>
        </div>
        '''

    @app.route('/auth/signup', methods=['GET', 'POST'])
    def signup():

        """
        Add an user to the database through the Signup
        """
        data = request.get_json()
        user_name = data['user_name']
        user_email = data['user_email']
        user_password = data['user_password']
        response = User.adduser(user_name, user_email, user_password)
        return response

    @app.route('/auth/login', methods=['GET', 'POST'])
    def login():
        """
        login user
        """
        pass
