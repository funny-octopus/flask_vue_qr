import os
from app import app, db
from app.main import bp
from app.models import User, Product, Factory, Country
from app.main.forms import LoginForm, ChangeImageForm
from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import secure_filename


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('main/index.html')


@bp.route('/item/<ident>', methods=['GET', 'POST'])
def item(ident):
    product = Product.query.get_or_404(ident)
    items = db.session.query(Product, Factory, Country)\
            .filter_by(id=int(ident))\
            .join(Factory)\
            .join(Country)\
            .first()
    if current_user.is_authenticated:
        form = ChangeImageForm()
        if form.validate_on_submit():
            if request.method == "POST":
                upload_file = request.files['filename']
                if upload_file and\
               ('.' in upload_file.filename) and\
               (upload_file.filename.rsplit('.',1)[1].lower() in app.config['IMAGES_ALLOWED_EXTENSIONS']):
                    filename = f"{ident}.{upload_file.filename.rsplit('.',1)[1]}"
                    upload_file.save(os.path.join(app.config['IMAGES_UPLOAD_FOLDER'], filename))
                    product.image_url = filename
                    try:
                        db.session.add(product)
                        db.session.commit()
                    except:
                        db.rollback()
        return render_template('main/managed_item.html', product=items[0], factory=items[1], ident=ident, form=form)
    else:
        return render_template('main/item.html', product=items[0], factory=items[1], country=items[2])


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


@bp.route('/auth/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

