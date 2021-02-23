from datetime import datetime

from flask_login import UserMixin
from database import db


class AppUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    pw_hash = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, email, pw_hash):
        self.email = email
        self.pw_hash = pw_hash
