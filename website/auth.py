from flask import Blueprint, render_template, request, url_for, flash, redirect
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
# from werkzeug import generate_password_hash, check_password_hash 
# used to hash password and check hashed password ^

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")
            # return redirect(url_for("views.signup"))
    # return redirect(url_for("views.home"))
    return render_template("login.html", boolean=True)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        # lastname = request.form.get("lastname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category="error")
        elif password1 != password2:
            flash("Password dont match.", category="error")
        elif len(password1) < 7:
            flash("Password must be 8 characters.", category="error")
        else:
            new_user = User(email=email, firstName=firstName, password=password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created!", category='success')
            return redirect(url_for("views.home"))
    return render_template("signup.html")