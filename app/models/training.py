from datetime import datetime

from ..models.exercise import Exercise
from .. import db

class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    trainings = db.relationship(Exercise, backref='training')
    trainingName = db.Column(db.String(100))
    muscleGroups = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.now())