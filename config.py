import os
basedir = os.path.abspath(os.path.dirname(__file__))


class DevConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'postgres://postgres:123@db:5432/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
