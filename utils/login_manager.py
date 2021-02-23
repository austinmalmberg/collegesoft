from flask import redirect, url_for
from flask_login import LoginManager

from database.queries.users import get_user_by_id

login_manager = LoginManager()


def init_app(app):
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return None

    return get_user_by_id(user_id)


def handle_unauthorized_user():
    return redirect(url_for('auth.login'))
