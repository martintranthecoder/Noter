from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User
# Import Flask-Login functions if you are using Flask-Login
# from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')  # Assuming you have an email field

        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('main.signup'))

        if User.query.filter_by(email=email).first():
            flash('Email already exists. Please choose a different one.', 'danger')
            return redirect(url_for('main.signup'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('main.signin'))
    
    return render_template('signup.html')

@main.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            # login_user(user)  # Uncomment if using Flask-Login
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('signin.html')

@main.route('/logout')
# @login_required  # Uncomment if using Flask-Login
def logout():
    # logout_user()  # Uncomment if using Flask-Login
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.index'))

@main.route('/')
def index():
    return render_template('index.html')

