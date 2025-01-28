from flask import Blueprint
from flask import render_template

training_list = Blueprint('training_list', __name__, template_folder='templates')

@training_list.route('/')
def index():
    return render_template('train_list/index.html')