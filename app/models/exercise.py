from .. import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    training_id = db.Column(db.Integer, db.ForeignKey('training.id', ondelete='CASCADE'))
    exerciseName = db.Column(db.String(100))
    muscleGroups = db.Column(db.String(100))
    numberOfTimes = db.Column(db.Integer)
    numberOfSets = db.Column(db.Integer)