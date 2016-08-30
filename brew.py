import os
import sqlite3
import re
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash

app = Flask(__name__)
app.config.from_object(__name__)

# Default config and override config from environment variable
app.config.from_object('config')
app.config.from_envvar('BREW_SETTINGS', silent=True)

# helper functions
def signup_func():
    # look inside the request to figure out what the user typed
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    # regular expressions for user input verification
    username_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    password_re = re.compile(r"^.{3,20}$")
    email_re = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    def valid_input(userin, regexp):
        return regexp.match(userin)

    # if the user typed invalid username, give error
    if not valid_input(username, username_re):
        uerror = "Invalid username"
    else:
        uerror = ""

    # if the user typed invalid password, give error
    if not valid_input(password, password_re):
        perror = "Invalid password"
    else:
        perror = ""

    # check if password matches verify
    if password != verify:
        verror = "Please reconfirm your password"
    else:
        verror = ""

    #if user typed invalid email address, give error
    if (email != "") and (not valid_input(email, email_re)):
        eerror = "Invalid email address"
    else:
        eerror = ""

    # if any of the above errors are triggered, preserve user input and clear password, display error messages
    if not (valid_input(username, username_re) and valid_input(password, password_re) and (password == verify)):
        return(render_template("signup.html", uerror=uerror, perror=perror, verror=verror, eerror=eerror, username=username, email=email))
    else:
        return(signup_welcome(username))

def signup_welcome(username):
    return(render_template("front.html", username=username))

@app.route('/', methods=['POST', 'GET'])
def index():
    return(render_template("front.html"))

@app.route('/about')
def about():
    return(render_template("about.html"))

@app.route('/notebook')
def notebook():
    return(render_template("notebook.html"))

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        return(signup_func())
    else:
        return(render_template("signup.html"))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return(login_func())
    else:
        return(render_template("login.html"))

@app.route('/welcome', methods=['GET'])
def welcome():
    return(render_template("welcome.html"))

# error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
