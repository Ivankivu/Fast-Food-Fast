from flask import Flask, Response, request, Blueprint
from app.models.menu import MenuModel
from app import app

# menu = Blueprint('menu', __name__)


class FoodMenu():

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

    @app.route("/menu", methods=['POST'])
    def addfood():
        data = request.get_json()
        food_type = data['food_type']
        food_price = data['food_price']

        response = MenuModel.addnewfood(food_type, food_price)
        return response

    @app.route("/menu", methods=['GET'])
    def getmenu():

        response = MenuModel.getmenu()
        return response
