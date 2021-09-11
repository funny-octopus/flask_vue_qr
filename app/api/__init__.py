from app import db, rest_api
from app.models import *
from flask_restful import Resource
from flask import request


class Item(Resource):
    def get(self, product_id):
        # prod = db.session.query(Product, Factory, Category, Country,\
        #                         Currency, Price_v, Collection)\
                # .join(Factory, Factory.id == Product.factory)\
                # .join(Collection, Collection.id == Product.collection)\
        prod = db.session.query(Product, Category, Country, Currency, Price_v)\
                .filter_by(id=int(product_id))\
                .join(Category)\
                .join(Country)\
                .join(Currency)\
                .join(Price_v)\
                .first()
        # p,f,ca,co,cu,pr,col  = prod
        p,ca,co,cu,pr  = prod
        return {'status':'ok',
                'id':p.id,
                'product':{
                    'category':{'title':'Категория','value':ca.name, 'id':ca.id},
                    'article':{'title':'Артикул','value':p.article},
                    # 'factory':{'title':'Фабрика','value':f.name, 'id':f.id},
                    'factory':{'title':'Фабрика','value':p.factory},
                    'country':{'title':'Страна','value':co.name, 'id':co.id},
                    # 'collection':{'title':'Коллекция','value':col.name, 'id':col.id},
                    'collection':{'title':'Коллекция','value':p.collection},
                    'name':{'title':'Название','value':p.name},
                    'price':{'title':'Цена','value':p.price},
                    'price_v':{'title':'Ед.изм','value':pr.name, 'id':pr.id},
                    'currency':{'title':'Ден.ед.','value':cu.name,'id':cu.id},
                    'percent':{'title':'Наценка(%)','value':p.percent},
                    'count':{'title':'Количество в упаковке','value':p.count}}}

    def post(self, product_id):
        resp = request.get_json()
        cat_id = Category.query.filter_by(name=resp['category']['value']).first()
        country_id = Country.query.filter_by(name=resp['country']['value']).first()
        # factory_id = Factory.query.filter_by(name=resp['factory']['value']).first()
        pricev_id = Price_v.query.filter_by(name=resp['price_v']['value']).first()
        cur_id = Currency.query.filter_by(name=resp['currency']['value']).first()
        # col_id = Collection.query.filter_by(name=resp['collection']['value']).first()
        prod = Product.query.get(int(product_id))
        prod.name = resp['name']['value']
        prod.category = cat_id.id
        # prod.factory = factory.id
        prod.factory = resp['factory']['value']
        prod.country = country_id.id
        # prod.collection = colection.id
        prod.collection = resp['collection']['value']
        prod.price = resp['price']['value']
        prod.price_v = pricev_id.id
        prod.price_m = cur_id.id
        prod.percent = resp['percent']['value']
        prod.count = resp['count']['value']
        prod.set_article()
        try:
            db.session.add(prod)
            db.session.commit()
            return {'status':'ok','article':prod.article}
        except Exception as e:
            db.session.rollback()
            return {'status':'error',}

rest_api.add_resource(Item, '/api/item/<int:product_id>')


# class Factories(Resource):
#     def get(self):
#         f = Factory.query.all()
#         fs = [{'id':x.id, 'name':x.name} for x in f]
#         return {'status':'ok', 'items':fs}
# 
# rest_api.add_resource(Factories, '/api/factories')


class Categories(Resource):
    def get(self):
        c = Category.query.all()
        cs = [{'id':x.id, 'name':x.name} for x in c]
        return {'status':'ok', 'items':cs}

rest_api.add_resource(Categories, '/api/category/')


# class Collections(Resource):
#     def get(self, factory_id):
#         factory = Factory.query.get(factory_id)
#         collections = factory.collections.all()
#         return {'status':'ok','items':[{'id':x.id, 'name':x.name} for x in collections]}
# 
# rest_api.add_resource(Collections, '/api/collections/<int:factory_id>')


class Products(Resource):
    def get(self, category_id):
        category = Category.query.get(category_id)
        products = category.products.all()
        return {'status':'ok','items':[{'id':x.id, 'name':x.name, 'image_url':x.image_url} for x in products]}

rest_api.add_resource(Products, '/api/products/<int:category_id>')


class Countries(Resource):
    def get(self):
        countries = Country.query.all()
        return {'status':'ok','items':[{'id':x.id, 'name':x.name} for x in countries]}

rest_api.add_resource(Countries, '/api/countries/')


class Items(Resource):
    def get(self):
        cats = Category.query.all()
        # facs = Factory.query.all()
        cou = Country.query.all()
        cur = Currency.query.all()
        pr = Price_v.query.all()
        c = {'category':[x.name for x in cats],
             # 'factory':[x.name for x in facs],
             'country':[x.name for x in cou],
             'currency':[x.name for x in cur],
             'price_v':[x.name for x in pr],
             }
        return {'status':'ok', 'items':c}

rest_api.add_resource(Items, '/api/items')

