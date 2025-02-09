from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from ..functions import save_picture
from ..forms import LoginForm, RegistrationForm
from .. import db, bcrypt
from ..models.user import User

user = Blueprint('user', __name__)

@user.route('/user/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hased_password = bcrypt.generate_password_hash(password=form.password.data).decode('utf-8')
        avatar_file_name = save_picture(form.avatar.data)
        try:
            user = User(name=form.name.data, login=form.login.data, avatar=avatar_file_name, password=hased_password)
            db.session.add(user)
            db.session.commit()
            flash(f"Регистрация прошла успешно", "success")
            return redirect(url_for('user.login'))
        except Exception as e:
            flash(f"При регистрации произошла ошибка", "danger")
    return render_template('user/registry.html', form=form)

@user.route('/user/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('training.show_all'))
        else:
            flash("Ошибка входа. Проверьте логин или пароль", "danger")
    return render_template('user/login.html', form=form)

@user.route('/user/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('training.show_all'))