from flask import Flask, jsonify
from app.database.server import DBConnection
from app.models.users import User
from app import app


class UserView():

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

    @app.route('/auth/signup/', methods=['POST'])
    def signup():

        """
        Add an user to the database through the Signup form
        """
        response2 = User('', '', '').adduser()
        if not response2:
            return jsonify({'error': "dfg"})
        return jsonify({'message': response2})
