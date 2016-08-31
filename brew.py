import os
import sqlite3
from datetime import datetime
import re
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from forms import NameEmailPassForm

app = Flask(__name__)
app.config.from_object(__name__)

# extensions
bootstrap = Bootstrap(app)
moment = Moment(app)

# Default config and override config from environment variable
app.config.from_object('config')
app.config.from_envvar('BREW_SETTINGS', silent=True)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("front.html", name=session.get('name'))


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/notebook')
def notebook():
    return render_template("notebook.html")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        return signup_func()
    else:
        return render_template("signup.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = NameEmailPassForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return(redirect(url_for('index')))
    return render_template("login.html", form=form)


@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template("welcome.html")


# error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
