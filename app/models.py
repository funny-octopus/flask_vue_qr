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


class Factory(db.Model):
    __tablename__ = "factory"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    logo_url = db.Column(db.String(64))
    products = db.relationship('Product', backref='provider', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Factory {self.name}>"


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    image_url = db.Column(db.String(64))
    article = db.Column(db.String(64), index=True)
    factory = db.Column(db.Integer, db.ForeignKey('factory.id'))
    country = db.Column(db.String(64))
    collection = db.Column(db.String(64))
    price = db.Column(db.Integer)
    price_v = db.Column(db.String(24)) # цена за шт. или м2
    price_m = db.Column(db.String(1)) # валюта e,d,r
    percent = db.Column(db.Integer) # процент накрутки
    count = db.Column(db.Integer)

    def __init__(self, name, category, factory, country, collection,\
            price, price_v, price_m, percent, count):
        self.name = name
        self.category = category
        self.factory = factory
        self.country = country
        self.collection = collection
        self.price = price
        self.price_v = price_v
        self.price_m = price_m
        self.percent = percent
        self.count = count

    def set_article(self)->None:
        "Вычисляет и присваивает внутренний артикул товару"
        f = Factory.query.get(self.factory)
        n = 4-len(str(self.id))
        full_id = '0'*n+str(self.id)
        self.article = f"{f.name[0]}{self.collection[0]}{full_id}-{self.category}".lower()
    def __repr__(self):
        return f"<Product {self.name}>"


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    products = db.relationship('Product', backref='cat', lazy='dynamic')

    def __repr__(self):
        return f"<Category {self.name}>"
