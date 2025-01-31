from flask import Flask
from app.config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_script import Manager

from train_list.blueprint import training_list

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

app.register_blueprint(training_list, url_prefix='/test')
migrate = Migrate(app, db)
manager = Manager(app)