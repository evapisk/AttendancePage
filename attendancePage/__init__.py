import os

from flask import Flask
from flask_login import LoginManager, login_manager
# from . import models
from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()
login_manager = LoginManager()

import json
from pprint import pprint



def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'attendancePage.sqlite'),
    # )

    # init SQLAlchemy so we can use it later in our models
    db.init_app(app)
    login_manager.init_app(app)


    with app.app_context():
        db.drop_all()
        db.create_all()



    from . import auth
    app.register_blueprint(auth.bp)

    from . import routes
    app.register_blueprint(routes.bp)

    return app

create_app()
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)
