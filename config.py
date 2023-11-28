import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never know it is a secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'myapp.db')
    # disable a feature of FlaskSQLAlchemy that is not needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False