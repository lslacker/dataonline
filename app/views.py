__author__ = 'lslacker'
from app import app
from app import login_manager
from app.models import User
from app.forms import LoginForm
from flask.ext.login import login_required, logout_user, login_user, current_user
from flask import render_template, request, flash, redirect, url_for


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
@login_required
def index():
    print current_user
    return render_template("index.html", title='Home')


@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated():
        return redirect(url_for("index"))

    form = LoginForm()
    print dir(form.username)
    if request.method == 'POST':

        if form.validate_on_submit():
            if login_user(form.user, remember=form.remember_me.data):
                return redirect(request.args.get("next") or url_for("index"))
            else:
                flash("Sorry, but you could not log in.")

    return render_template('login.html', title='Login', form=form)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
