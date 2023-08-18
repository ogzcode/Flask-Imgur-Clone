import os

upload_folder = os.path.join(os.getcwd(), 'app', 'static', 'image')
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hello world'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = upload_folder
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}