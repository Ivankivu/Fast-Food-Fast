from flask import Flask
from views import orders
from views.orders import app

if __name__ == '__main__':
    app.run(debug=True)
