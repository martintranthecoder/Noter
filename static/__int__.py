# __init__.py inside the 'app' directory
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import main as main_routes  # Relative import within the 'app' package

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    app.register_blueprint(main_routes)

    return app
