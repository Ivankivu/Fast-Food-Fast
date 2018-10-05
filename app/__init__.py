from flask import Flask
from app.models import users
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
                                get_jwt_identity)

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'andela'
jwt = JWTManager(app)

app.config.from_object(app_config["development"])
