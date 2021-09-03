import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bigbigsecret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or\
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
    IMAGES_UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'images')
    IMAGES_ALLOWED_EXTENSIONS = {'jpg','jpeg','png','bmp'}

