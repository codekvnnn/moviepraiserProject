from flask_app import app
from flask_app.controllers.users import users
from flask_app.controllers import movie
# Register the users blueprint
app.register_blueprint(users)

if __name__ == "__main__":
    app.run(debug=True)