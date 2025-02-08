import os


class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload'
    SERVER_PATH = ROOT + UPLOAD_PATH
    
    USER = os.environ.get('POSTGRES_USER', 'user')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'user')
    HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    PORT = os.environ.get('POSTGRES_PORT', '5432')
    DB = os.environ.get('POSTGRES_DB', 'db')
    
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = 'WDQewqsqdwq!@3dwdwq'
    SQLALCHEMY_TRACK_MODIFICATIONS = True