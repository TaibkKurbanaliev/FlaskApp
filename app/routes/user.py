from flask import Blueprint, redirect, render_template

from ..functions import save_picture
from ..forms import RegistrationForm
from .. import db, bcrypt
from ..models.user import User

user = Blueprint('user', __name__)

@user.route('/user/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hased_password = bcrypt.generate_password_hash(password=form.password.data).decode('utf-8')
        avatar_file_name = save_picture(form.avatar.data)
        user = User(name=form.name.data, login=form.login.data, avatar=avatar_file_name, password=hased_password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        print("Ошибка регистрации")
    return render_template('user/registry.html', form=form)