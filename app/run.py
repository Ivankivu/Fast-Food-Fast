from flask import Flask
from app.views import orderviews
from app.views import userviews
from app.views import menuviews
from app import app

# app.config.from_pyfile('config.py')

if __name__ == '__main__':
    app.run(debug=True)
