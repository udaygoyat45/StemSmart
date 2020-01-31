from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(max=120)])
    confirm_email = PasswordField('Confirm Email',
                             validators=[DataRequired(), EqualTo('Email')])
    submit = SubmitField('Sign Up For Newsletter')