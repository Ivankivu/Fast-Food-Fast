[![Build Status](https://travis-ci.org/Ivankivu/Fast-Food-Fast.svg?branch=user-sign-in%2Fout)](https://travis-ci.org/Ivankivu/Fast-Food-Fast) | [![Coverage Status](https://coveralls.io/repos/github/Ivankivu/Fast-Food-Fast/badge.svg?branch=user-sign-in/out)](https://coveralls.io/github/Ivankivu/Fast-Food-Fast?branch=user-sign-in/out)

# Fast-Food-Fast - API

Fast-Food-Fast is a food delivery service app for a restaurant

## Features

* As a User:
    1. I should signup for a new account.

## Built-with

* Python3.6.6 or higher - Programming language that lets you work more dynamically
* Flask - Python based web framework thats rich with dependecy support
* Virtualenv - A virtual environment for Running the tests
* Postgresql database

To get started in order to run tests, use this command below in your terminal

`pytest -v --cov app --cov-report term-missing`

### Installation

Clone this Repository

[clone this](https://github.com/Ivankivu/Fast-Food-Fast.git)

`$ cd Fast-Food-Fast`

Create virtual environment and install it

`$ python3 -m pipenv shell`

Install all the necessary dependencies by

`$ pip install -r requirements.txt`

### Run app by

Run the server At the terminal or console type

`$ Python run.py`

use this sample data to test the API functionality

`{
"food_type": "katogo",
"food_price": 5000
}`

# API routes and their actions

| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| POST | [/api/v2/auth/signup](https://fastfood-fast-api-heroku.herokuapp.com/api/v2/auth/signup) | Register new user |
| POST | [/api/v2/menu](https://fastfood-fast-api-heroku.herokuapp.com/api/v2/menu) | Add a meal option to the menu |
| GET | [/api/v2/menu](https://fastfood-fast-api-heroku.herokuapp.com/api/v2/menu) | Get Menu|
| GET | [/api/v2/users/orders](https://fastfood-fast-api-heroku.herokuapp.com/api/v2/users/orders) | Place an order for food|


Use the links in the above table on [Postman](https://www.getpostman.com/apps) to interact with the API

## Author

Ivan Kivumbi
