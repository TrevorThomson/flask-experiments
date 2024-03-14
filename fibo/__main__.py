
import flask

import fibo.api.home
import fibo.api.hello
import fibo.api.fibo

def create_service():
    # create and configure the app
    service = flask.Flask(__name__)

    service.register_blueprint(fibo.api.home.api)
    service.register_blueprint(fibo.api.hello.api)
    service.register_blueprint(fibo.api.fibo.api)

    return service

if __name__ == '__main__':
    service = create_service()
    service.run()
