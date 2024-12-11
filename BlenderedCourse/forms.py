from flask_wtf import FlaskForm
from wtforms import StringField, EmailField,SubmitFieldfrom wtforms.validators import DataRequired,Email

class RegistrationForm(FlaskForm):
    name = StringField('Имя',validators=[DataRequired()])
    email = EmailField ('Электронная почта', validators=[DataRequired(), Email())]
    submit = SubmitField('Отправить')
    