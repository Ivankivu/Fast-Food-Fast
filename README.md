[![Build Status](https://travis-ci.org/Ivankivu/Fast-Food-Fast.svg?branch=getallorders)](https://travis-ci.org/Ivankivu/Fast-Food-Fast) | [![Maintainability](https://api.codeclimate.com/v1/badges/5ce73e662ec9328c1345/maintainability)](https://codeclimate.com/github/Ivankivu/Fast-Food-Fast/maintainability) | [![codecov](https://codecov.io/gh/Ivankivu/Fast-Food-Fast/branch/getallorders/graph/badge.svg)](https://codecov.io/gh/Ivankivu/Fast-Food-Fast) | [![Coverage Status](https://coveralls.io/repos/github/Ivankivu/Fast-Food-Fast/badge.svg?branch=getallorders)](https://coveralls.io/github/Ivankivu/Fast-Food-Fast?branch=getallorders)

# Fast-Food-Fast

Fast-Food-Fast is a food delivery service app for a restaurant

## Features

* As a User:
    1. Landing page.
    2. Signup page with a registration form for personal and address information.
    3. Login page with login form and forgot password redirect.
    4. User product selection page.
    5. User view item order and verify
    6. User checkout order
    7. User view and edit profile
    8. User logout

* As an Admin:
    1. Admin login page
    2. Admin view orders page
    3. Admin add, edit and delete food items
    4. Admin mark completed orders
    5. Admin logout

## User Interface [Demo here](https://ivankivu.github.io/Fast-Food-Fast/UI)

### sample gif demo below:-


## Built-with

* Python3.6.6 - Programming language that lets you work more dynamically
* Flask - Python based web framework thats rich with dependecy support
* Virtualenv - A virtual environment for Running the tests

To get started in order to run tests, use this command below in your terminal

pytest -v --cov app --cov-report term-missing

### Installation

Clone this Repository

$ https://github.com/Ivankivu/Fast-Food-Fast.git

$ cd Fast-Food-Fast

Create virtual environment and install it

$ python -m pipenv shell

Install all the necessary dependencies by

$ pip install -r requirements.txt

### Run app by

Run the server At the terminal or console type

$ Python run.py

# API routes and their actions

| REQUEST | ROUTE | ACTION |
| ------- | ----- | ------------- |
| GET | [/api/v1/orders](https://fastfood-fast-api-heroku.herokuapp.com/api/v1/orders) | Returns all orders made |
| POST | [/api/v1/orders](https://fastfood-fast-api-heroku.herokuapp.com/api/v1/orders) | adds a new  order|
| GET | [/api/v1/orders/&lt;order_id&gt;](https://fastfood-fast-api-heroku.herokuapp.com/api/v1/orders/9) | retrieves a specific order |
| PUT | /api/v1/orders/&lt;order_id&gt; | updates the status of a specific order |
| DELETE| [/api/v1/orders/&lt;order_id&gt;](https://fastfood-fast-api-heroku.herokuapp.com/api/v1/orders/9) | removes a specific order |

Use the links in the above table on [Postman](https://www.getpostman.com/apps) to interact with the API


## Author

Ivan
