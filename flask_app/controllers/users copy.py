# from flask import Blueprint, render_template, redirect, request, session, flash
# from flask_app.config.mysqlconnection import MySQLConnection
# from flask_app.models.user import User
# from flask_app import app, bcrypt

# users = Blueprint("users", __name__)

# @users.route('/')
# def index():
#     return render_template('index.html')

# @users.route('/reg')
# def reg():
#     return render_template('registration.html')


# @users.route('/registration', methods=['POST'])
# def register():
#     # if not User.validate_register(request.form):
#     #     return redirect('/')
#     data ={ 
#         "first_name": request.form['first_name'],
#         "last_name": request.form['last_name'],
#         "email": request.form['email'],
#         "password": bcrypt.generate_password_hash(request.form['password'])
#     }
    
#     id = User.new_user(data)
#     session['user_id'] = id 
#     return redirect('/')

# @users.route('/login', methods=['GET', 'POST'])
# def login():
#     # form = LoginForm()
#     if request.method == 'POST':
#         # Login logic for handling POST requests
#         user = User.get_by_email(request.form['email'])

#         if not user:
#             flash("Invalid Email", "login")
#             return redirect('/')
#         if not bcrypt.check_password_hash(user.password, request.form['password']):
#             flash("Invalid Password", "login")
#             return redirect('/')
#         session['user_id'] = user.id
#         return redirect('/')
#     else:
#         # Logic for rendering the login form for GET requests
#         return render_template('login.html')  # Pass the form to the template context

# @users.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/')
