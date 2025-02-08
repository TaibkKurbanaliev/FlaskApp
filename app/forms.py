from flask_wtf import FlaskForm
from wtforms import FileField, PasswordField, StringField, SubmitField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(),Length(min=2, max=100)])
    login = StringField('Логин', validators=[DataRequired(),Length(min=2, max=64)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердить пароль', validators=[DataRequired(), EqualTo('password')])
    avatar = FileField('Загрузите фото', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Зарегистрироваться')