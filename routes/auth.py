from flask import Blueprint, render_template, redirect, url_for, request, flash

from extensions import db
from models.user import User

from flask_login import login_user, logout_user


auth = Blueprint(
    "auth",
    __name__
)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]


        existing_user = User.query.filter_by(
            email=email
        ).first()


        if existing_user:
            flash("Email already registered")
            return redirect(
                url_for("auth.register")
            )


        user = User(
            username=username,
            email=email
        )


        user.set_password(password)


        db.session.add(user)
        db.session.commit()


        flash("Account created successfully")

        return redirect(
            url_for("auth.login")
        )


    return render_template(
        "register.html"
    )



@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]


        user = User.query.filter_by(
            email=email
        ).first()


        if user and user.check_password(password):

            login_user(user)

            return redirect("/")


        else:

            flash(
                "Invalid email or password"
            )


    return render_template(
        "login.html"
    )



@auth.route("/logout")
def logout():

    logout_user()

    return redirect(
        url_for("auth.login")
    )