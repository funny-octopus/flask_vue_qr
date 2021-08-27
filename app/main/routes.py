from app import app, db
from app.main import bp
from flask import render_template, request, flash


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('main/index.html')


@bp.route('/item/<ident>', methods=['GET'])
def item(ident):
    return ident


@bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    return render_template('main/login.html')

