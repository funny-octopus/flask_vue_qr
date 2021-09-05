from app import db, rest_api
from app.models import *
from flask_restful import Resource
from flask import request


class Prod(Resource):
    def get(self, product_id):
        prod = db.session.query(Product, Factory, Category, Country,\
                                Currency, Price_v, Collection)\
                .filter_by(id=int(product_id))\
                .join(Factory, Factory.id == Product.factory)\
                .join(Category)\
                .join(Country)\
                .join(Currency)\
                .join(Price_v)\
                .join(Collection, Collection.id == Product.collection)\
                .first()
        p,f,ca,co,cu,pr,col  = prod
        return {'status':'ok',
                'id':p.id,
                'product':{
                    'name':{'title':'Название','value':p.name},
                    'category':{'title':'Категория','value':ca.name, 'id':ca.id},
                    'article':{'title':'Артикул','value':p.article},
                    'factory':{'title':'Фабрика','value':f.name, 'id':f.id},
                    'country':{'title':'Страна','value':co.name, 'id':co.id},
                    'collection':{'title':'Коллекция','value':col.name, 'id':col.id},
                    'price':{'title':'Цена','value':p.price},
                    'price_v':{'title':'Ед.изм','value':pr.name, 'id':pr.id},
                    'currency':{'title':'Ден.ед.','value':cu.name,'id':cu.id},
                    'percent':{'title':'Процент','value':p.percent},
                    'count':{'title':'Количество в упаковке','value':p.count}}}

    def post(self, product_id):
        resp = request.get_json()
        cat_id = Category.query.filter_by(name=resp['category']['value']).first()
        country_id = Country.query.filter_by(name=resp['country']['value']).first()
        factory_id = Factory.query.filter_by(name=resp['factory']['value']).first()
        pricev_id = Price_v.query.filter_by(name=resp['price_v']['value']).first()
        cur_id = Currency.query.filter_by(name=resp['currency']['value']).first()
        col_id = Collection.query.filter_by(name=resp['collection']['value']).first()
        prod = Product.query.get(int(product_id))
        prod.name = resp['name']['value']
        prod.category = cat_id.id
        prod.factory = factory_id.id
        prod.country = country_id.id
        prod.collection = col_id.id
        prod.price = resp['price']['value']
        prod.price_v = pricev_id.id
        prod.price_m = cur_id.id
        prod.percent = resp['percent']['value']
        prod.count = resp['count']['value']
        prod.set_article()
        print(prod.__dict__)
        try:
            db.session.add(prod)
            db.session.commit()
            return {'status':'ok','article':prod.article}
        except Exception as e:
            print(str(e))
            db.session.rollback()
            return {'status':'error',}


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


class Collections(Resource):
    def get(self, factory_id):
        factory = Factory.query.get(factory_id)
        collections = factory.collections
        print(collections)
        return {'items':cs}

rest_api.add_resource(Collections, '/api/collections/<int:factory_id>')


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
             'price_v':[x.name for x in pr],
             }
        return {'status':'ok', 'items':c}

rest_api.add_resource(Items, '/api/items')
