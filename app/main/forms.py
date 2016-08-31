from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, DataRequired, Email, Optional

# Forms
class NameEmailPassForm(Form):
    name = StringField('Name', validators=[Optional()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
