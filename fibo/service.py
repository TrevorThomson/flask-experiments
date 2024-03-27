
'''
Define create_service() function.
Usage:
    service = create_service()
    service.run()
'''

import flask

import fibo.api.home
import fibo.api.hello
import fibo.api.fibo

def create_service():
    # create and configure the app
    service = flask.Flask(__name__)

    # register the api endpoints
    service.register_blueprint(fibo.api.home.api)
    service.register_blueprint(fibo.api.hello.api)
    service.register_blueprint(fibo.api.fibo.api)

    return service
