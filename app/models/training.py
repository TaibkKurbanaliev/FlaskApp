from datetime import datetime
from .. import db

class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainingName = db.Column(db.String(100))
    muscleGroups = db.Column(db.String(100))
    numberOfTimes = db.Column(db.Integer)
    numberOfSets = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now())