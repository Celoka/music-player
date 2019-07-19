import os

from flask_api import FlaskAPI
from flask_bcrypt import Bcrypt

from app.utils import db
from app.blueprints.base_blueprint import BaseBlueprint
from config import env, get_env


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(env.app_env[config_name])
    app.config.from_pyfile('../config/env.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app


app = create_app(get_env('APP_ENV'))
bcrypt = Bcrypt(app)
db.init_app(app)
blueprint = BaseBlueprint(app)
blueprint.register()
