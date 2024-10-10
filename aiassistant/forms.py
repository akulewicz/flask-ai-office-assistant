from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SubmitField, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Email, Length
from aiassistant.models import User

class CorrectorForm(FlaskForm):
    text = TextAreaField('Tekst do korekty', validators=[DataRequired(message='Musisz podać tekst')])
    simplify = BooleanField('Uprość tekst')
    submit = SubmitField('Popraw')

class AltGeneratorForm(FlaskForm):
    image_url = StringField('Link do obrazka', validators=[DataRequired(message='Podaj link do obrazka')])
    submit = SubmitField('Generuj')
    
class RegistrationForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(message='Podaj nazwę użytkownika')])
    email = StringField('E-mail', validators=[DataRequired(message='Podaj prawidłowy adres e-mail'), Email(message='Podaj prawidłowy e-mail')])
    password = PasswordField('Hasło', validators=[DataRequired(message='Hasło musi składać się z min. 8 znaków')])
    confirm_password = PasswordField('Powtórz hasło', validators=[DataRequired('Pole jest wymagane'), EqualTo('password', message='Hasła muszą być identyczn')])
    submit = SubmitField('Zarejestruj')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Ten e-mail jest już zarejestrowany')
        
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Ta nazwa użytkownika jest już używana')

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(message='Podaj prawidłowy adres e-mail'), Email(message='Podaj prawidłowy e-mail')])
    password = PasswordField('Hasło', validators=[DataRequired(message='Hasło musi składać się z min. 8 znaków'), Length(min=8)])
    remember = BooleanField('Zapamiętaj mnie')
    submit = SubmitField('Zaloguj')