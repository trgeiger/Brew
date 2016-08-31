import os
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from forms import NameEmailPassForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.from_object(__name__)

# Default config and override config from environment variable
app.config.from_object('config')
app.config.from_envvar('BREW_SETTINGS', silent=True)

# extensions
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)


# database tables
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

# debug shell context
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


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
    #app.run(debug=True)
    manager.run()
