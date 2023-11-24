from app import myapp
from flask import render_template

@myapp.route('/home')
def home_page():
    return render_template('main_page.html')

@myapp.route('/login')
def login():
    return render_template('login.html')

@myapp.route('/signup')
def signup():
    return render_template('signhup.html')

@myapp.route('/note')
def create():
    return render_template('new_note.html')

