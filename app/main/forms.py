from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, DataRequired, Email, Optional

# Forms
class NameEmailPassForm(Form):
    name = StringField('Name', validators=[Optional()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField('Login')
