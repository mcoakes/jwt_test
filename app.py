# app.py

from flask import Flask, current_app
from flask_restful import Api, Resource
import inspect

'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = \
    '\x1e0mS\x87\xa3\xf8npw\xed\xb5\xdd\xc3\xb1\xa1\xea\xcerg[\xf2\xff'
'''

import views, models, resources, config
db = models.db

def add_resources(api):
    for name, cls in inspect.getmembers(resources):
        try:
            if cls.__base__ == resources.AutoResource:
                api.add_resource(cls, cls.route)
        except Exception as e:
            pass

def create_app(config_type=None):
    app = Flask(__name__, instance_relative_config=True)
    db = models.db

    api = Api(app) 
    add_resources(api)
    app.register_blueprint(views.route_blueprint)    

    if config_type is None:
        app.config.from_object(config.BaseConfig)    
    elif config_type == 'dev':
         app.config.from_object(config.DevConfig)
    elif config_type == 'testing':
        app.config.from_object(config.TestingConfig)
    else:
        raise ValueError("Invalid config type.")

    @app.before_first_request
    def create_db():
        db.init_app(app)
        db.create_all()
    
    return app
