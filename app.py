import os

from flask import Flask

import database
from utils import login_manager


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ['SECRET_KEY'],
        SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'],
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    database.init_app(app)

    login_manager.init_app(app)

    import routes
    routes.register_blueprints(app)

    return app
