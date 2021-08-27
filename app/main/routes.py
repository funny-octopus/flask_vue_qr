from app import app, db
from app.main import bp
from flask import render_template, request, flash


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('main/index.html')


@bp.route('/item/<ident>')
def item(ident):
    return ident

