from flask import Flask, jsonify, make_response, request, json, Blueprint
import logging
from app.database.server import DBConnection
from app.models.users import User
# from ..controller import UserController
from app import app
import jwt
import datetime
from functools import wraps

# users = Blueprint('users', __name__)

app.config['SECRET_KEY'] = 'andela'


def token_required(f):
    @wrap(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')


class UserView():

    @app.route('/auth/users', methods=['GET'])
    def getusers():
        """
        Return all users
        """
        pass

    @app.route('/auth/signup', methods=['GET', 'POST'])
    def signup():

        """
        Add an user to the database through the Signup
        """
        users = User().adduser()
        return make_response(users)

    @app.route('/auth/login', methods=['GET', 'POST'])
    def login():
        """login user"""

        auth = request.authorization

        if auth and auth.user_password == 'user_password':
            token = jwt.encode({'user_name': auth.user_name, 'exp': datatime.datetime.utcnow() + datetime.timedelta(minutes=5)}, app.config['SECRET_KEY'])
            return jsonify({'token': token.decode('UTF-8')})

        # return make_response(jsonify({'message': 'Login Required'}), 401)
