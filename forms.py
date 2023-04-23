from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, Length, NumberRange

class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Name required")])
    species = SelectField("Species", choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine', 'Porcupine')])    
    photo_url = StringField("Image URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    avilable = BooleanField("Available")

class EditPetForm(FlaskForm):    
    photo_url = StringField("Image URL", validators=[Optional(), URL()])    
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    avilable = BooleanField("Available")
    
