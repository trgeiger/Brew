from flask import render_template, session, redirect, url_for, current_app, flash, g, request
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameEmailPassForm


@main.route('/', methods=['POST', 'GET'])
def index():
    return render_template("front.html", name=session.get('name'))


@main.route('/about')
def about():
    return render_template("about.html")


@main.route('/notebook')
def notebook():
    return render_template("notebook.html")


@main.route('/signup', methods=['POST', 'GET'])
def signup():
        return render_template("signup.html")


@main.route('/login', methods=['POST', 'GET'])
def login():
    form = NameEmailPassForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return(redirect(url_for('.index')))
    return render_template("login.html", form=form)


@main.route('/welcome', methods=['GET'])
def welcome():
    return render_template("welcome.html")
