from flask import Blueprint, redirect, render_template, request
from .. import db
from ..models.training import Training

training = Blueprint('training', __name__)

@training.route('/training/create', methods=['POST','GET'])
def create():
    if request.method == 'POST':
        trainingName = request.form.get('trainingName')
        muscleGroups = request.form.get('muscleGroups')
        numberOfTimes = request.form.get('numberOfTimes')
        numberOfSets = request.form.get('numberOfSets')
        training = Training(trainingName=trainingName, muscleGroups=muscleGroups, numberOfTimes=numberOfTimes, numberOfSets=numberOfSets)
        try:
            db.session.add(training)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))
        return redirect('/')
    else:
        return render_template('training/create.html')