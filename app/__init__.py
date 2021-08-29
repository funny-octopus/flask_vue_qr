from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)

from app import models
from app.main import bp as main_bp
from app.errors import bp as errors_bp
# from app.api import bp as api_bp
from app.models import User, Factory, Product, Category

app.register_blueprint(main_bp)
app.register_blueprint(errors_bp)
# app.register_blueprint(api_bp, prefix="/api")


@app.shell_context_processor
def make_shell_contex():
    return {'db':db,
            'User':User,
            'Fac':Factory,
            'Prod':Product,
            'Cat':Category,
             }
