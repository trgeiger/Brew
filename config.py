#DATABASE=os.path.join(app.root_path, 'brew.db')
import os

basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY='dev key'
USERNAME='admin'
PASSWORD='default'
WTF_CSRF_ENABLED=True
SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN=True

# mail
MAIL_SERVER='smtp.googlemail.com'
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
