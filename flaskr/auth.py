import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_login import LoginManager



from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

bp = Blueprint('auth', __name__, url_prefix='/auth')
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(
            email=email).first()  # if this returns a user, then the email already exists in database

        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, password=password)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    if request.method == 'POST':
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flash('Logged in successfully.')
        print('Logged in successfully.')


        return redirect(url_for('hello'))
    return render_template('auth/login.html')



@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


