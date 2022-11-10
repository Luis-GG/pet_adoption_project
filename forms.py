from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    """Form for adding Pets"""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species")
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = StringField("Age")
    notes = StringField("Notes")
