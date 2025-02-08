from flask import Blueprint, redirect, render_template, request
from .. import db
from ..models.training import Training

training = Blueprint('training', __name__)

@training.route("/", methods=['GET'])
def show_all():
    trainings = Training.query.all()
    return render_template('training/popular.html', trainings=trainings)

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
    
@training.route('/training/<int:id>/update', methods=['POST', 'GET'])
def update(id):
    training = Training.query.get(id)
    if request.method == 'POST':
        training.trainingName = request.form.get('trainingName')
        training.muscleGroups = request.form.get('muscleGroups')
        training.numberOfTimes = request.form.get('numberOfTimes')
        training.numberOfSets = request.form.get('numberOfSets')
        
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))
            
        return redirect('/')
    else:
        return render_template('training/update.html', training=training)
    
@training.route('/training/<int:id>/delete', methods=['GET'])
def delete(id):
    training = Training.query.get(id)
    try:
        db.session.delete(training)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(str(e))
        
    return redirect('/')