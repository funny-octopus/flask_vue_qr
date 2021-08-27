from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.name}>"


class Organization(db.Model):
    __tablename__ = "organization"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    logo_url = db.Column(db.String(64))
    products = db.relationship('Product', backref='provider', lazy='dynamic')

    def __repr__(self):
        return f"<Org {self.name}>"


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    image_url = db.Column(db.String(64))
    desc = db.Column(db.Text)
    prov = db.Column(db.Integer, db.ForeignKey('organization.id'))

    def __repr__(self):
        return f"<Product {self.name}>"

