# app.py

from flask import Flask
from flask_restful import Api, Resource
import inspect


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = \
    '\x1e0mS\x87\xa3\xf8npw\xed\xb5\xdd\xc3\xb1\xa1\xea\xcerg[\xf2\xff'

import views, models, resources, config
db = resources.db

def add_resources():
    for name, obj in inspect.getmembers(resources):
        if inspect.isclass(obj):
            if obj.__base__ == resources.AutoResource:
                api.add_resource(obj, obj.route)

def create_app(config_type=None):
    app = Flask(__name__, instance_relative_config=True)
    db.init_app(app)

    if config_type is None:
    
    elif config_type == 'dev'
         app.config.from_pyfile(config_filename) 

    elif config_type == 'testing'
        

@app.before_first_request
def create_tables():
    db.create_all()
