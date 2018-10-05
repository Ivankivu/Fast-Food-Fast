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
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, app.cofig['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403
        return f(*args, **kwargs)
    return decorated


class UserView():

    @app.route('/auth/users', methods=['GET'])
    @token_required
    def getusers():
        """
        Return all users
        """
        content = User().get_all_users()
        return content

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

        if auth and auth.password == 'user_password':
            token = jwt.encode({'user': auth.username,'exp': datatime.datetime.utcnow() + datetime.timedelta(hour=6)}, app.config['SECRET_KEY'])
            return jsonify({'token': token.decode('UTF-8')})
        return make_response('Could not verify', 401, {'www-Authenticate': 'Basic realm="Login Required"'})

