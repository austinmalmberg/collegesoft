from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from database.queries.users import get_user_by_email, create_new_user
from utils.password_validator import PasswordValidator

password_validator = PasswordValidator()

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        errors = []

        if get_user_by_email(email):
            errors = ['Email already exists']
        else:
            errors = password_validator.validation_errors(password)

        if len(errors) == 0:
            create_new_user(email, password)
            return redirect(url_for('auth.login'))

        for error in errors:
            flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        error = None

        user = get_user_by_email(email)
        if user is None or not check_password_hash(user.pw_hash, password):
            error = 'Incorrect email or password'

        if error is None:
            login_user(user)

            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
