# # flask_app/models/user.py
# from flask_app.config.mysqlconnection import connectToMySQL
# from flask import flash
# from flask_app import app, bcrypt
# import re
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Email



# password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# letters_regex = re.compile(r'^[a-zA-Z]+$')

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[InputRequired(), Email()])
#     password = PasswordField('Password', validators=[InputRequired()])
#     submit = SubmitField('Login')
    
    
# class User:
#     db = ""

#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.email = data['email']
#         self.password = data['password']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']

#     @classmethod
#     def get_all(cls):
#         query = """
#             SELECT * FROM users;
#         """
#         results = connectToMySQL(cls.db).query_db(query)
#         users = []
#         for user in results:
#             users.append(cls(user))
#         return users

#     @classmethod
#     def new_user(cls, data):
#         # Hash the password before storing it in the database
#         hashed_password = bcrypt.generate_password_hash(data['password'])
#         data['password'] = hashed_password

#         query = """
#             INSERT INTO users (first_name, last_name, email, password)
#             VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
#         """
#         return connectToMySQL(cls.db).query_db(query, data)
    
#     @classmethod
#     def get_user_by_id(cls, data):
#         query = """
#             SELECT * FROM users WHERE id = %(id)s;
#         """
#         result = connectToMySQL(cls.db).query_db(query, data)
#         return cls(result[0]) if result else None
    
#     @classmethod
#     def get_by_email(cls, data):
#         query = """
#             SELECT * FROM users WHERE email = %(email)s;
#         """
#         result = connectToMySQL(cls.db).query_db(query, data)
#         return cls(result[0]) if result else None

#     def check_password(self, password):
#         # Check if the provided password matches the hashed password in the database
#         return bcrypt.check_password_hash(self.password, password)

#     # validates complete
#     @staticmethod 
#     def validate_register(user):
#         is_valid = True
#         query = "SELECT * FROM users WHERE email = %(email)s;"
#         results = connectToMySQL(User.db).query_db(query,user)
#         if len(results) >= 1:
#             flash("Email already in use","register")
#             is_valid = False
#         if not EMAIL_REGEX.match(user['email']):
#             flash("Invalid Email, please try again","register")
#             is_valid = False
#         if len(user['first_name']) < 2:
#             flash("First name must be at least 2 characters","register")
#             is_valid = False
#         if len(user['last_name']) < 2:
#             flash("Last name must be at least 2 characters","register")
#             is_valid = False
#         if len(user['password']) < 8:
#             flash("Password must be at least 8 characters","register")
#             is_valid = False
#         if user['password'] != user['confirm']:
#             flash("Passwords must match","register")
#             is_valid = False
#         return is_valid