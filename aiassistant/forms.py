from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CorrectorForm(FlaskForm):
    text = TextAreaField('Tekst do korekty', validators=[DataRequired(message='Musisz podać tekst')])
    simplify = BooleanField('Uprość tekst')
    submit = SubmitField('Popraw')