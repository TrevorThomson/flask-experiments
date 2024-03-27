'''
Define the hello/ endpoint
Usage:
    <url>/hello/<name>
'''

from flask import Blueprint
from markupsafe import escape

api = Blueprint('hello_api', __name__)

@api.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello, {escape(name)}!</h1>', 200
