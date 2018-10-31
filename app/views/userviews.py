from flask import Flask, jsonify, make_response, request, json, Blueprint
import logging
from app.database.server import DBConnection
from app.models.users import User
from app import app
import jwt
import datetime
from functools import wraps


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
        pass

    @app.route('/auth/login', methods=['GET', 'POST'])
    def login():
        """login user"""
        pass
