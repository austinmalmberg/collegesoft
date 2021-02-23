from werkzeug.security import generate_password_hash

from database import db
from database.models import AppUser


def create_new_user(email, password):
    existing_user = AppUser.query.filter_by(email=email).first()
    if existing_user is not None:
        raise ValueError('Email already exists')

    pw_hash = generate_password_hash(password)

    new_user = AppUser(email, pw_hash)
    db.session.add(new_user)
    db.session.commit()

    return new_user


def get_user_by_id(user_id):
    return AppUser.query.get(user_id)


def get_user_by_email(email):
    return AppUser.query.filter_by(email=email).first()
