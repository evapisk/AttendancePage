import functools


from flask_login import LoginManager, login_user

from flask import Blueprint, render_template, redirect, url_for, request, session, flash, g
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, db


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
            return redirect(url_for('auth.register'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, password=password)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(
            email=email).first()  # if this returns a user, then the email already exists in database

        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            flash('Logged in successfully.')
            print('Logged in successfully.')
            user.is_active = True
            login_user(user, remember=True)
            return redirect(url_for('main'))
        print("login failed")

    return render_template('auth/login.html')




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


