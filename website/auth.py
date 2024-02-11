from flask import Blueprint, render_template, request, url_for, flash, redirect
from .models import User
from . import db
# from werkzeug import generate_password_hash, check_password_hash 
# used to hash password and check hashed password ^

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "Logged out"

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        # lastname = request.form.get("lastname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if password1 != password2:
            flash("Password dont match.", category="error")
        elif len(password1) < 7:
            flash("Password must be 8 characters.", category="error")
        else:
            new_user = User(email=email, firstName=firstName, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category='success')
            return redirect(url_for("views.home"))
    return render_template("signup.html")