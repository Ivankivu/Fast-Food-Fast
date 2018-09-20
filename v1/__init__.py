from flask import Flask
from v1.views.orders import restuarant

restuarant.register_blueprint(views.orders.od, url_prefix='/api/v1')
