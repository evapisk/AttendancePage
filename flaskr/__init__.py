import os

from flask import Flask
from flask_login import LoginManager, login_manager

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # init SQLAlchemy so we can use it later in our models
    db.init_app(app)

    from . import models

    with app.app_context():
        db.create_all()


    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)
    #
    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'



    # login_manager = LoginManager()
    # login_manager.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app


# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)
