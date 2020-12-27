# config .py

import os


base_dir = os.path.abspath(os.path.dirname(__file__))
base_db = os.path.join(base_dir, 'app.db')
dev_db = os.path.join(base_dir, 'dev_app.db')
test_db = os.path.join(base_dir, 'testing_app.db')


class BaseConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This is a very secure key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + base_db
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + dev_db

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + test_db

