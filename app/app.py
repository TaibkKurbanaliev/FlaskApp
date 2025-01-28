from flask import Flask
from config import Configuration

from train_list.blueprint import training_list

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(training_list, url_prefix='/test')