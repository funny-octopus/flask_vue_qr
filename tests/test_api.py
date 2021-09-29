import os
import sys
import unittest
from datetime import datetime
from ..app import create_app, db
from ..config import TestConfig
from .models import Product, Country, Category, Currency, Price_v, Ruble_course

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI']='sqlite://'
        db.create_all()
        cou1 = Country(name='England')
        cou2 = Country(name='Russia')
        cou3 = Country(name='USA')
        db.session.add_all([cou1, cou2, cou3])
        prv1 = Price_v(name='m3')
        prv2 = Price_v(name='sht')
        db.session.add_all([prv1, prv2])
        cur1 = Currency(name='Rub')
        cur2 = Currency(name='Dol')
        cur3 = Currency(name='Eur')
        db.session.add_all([cur1, cur2])
        cat1 = Category(name='plitka')
        cat2 = Category(name='svet')
        cat3 = Category(name='pol')
        cat4 = Category(name='tkan')
        db.session.add_all([cat1, cat2, cat3, cat4])
        rub = Ruble_course(dollar='70', euro='80', date=datetime.now())
        db.session.add(rub)
        db.session.commit()
        prod1 = Product('prod1',cat1.id,'fac1',cou1.id,'col1','32x32','12',prv1.id, cur1.id, '12', '12')
        db.session.add(prod1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()



class ProductTestCase(BaseTestCase):
    def test_set_article(self):
        pass

