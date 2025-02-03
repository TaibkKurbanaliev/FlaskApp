from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app(config_app=Config):
    app = Flask(__name__)
    
    config = Config()
    app.register_blueprint(user)
    app.config.from_object(config_app)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    
    return app

from app.routes import user