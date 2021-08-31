from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)
rest_api = Api(app)

from app import models, api
from app.main import bp as main_bp
from app.errors import bp as errors_bp
from app.models import *


app.register_blueprint(main_bp)
app.register_blueprint(errors_bp)


@app.shell_context_processor
def make_shell_contex():
    return {'db':db,
            'User':User,
            'Fac':Factory,
            'Prod':Product,
            'Cat':Category,
            'Coun':Country,
            'Cur':Currency,
            'Prv':Price_v,
             }
