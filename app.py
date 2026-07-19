from flask import Flask
from flask_login import current_user

from config import Config
from extensions import db, login_manager


app = Flask(__name__)

app.config.from_object(Config)


# Database initialization
db.init_app(app)


# Login manager
login_manager.init_app(app)


from models.user import User


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


# Authentication routes
from routes.auth import auth

app.register_blueprint(auth)



from flask_login import current_user

@app.route("/")
def home():

    if current_user.is_authenticated:

        return f"""
        <h1>Welcome, {current_user.username}!</h1>

        <p>You are successfully logged in.</p>

        <br>

        <a href="/logout">Logout</a>
        """

    return """
    <h1>Welcome to PrepWise</h1>

    <a href="/register">Register</a>

    <br><br>

    <a href="/login">Login</a>
    """



with app.app_context():

    db.create_all()



if __name__ == "__main__":

    app.run(debug=True)