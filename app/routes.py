from flask import Blueprint
from app import db
from app.models.user import User

user = Blueprint('user', __name__)

@user.route('/user/<name>')
def create_user(name):
    user = User()
    user.id = 1
    user.name = name
    db.session.add(user)
    db.session.commit()
    return "User Created!"