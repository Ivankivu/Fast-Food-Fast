from flask import Flask
from v1.views.orders import app

app.register_blueprint(views.orders.od, url_prefix='/api/v1')
