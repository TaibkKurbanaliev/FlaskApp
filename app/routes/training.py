from flask import Blueprint
from .. import db
from ..models.training import Training

training = Blueprint('training', __name__)

@training.route('/training/<name>')
def create_training(name):
    training = Training(name=name)
    db.session.add(training)
    db.session.commit()
    return "Training Created!"