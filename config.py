import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    load_dotenv()
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bigbigsecret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or\
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
    IMAGES_UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'images')
    IMAGES_ALLOWED_EXTENSIONS = {'jpg','jpeg','png','bmp'}
    DOMAIN = os.environ.get('DOMAIN') or 'http://127.0.0.1:5000'

