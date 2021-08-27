from app import app, db
from app.main import bp
from app.models import User
from app.main.forms import LoginForm
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('main/index.html')


@bp.route('/item/<ident>', methods=['GET'])
def item(ident):
    return ident


@bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return render_template('main/login.html', title="Вход", form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

