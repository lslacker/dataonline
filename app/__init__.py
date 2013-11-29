__author__ = 'lslacker'
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

# initialize the Flask app
app = Flask(__name__)

# initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)

# forward to login page, if not authenticated
login_manager.login_view = "login"

app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

