from app import db, rest_api
from app.models import *
from flask_restful import Resource


class Prod(Resource):
    def get(self, product_id):
        prod = db.session.query(Product, Factory, Category, Country,\
                                Currency, Price_v)\
                .filter_by(id=int(product_id))\
                .join(Factory)\
                .join(Category)\
                .join(Country)\
                .join(Currency)\
                .join(Price_v)\
                .first()
        p,f,ca,co,cu,pr  = prod
        return {'status':'ok',
                'id':p.id,
                'product':{
                    'name':{'title':'Название','value':p.name},
                    'category':{'title':'Категория','value':ca.name},
                    'article':{'title':'Артикул','value':p.article},
                    'factory':{'title':'Фабрика','value':f.name},
                    'country':{'title':'Страна','value':co.name},
                    'collection':{'title':'Коллекция','value':p.collection},
                    'price':{'title':'Цена','value':p.price},
                    'price_v':{'title':'Ед.изм','value':pr.name},
                    'currency':{'title':'Ден.ед.','value':cu.name},
                    'percent':{'title':'Процент','value':p.percent},
                    'count':{'title':'Количество в упаковке','value':p.count}}}
    def post(self, product_id):
        return {'status':'ok', 'method':'post'}

rest_api.add_resource(Prod, '/api/item/<int:product_id>')

class Factories(Resource):
    def get(self):
        f = Factory.query.all()
        fs = [x.name for x in f]
        return {'items':fs}

rest_api.add_resource(Factories, '/api/factories')


class Categories(Resource):
    def get(self):
        c = Category.query.all()
        cs = [x.name for x in c]
        return {'items':cs}

rest_api.add_resource(Categories, '/api/categories')


class Items(Resource):
    def get(self):
        cats = Category.query.all()
        facs = Factory.query.all()
        cou = Country.query.all()
        cur = Currency.query.all()
        pr = Price_v.query.all()
        c = {'category':[x.name for x in cats],
             'factory':[x.name for x in facs],
             'country':[x.name for x in cou],
             'currency':[x.name for x in cur],
             'price_v':[x.name for x in pr],}
        return {'status':'ok', 'items':c}

rest_api.add_resource(Items, '/api/items')
