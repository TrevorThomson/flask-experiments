'''
Define the home/ endpoint
Usage:
    <url>/home
'''

from flask import Blueprint

api = Blueprint('home_api', __name__)

@api.route('/')
def index():
    return '<h1>Home Page</h1>', 200
