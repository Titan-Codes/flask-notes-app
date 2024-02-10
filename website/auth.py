from flask import Blueprint, render_template, request, flash

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
        firstname = request.form.get("firstname")
        # lastname = request.form.get("lastname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if password1 != password2:
            flash("Password dont match.", category="error")
        elif len(password1) < 8:
            flash("Password must be 8 characters.", category="error")
    return render_template("signup.html")