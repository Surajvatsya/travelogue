from flask import Flask, render_template, url_for, request, redirect, flash
from flask_login import LoginManager, current_user, logout_user, login_user, UserMixin 
from forms import LoginForm, SignupForm
from app_config import app
from modals import db, City, User

# Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        flash("Already Login")
        return redirect(url_for("index"))

    # Get Data from the html
    if form.validate_on_submit():
        user = User.query.filter_by(email=request.form.get("username")).first()
        
        if not user:
            flash("Invalid Username")
        elif user.verify_password(request.form.get("password")):
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Incorrect Username or Password")

    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # Get all data from html
        username = username=request.form.get("username")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("User Already Exist")
        else:
            new_user = User(username, first_name, last_name, password, email)
            db.session.add(new_user)
            db.session.commit()            
            return redirect(url_for('login'))
    return render_template("signup.html", form=form)

@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Logged out!")
        return redirect(url_for("index"))
    flash("Not Logged In")
    return redirect(url_for("login"))



if __name__ == '__main__':
    app.run(debug=True)