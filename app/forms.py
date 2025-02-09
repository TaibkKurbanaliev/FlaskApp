from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField, PasswordField, StringField, SubmitField, ValidationError
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo

from .models.user import User

class RegistrationForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(),Length(min=2, max=100)])
    login = StringField('Логин', validators=[DataRequired(),Length(min=2, max=64)])
    password = PasswordField('Пароль', validators=[DataRequired(),Length(min=2, max=64)])
    confirm_password = PasswordField('Подтвердить пароль', validators=[DataRequired(),Length(min=2, max=64), EqualTo('password')])
    avatar = FileField('Загрузите фото', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Зарегистрироваться')
    
    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Данный логин пользователя уже занят')
        
class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(),Length(min=2, max=64)])
    password = PasswordField('Пароль', validators=[DataRequired(),Length(min=2, max=64)])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')