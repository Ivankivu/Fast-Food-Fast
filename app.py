from flask import Flask
from main.views import orders
from main.views.orders import app

if __name__ == '__main__':
    app.run(debug=True)
