
import flask

import api.route.home
import api.route.hello
import api.route.fibo

def create_app():
    # create and configure the app
    app = flask.Flask(__name__)

    app.register_blueprint(api.route.home.api)
    app.register_blueprint(api.route.hello.api)
    app.register_blueprint(api.route.fibo.api)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
