# flask_app/controllers/users.py
from flask import Blueprint, render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app import app, bcrypt

users = Blueprint("users", __name__)

@users.route('/')
def index():
    if "user_id" not in session: 
        user = None
    else:
        user = User.get_by_id({"id": session["user_id"]})
    return render_template('index.html', user = user)

@users.route('/reg')
def reg():
    return render_template('registration.html')

@users.route('/registration', methods=['POST'])
def register():
    if request.method == 'POST':
        # Extract user registration data from the form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        # Create a dictionary to hold the user registration data
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "confirm": confirm
        }

        # Validate the user registration data using the static method
        is_valid = User.validate_register(user_data)

        if not is_valid:
            # If the data is not valid, redirect back to the registration page
            return redirect('/reg')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": hashed_password
        }

        id = User.new_user(data)
        session['user_id'] = id 
        session['logged_in'] = True 
        print("A", id)
        return redirect('/')

    return redirect('/reg')

@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.get_by_email({"email": email})
        print("B", user)
        if not user:
            flash("Invalid Email", "login")
            return redirect('/')

        if not bcrypt.check_password_hash(user.password, password):
            flash("Invalid Password", "login")
            return redirect('/')

        session['user_id'] = user.id
        session['logged_in'] = True
        return redirect('/')
    else:
        user_id = session.get('user_id')
        user = None
        if user_id:
            user = User.get_by_id({"id": user_id})
        return render_template('login.html', user=user)

@users.route('/logout')
def logout():
    session.clear()
    return redirect('/')
