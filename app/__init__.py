from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

myapp = Flask(__name__)
myapp.config.from_object(Config)

db = SQLAlchemy(myapp)

login = LoginManager(myapp)
login.login_view = 'login'
login.login_message = "Please login to access this page."
login.refresh_view = 'login'
login.needs_refresh_message = "Please re-login to access this page."


with myapp.app_context():
    from app.models import User, Note
    db.create_all()

from app import routes, models

