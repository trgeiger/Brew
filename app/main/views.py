from flask import render_template, session, redirect, url_for, current_app, flash, g, request
from flask_login import login_required, current_user
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
    form.origin(placeholder="e.g. Kenya")
    if form.validate_on_submit():
        brewlog = BrewLog(origin=form.origin.data,
                    method=form.method.data,
                    grind=form.grind.data,
                    water=form.water.data,
                    coffee=form.coffee.data,
                    temp=form.temp.data,
                    flavor=form.flavor.data,
                    notes=form.notes.data,
                    author=current_user._get_current_object(),
                    rating=form.rating.data)
        db.session.add(brewlog)
        db.session.commit()
        flash("Log saved.")
        return redirect(url_for("main.brewlog"))
    brewlogs = BrewLog.query.filter_by(author_id=current_user.id).order_by(BrewLog.timestamp.desc()).limit(5)
    return render_template('brewlog.html', form=form, brewlogs=brewlogs)

@main.route('/abrewlog/<brewlogid>', methods=['POST', 'GET'])
@login_required
def abrewlog(brewlogid):
    thebrewlog = BrewLog.query.filter_by(id=brewlogid).first_or_404()
    if request.method == 'POST':
        db.session.delete(thebrewlog)
        db.session.commit()
        flash("Log Deleted.")
        return redirect(url_for("main.loglist"))
    return render_template('abrewlog.html', thebrewlog=thebrewlog)

@main.route('/loglist')
@login_required
def loglist():
    brewlogs = BrewLog.query.filter_by(author_id=current_user.id).order_by(BrewLog.timestamp.desc()).all()
    return render_template('loglist.html', brewlogs=brewlogs)


@main.route('/welcome', methods=['GET'])
def welcome():
    return render_template("welcome.html")
