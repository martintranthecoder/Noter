from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm, SignupForm, AddNoteForm, CreateFolderForm, SaveNoteForm, ForgotPassword
from flask_login import current_user, login_user, logout_user, login_required
from app import myapp, login
from app import db
from app.models import User, Note, Folder

# login page
@myapp.route("/")
@myapp.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('main_page')) # not sure which page to refer to 
   
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Please make sure you enter correct username and password and try again.")
            return redirect(url_for('login'))
        login_user(user, remember = form.remember_me.data)
        return redirect(url_for('main_page')) 
    
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

#sign up page
@myapp.route("/signup", methods=['GET', 'POST'])
def signup():
    
    form = SignupForm()
    
    if form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations! You have successfully signed up.")
        return redirect(url_for('login'))
    
    return render_template('signup.html', title='Signup', form=form)

# @myapp.route("/signup", methods=['POST'])
# def signup_post():
#     name = request.form.get('name')
#     username = request.form.get('username')
#     email = request.form.get('email')
#     password = request.form.get('password')
    
#     #Check if username and email already exists
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
#     flash("Congratulations! You have successfully signed up.")
    
#     return redirect(url_for('login'))

#logout function
@myapp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out.")
    return redirect(url_for('login'))

#delete account function
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

#main page
@myapp.route('/main_page', methods=['GET','POST'])
@login_required
def main_page():
    all_notes = Note.query.filter_by(user_id=current_user.id, folder_id = None).all()
    length = len(all_notes)
    all_folders = Folder.query.filter_by(user_id=current_user.id).all()
    length1 = len(all_folders)
    form = CreateFolderForm()
    if form.validate_on_submit():
        folder = Folder(title=form.name.data, user_id=current_user.id)
        db.session.add(folder)
        db.session.commit()
        
        return render_template('main_page.html', name = current_user.username, user = current_user, 
                               notes = all_notes, length = length, 
                               folders = Folder.query.filter_by(user_id=current_user.id).all(), 
                               length1 = len(Folder.query.filter_by(user_id=current_user.id).all()), 
                               form = form)
    return render_template('main_page.html', name = current_user.username, user = current_user, notes = all_notes, length = length, folders = all_folders, length1 = length1, form = form)

#create new note function
@myapp.route('/new_note', methods=['GET','POST'])
def new_note():
    form = AddNoteForm()
    if form.validate_on_submit():
        note = Note(title=form.name.data, body=form.body.data, user_id=current_user.id)
        db.session.add(note)
        db.session.commit()
        
        return redirect(url_for('main_page'))
    return render_template('new_note.html', title='New Note', form=form)

@myapp.route('/new_note_folder/<int:folder_id>', methods=['GET','POST'])
def new_note_folder(folder_id):
    form = AddNoteForm()
    if form.validate_on_submit():
        note = Note(title=form.name.data, body=form.body.data, user_id = current_user.id, folder_id = folder_id)
        db.session.add(note)
        db.session.commit()
        
        return redirect("/folder_view/"+str(folder_id))
    return render_template('new_note_folder.html', title='New Note', form=form, folder_id=folder_id)

#delete note function
@myapp.route('/delete/<int:note_id>', methods=['GET','POST'])
def delete_note(note_id):
    form = CreateFolderForm()
    all_folders = Folder.query.filter_by(user_id=current_user.id).all()
    length1 = len(all_folders)
    note = Note.query.filter_by(id=note_id).first()
    if note:
        db.session.delete(note)
        db.session.commit()
        flash("Note deleted.")
    return render_template('main_page.html', name = current_user.username, user = current_user, 
                           notes = Note.query.filter_by(user_id=current_user.id).all(), 
                           length = len(Note.query.filter_by(user_id=current_user.id).all()),
                           folders = all_folders, length1 = length1, form = form)

#edit note function
@myapp.route('/edit/<int:note_id>', methods=['GET','POST'])
def view_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    form = SaveNoteForm(name=note.title, body=note.body)
    
    if form.validate_on_submit():
        db.session.delete(note)
        note = Note(title=form.name.data, body=form.body.data, id=note_id)
        db.session.add(note)
        db.session.commit()

    return render_template('note_view.html', name=note.title, body=note.body, note=note, form=form)

#password reset
@myapp.route('/password_reset', methods=['GET','POST'])
def password_reset():
    form = ForgotPassword()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            new_password = form.new_password.data
            user.set_password(new_password)
            
            db.session.commit()
            flash("Password has been reset.")
            return redirect(url_for('login'))
        else:
            flash("Not valid user information")
            return redirect(url_for('password_reset'))
    
    return render_template('forgot_password.html', form=form)

#view folder function
@myapp.route('/folder_view/<int:folder_id>', methods=['GET','POST'])
def form_view(folder_id):
    folder = Folder.query.filter_by(user_id = current_user.id, id=folder_id).first()
    notes = Note.query.filter_by(user_id = current_user.id, folder_id=folder_id).all()
    length = len(notes)
    return render_template('folder_view.html', folder=folder, notes=notes, length=length)

#delete folder function 
@myapp.route('/delete_folder/<int:folder_id>', methods=['GET','POST'])
def delete_folder(folder_id):
    form = CreateFolderForm()
    folder = Folder.query.filter_by(id=folder_id).first()
    if folder:
        db.session.delete(folder)
        db.session.commit()
        flash("Folder deleted.")
    all_folders = Folder.query.filter_by(user_id=current_user.id).all()
    length1 = len(all_folders)
    return render_template('main_page.html', name = current_user.username, user = current_user, 
                           notes = Note.query.filter_by(user_id=current_user.id).all(), 
                           length = len(Note.query.filter_by(user_id=current_user.id).all()),
                           folders = all_folders, length1 = length1, form = form)