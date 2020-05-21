from flask import render_template, redirect, url_for, flash

from flaskapp import app
from flaskapp.form import RegistrationForm, LoginForm

posts = [
    {"title": "First Post", "author": "Mihir Bindal", "date_posted": "9th May 2020", "content": "Welcome to my blog"},
    {"title": "My first Post", "author": "John Doe", "date_posted": "13th May 2020", "content": "Welcome to my blog"}]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "mihirbindal3@gmail.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login failed", "danger")
    return render_template("login.html", title="Login", form=form)

