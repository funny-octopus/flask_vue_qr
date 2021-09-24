from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, name):
        self.name = name

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.name}>"


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    image_url = db.Column(db.String(64))
    sm_image_url = db.Column(db.String(64))
    article = db.Column(db.String(64), index=True)
    factory = db.Column(db.String(128))
    country = db.Column(db.Integer, db.ForeignKey('country.id'))
    collection = db.Column(db.String(128))
    size = db.Column(db.String(64))
    price = db.Column(db.String(16))
    price_v = db.Column(db.Integer, db.ForeignKey('price_v.id'))
    price_m = db.Column(db.Integer, db.ForeignKey('currency.id'))
    percent = db.Column(db.String(16)) # процент накрутки
    count = db.Column(db.String(16))

    def __init__(self, name, category, factory, country, collection,\
            size ,price, price_v, price_m, percent, count,\
            image_url='big_default.png', sm_image_url='sm_default.png'):
        self.name = name
        self.category = category
        self.factory = factory
        self.country = country
        self.collection = collection
        self.size = size
        self.price = price
        self.price_v = price_v
        self.price_m = price_m
        self.percent = percent
        self.count = count
        self.image_url = image_url
        self.sm_image_url = sm_image_url

    def set_article(self)->None:
        "Вычисляет и присваивает внутренний артикул товару"
        f = self.factory
        c = self.collection
        n = 4-len(str(self.id))
        full_id = '0'*n+str(self.id)
        self.article = f"{f[0]}{c[0]}{full_id}-{self.category}".lower()

    def __repr__(self):
        return f"<Product {self.name}>"


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    products = db.relationship('Product', backref='cat', lazy='dynamic')

    def __repr__(self):
        return f"<Category {self.name}>"


class Country(db.Model):
    __tablename__ = "country"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return f"<Country {self.name}>"


class Currency(db.Model):
    __tablename__ = "currency"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return f"<Currency {self.name}>"

class Price_v(db.Model):
    __tablename__ = "price_v"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return f"<Price_v {self.name}>"


class Ruble_course(db.Model):
    __tablename__ = "ruble_course"
    id = db.Column(db.Integer, primary_key=True)
    dollar = db.Column(db.String(16))
    euro = db.Column(db.String(16))
    date = db.Column(db.DateTime(timezone=True))

    def __init__(self, dollar, euro, date):
        self.dollar = dollar
        self.euro = euro
        self.date = date

