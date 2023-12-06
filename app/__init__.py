from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ckeditor import CKEditor

myapp = Flask(__name__)
# Configuration
myapp.config.from_object(Config)

# Database
db = SQLAlchemy(myapp)

# CKEditor for rich text editing
ckeditor = CKEditor(myapp)

# Login Manager
login = LoginManager(myapp)
login.login_view = 'login'
login.login_message = "Please login to access this page."
login.refresh_view = 'login'
login.needs_refresh_message = "Please re-login to access this page."

#create database tables
with myapp.app_context():
    from app.models import *
    # db.drop_all()
    db.create_all()

from app import routes

