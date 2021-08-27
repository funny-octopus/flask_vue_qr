from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app.main import bp as main_bp
# from app.api import bp as api_bp

app.register_blueprint(main_bp)
# app.register_blueprint(api_bp, prefix="/api")


@app.shell_context_processor
def make_shell_contex():
    return {'db':db,
             }
