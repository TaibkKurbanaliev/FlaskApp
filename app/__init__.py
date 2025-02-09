from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.config import Config


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_app=Config):
    app = Flask(__name__)
    
    config = Config()
    
    from .routes.user import user
    app.register_blueprint(user)
    
    from .routes.training import training
    app.register_blueprint(training)
    
    app.config.from_object(config_app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message = 'Вы не можете получить доступ к данной странице'
    login_manager.login_message_category = 'info'
    
    with app.app_context():
        db.create_all()
    
    return app




