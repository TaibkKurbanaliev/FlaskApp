from datetime import datetime
from .. import db

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), default='user')
    avatar = db.Column(db.String(200))
    name = db.Column(db.String(100))
    login = db.Column(db.String(64))
    password = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.now())