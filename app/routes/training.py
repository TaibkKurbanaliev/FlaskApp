from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required
from .. import db
from ..models.training import Training

training = Blueprint('training', __name__)

@training.route("/", methods=['GET'])
def show_all():
    trainings = Training.query.all()
    return render_template('training/popular.html', trainings=trainings)

@training.route('/training/create', methods=['POST','GET'])
@login_required
def create():
    if request.method == 'POST':
        trainingName = request.form.get('trainingName')
        muscleGroups = request.form.get('muscleGroups')
        
        training = Training(user=current_user.id,trainingName=trainingName, muscleGroups=muscleGroups)
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
@login_required
def update(id):
    training = Training.query.get(id)
    if request.method == 'POST':
        training.trainingName = request.form.get('trainingName')
        training.muscleGroups = request.form.get('muscleGroups')
        
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))
            
        return redirect('/')
    else:
        return render_template('training/update.html', training=training)
    
@training.route('/training/<int:id>/delete', methods=['GET'])
@login_required
def delete(id):
    training = Training.query.get(id)
    try:
        db.session.delete(training)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(str(e))
        
    return redirect('/')