# views.py

#from run import app
from flask import Blueprint, current_app, jsonify
route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/')
def index():
    return jsonify(
        { 'message': 'I\'ll Create a landing page someday...' }
    )
