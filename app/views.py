__author__ = 'lslacker'
from app import app
from app import login_manager
from app.models import User
from flask.ext.login import login_required, logout_user, login_user
from flask import render_template, redirect


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)




@app.route("/login", methods=["GET", "POST"])
def login():
    return "You need to login first"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
