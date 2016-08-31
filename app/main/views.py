from flask import render_template, session, redirect, url_for, current_app, flash, g, request
from flask_login import login_required
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
@login_required
def notebook():
    return render_template("notebook.html")


@main.route('/welcome', methods=['GET'])
def welcome():
    return render_template("welcome.html")
