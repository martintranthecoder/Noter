from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm, SignupForm
from flask_login import current_user, login_user, logout_user, login_required
from app import myapp
from app import db
from app.models import User, Note

@myapp.route("/")
@myapp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('notes')) # not sure which page to refer to 
    form = LoginForm()
    
    if login.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Please make sure you enter correct username and password and try again.")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('notes'))
    
    return render_template('login.html', title='Login', form=form)

# @myapp.route("/login", methods=['POST'])
# def login_post():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     remember = True if request.form.get('remember') else False
    
#     #Check if user exists
#     username = User.query.filter_by(username=username).first()
    
#     #Check if password is correct
#     if not username or not username.check_password(password):
#         flash('Please make sure you enter correct username and password and try again.')
#         return redirect(url_for('login'))

@myapp.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('notes'))
    form = SignupForm()
    
    if form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations! You have successfully signed up.")
        return redirect(url_for('login'))
    return render_template('signup.html', title='Signup', form=form)

#@myapp.route("/signup", methods=['POST'])
# def signup_post():
#     name = request.form.get('name')
#     username = request.form.get('username')
#     email = request.form.get('email')
#     password = request.form.get('password')
    
#     #Check if user exists
#     username = User.query.filter_by(username=username).first()
#     email = User.query.filter_by(email=email).first()
    
#     if username:
#         flash('Username already exists.')
#         return redirect(url_for('signup'))
#     if email:
#         flash('Email already exists.')
#         return redirect(url_for('signup'))
    
#     #Create new user
#     new_user = User(name=name, username=username, email=email)
#     new_user.set_password(password)
#     db.session.add(new_user)
#     db.session.commit()
    
#     return redirect(url_for('login'))

@myapp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@myapp.route('/deleteaccount')
@login_required
def deleteaccount():
    #User clicks "Delete Account" option which signs them out and redirects them to homepage
    userId=current_user.id
    user = User.query.get(userId) #getting row which has primary key of user (user id) from database
    logout_user()
    print(user)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('login'))

@myapp.route('/hello')
def hello():
    return "Hello World!"