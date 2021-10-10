import os
import math
from datetime import datetime
from app import db
from app.main import bp
from app.models import *
from app.utils import MakeQR, save_images, get_currency
from app.main.forms import LoginForm, ChangeImageForm, AddProductForm, ChangeCurrency, ChangePasswordForm
from flask import render_template, request, flash, redirect, url_for, abort, send_file, current_app
from flask_login import current_user, login_user, logout_user, login_required


@bp.route('/item/<ident>', methods=['GET', 'POST'])
def item(ident):
    product = Product.query.get_or_404(ident)
    course = Ruble_course.query.order_by(Ruble_course.id.desc()).first()
    cur = Currency.query.filter_by(id=product.price_m).first()
    if cur.name.lower() == 'доллар':
        k = course.dollar
    elif cur.name.lower() == 'евро':
        k = course.euro
    else:
        k = '1'
    k = k.replace(',', '.')
    price = (float(product.price)*float(k))*((float(product.percent)/100)+1.0)
    price = math.ceil(price)
    items = db.session.query(Product, Country)\
            .filter_by(id=int(ident))\
            .join(Country)\
            .first()
    if current_user.is_authenticated:
        form = ChangeImageForm()
        if form.validate_on_submit():
            if request.method == "POST":
                upload_file = request.files['filename']
                if upload_file and\
               ('.' in upload_file.filename) and\
               (upload_file.filename.rsplit('.',1)[1].lower() in current_app.config['IMAGES_ALLOWED_EXTENSIONS']):
                    filename = f"{ident}.{upload_file.filename.rsplit('.',1)[1]}"
                    upload_file.save(os.path.join(current_app.config['IMAGES_UPLOAD_FOLDER'], filename))
                    save_images(os.path.join(current_app.config['IMAGES_UPLOAD_FOLDER'], filename))
                    product.image_url = 'big_' + filename
                    product.sm_image_url = 'sm_' + filename
                    try:
                        db.session.add(product)
                        db.session.commit()
                    except:
                        db.rollback()
        return render_template('main/managed_item.html', product=items[0], ident=ident, form=form)
    else:
        return render_template('main/item.html', product=items[0], country=items[1], price=price)


@bp.route('/add/', methods=['GET', 'POST'])
@login_required
def add_product():
    form = AddProductForm()
    cats = Category.query.all()
    cos = Country.query.all()
    prvs = Price_v.query.all()
    curs = Currency.query.all()
    form.category.choices = [('','')]+[(x.id,x.name) for x in cats]
    form.country.choices = [('','')]+[(x.id,x.name) for x in cos]
    form.price_v.choices = [('','')]+[(x.id,x.name) for x in prvs]
    form.currency.choices = [('','')]+[(x.id,x.name) for x in curs]
    if request.method == 'POST' and form.validate_on_submit():
        resp = request.form
        prod = Product(resp['name'],\
                resp['category'],\
                resp['factory'],\
                resp['country'],\
                resp['collection'],\
                resp['size'],\
                resp['price'].replace(',','.').replace(' ','').strip(),\
                resp['price_v'],\
                resp['currency'],\
                resp['percent'].replace(',','.').replace(' ','').strip(),\
                resp['count'])
        try:
            db.session.add(prod)
            db.session.commit()
        except Exception as e:
            print(str(e))
            db.session.rollback()
            abort(500)
        prod.set_article()
        upload_file = request.files['image_url']
        if upload_file and\
       ('.' in upload_file.filename) and\
       (upload_file.filename.rsplit('.',1)[1].lower() in current_app.config['IMAGES_ALLOWED_EXTENSIONS']):
            filename = f"{prod.id}.{upload_file.filename.rsplit('.',1)[1]}"
            upload_file.save(os.path.join(current_app.config['IMAGES_UPLOAD_FOLDER'], filename))
            save_images(os.path.join(current_app.config['IMAGES_UPLOAD_FOLDER'], filename))
            prod.image_url = 'big_' + filename
            prod.sm_image_url = 'sm_' + filename
        try:
            db.session.add(prod)
            db.session.commit()
        except Exception as e:
            print(str(e))
            db.session.rollback()
            abort(500)

        return redirect(url_for('main.add_product'))
    return render_template('main/add.html', title="Добавить товар", form=form)


@bp.route('/', methods=['GET',])
@bp.route('/index', methods=['GET',])
@bp.route('/catalog', methods=['GET',])
@login_required
def catalog():
    return render_template('main/catalog.html')


@bp.route('/course', methods=['GET', 'POST'])
@bp.route('/course/<r>', methods=['GET','POST'])
@login_required
def course(r=None):
    if r:
        dollar, euro = get_currency()
        c = Ruble_course(dollar, euro, datetime.now())
        try:
            db.session.add(c)
            db.session.commit()
            return redirect('/course')
        except Exception as e:
            db.session.rollback()
            # flash('Ошибка при добавлении в базу')
    form = ChangeCurrency()
    if request.method == 'POST' and form.validate_on_submit():
        c = Ruble_course(form.dollar.data, form.euro.data, datetime.now())
        try:
            db.session.add(c)
            db.session.commit()
            return redireect('/course')
        except Exception as e:
            db.session.rollback()
            # flash('Ошибка при добавлении в базу')
    course = Ruble_course.query.order_by(Ruble_course.id.desc()).first()
    return render_template('main/course.html', course=course, form=form)

@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template('main/edit.html')


@bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.catalog'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильное имя пользователя или пароль')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.catalog'))
    return render_template('main/login.html', title="Вход", form=form)


@bp.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@bp.route('/qr/<ident>', methods=['GET',])
@login_required
def qr(ident):
    # filename = MakeQR(f"http://127.0.0.1:5000/item/{ident}")
    filename = MakeQR(f"https://{current_app.config['DOMAIN']}/item/{ident}")
    return send_file(filename, as_attachment=True, download_name=f"{ident}.png")


@bp.route('/password', methods=['GET','POST'])
@login_required
def password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.password.data)
        db.session.commit()
        flash("Пароль успешно изменен!")
    return render_template('main/password.html', title="Изменение пароля", form=form)

