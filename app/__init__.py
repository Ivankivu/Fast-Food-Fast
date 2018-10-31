from flask import Flask
from app.models.users import User
from app.config import app_config


app = Flask(__name__)

app.config.from_object(app_config["development"])
