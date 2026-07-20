from flask import Flask
from flask import Flask, render_template

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
from routes.questions import questions_bp

app.register_blueprint(auth)
app.register_blueprint(questions_bp)



from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")



with app.app_context():

    db.create_all()



if __name__ == "__main__":

    app.run(debug=True)