from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, IntegerField, SelectField, BooleanField, DecimalField
from wtforms.validators import Required, DataRequired, Email, Optional


class BrewLogForm(Form):
    origin = StringField("Coffee Origin", render_kw={"placeholder": "e.g. Kenya"})
    method = SelectField("Brew Method", choices=[('Drip', 'Drip'), ('Chemex', 'Chemex'), ('Hario V60', 'Hario V60'), ('Aeropress', 'Aeropress'), ('French Press', 'French Press'), ('Moka Pot', 'Moka Pot'), ('Vacuum Pot', 'Vacuum Pot')])
    grind = StringField("Grind", render_kw={"placeholder": "e.g. 17 on home grinder"})
    water = IntegerField("Water in grams", render_kw={"placeholder": "e.g. 500"})
    coffee = IntegerField("Coffee in grams", render_kw={"placeholder": "e.g. 17"})
    temp = IntegerField("Water Temperature", render_kw={"placeholder": "e.g. 190"})
    flavor = TextAreaField("Tasting Notes", render_kw={"placeholder": "e.g. Fruity, acidic, floral ending notes"})
    notes = TextAreaField("Other Notes", render_kw={"placeholder": "e.g. Try lower temperature next brew, longer bloom"})
    rating = SelectField("Rating", choices=[('None', 'None'), ('1', '1: gross'), ('2', '2: bad'), ('3', '3: fine'), ('4', '4: good'), ('5', '5: great')])
    submit = SubmitField('Save')
