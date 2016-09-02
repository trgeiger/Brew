from flask import render_template, session, redirect, url_for, current_app, flash, g, request
from flask_login import login_required
from .. import db
from ..models import User, BrewLog
from ..email import send_email
from . import main
from .forms import NameEmailPassForm, BrewLogForm


@main.route('/', methods=['POST', 'GET'])
def index():
    return render_template("front.html", name=session.get('name'))


@main.route('/about')
def about():
    return render_template("about.html")


@main.route('/brewlog', methods=['POST', 'GET'])
@login_required
def brewlog():
    form = BrewLogForm()
    if form.validate_on_submit():
        brewlog = BrewLog(origin=form.origin.data,
                    method=form.method.data,
                    grind=form.grind.data,
                    water=form.water.data,
                    coffee=form.coffee.data,
                    temp=form.temp.data,
                    flavor=form.flavor.data,
                    notes=form.notes.data)
        db.session.add(brewlog)
        db.session.commit()
        flash("Log saved.")
        return redirect(url_for("main.brewlog"))
    brewlogs = BrewLog.query.order_by(BrewLog.timestamp.desc()).all()
    return render_template('brewlog.html', form=form, brewlogs=brewlogs)

@main.route('/abrewlog/<brewlogid>')
@login_required
def abrewlog(brewlogid):
    thebrewlog = BrewLog.query.filter_by(id=brewlogid).first_or_404()
    #brewlog=User.query.filter_by(brewlog_id).first_or_404()
    return render_template('abrewlog.html', thebrewlog=thebrewlog)


@main.route('/welcome', methods=['GET'])
def welcome():
    return render_template("welcome.html")
