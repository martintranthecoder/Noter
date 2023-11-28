from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

myapp = Flask(__name__)
myapp.config.from_object(Config)
db = SQLAlchemy(myapp)
login = LoginManager(myapp)
login.login_view = 'login'


with myapp.app_context():
    from app.models import User, Note
    db.create_all()

from app import routes, models

