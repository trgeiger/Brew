from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import Required, DataRequired, Email, Optional

# Forms
class NameEmailPassForm(Form):
    name = StringField('Name', validators=[Optional()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField('Login')

class BrewLogForm(Form):
    origin = StringField("Coffee Origin")
    method = StringField("Brew Method")
    grind = StringField("Grind")
    water = IntegerField("Water in grams")
    coffee = IntegerField("Coffee in grams")
    temp = IntegerField("Water Temperature")
    flavor = TextAreaField("Tasting Notes")
    notes = TextAreaField("Other Notes")
    submit = SubmitField('Save')
