from app import db, rest_api
from app.models import *
from flask_restful import Resource
from flask import request


class Item(Resource):
    def get(self, product_id):
        prod = db.session.query(Product, Category, Country, Currency, Price_v)\
                .filter_by(id=int(product_id))\
                .join(Category)\
                .join(Country)\
                .join(Currency)\
                .join(Price_v)\
                .first()
        p,ca,co,cu,pr  = prod
        return {'status':'ok',
                'id':p.id,
                'product':{
                    'category':{'title':'Категория','value':ca.name, 'id':ca.id},
                    'article':{'title':'Артикул','value':p.article},
                    'factory':{'title':'Фабрика','value':p.factory},
                    'country':{'title':'Страна','value':co.name, 'id':co.id},
                    'collection':{'title':'Коллекция','value':p.collection},
                    'name':{'title':'Название','value':p.name},
                    'price':{'title':'Цена','value':p.price},
                    'currency':{'title':'Ден.ед.','value':cu.name,'id':cu.id},
                    'price_v':{'title':'Ед.изм','value':pr.name, 'id':pr.id},
                    'percent':{'title':'Наценка(%)','value':p.percent},
                    'count':{'title':'Количество в упаковке','value':p.count}}}

    def post(self, product_id):
        resp = request.get_json()
        cat_id = Category.query.filter_by(name=resp['category']['value']).first()
        country_id = Country.query.filter_by(name=resp['country']['value']).first()
        pricev_id = Price_v.query.filter_by(name=resp['price_v']['value']).first()
        cur_id = Currency.query.filter_by(name=resp['currency']['value']).first()
        prod = Product.query.get(int(product_id))
        prod.name = resp['name']['value']
        prod.category = cat_id.id
        prod.factory = resp['factory']['value']
        prod.country = country_id.id
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

    def delete(self, product_id):
        prod = Product.query.get_or_404(product_id)
        try:
            db.session.delete(prod)
            db.session.commit()
            return {'status':'ok',}
        except Exception as e:
            print(str(e))
            db.session.rollback()
            return {'status':'error',}


rest_api.add_resource(Item, '/api/item/<int:product_id>')


class Categories(Resource):
    def get(self):
        c = Category.query.all()
        cs = [{'id':x.id, 'name':x.name, 'article':'0', 'count':'1'} for x in c]
        return {'status':'ok', 'items':cs}
    def post(self):
        resp = request.get_json()
        cats = Category.query.all()
        update_list = []
        for cat in cats:
            for item in resp:
                if cat.id == item['id'] and cat.name != item['name']:
                    cat.name = item['name']
                    update_list.append(cat)
        for item in resp:
            if item['id'] == '0':
                c = Category(name=item['name'])
                update_list.append(c)
        try:
            db.session.add_all(update_list)
            db.session.commit()
        except Exception as e:
            print(str(e))
            db.session.rollback()
            return {'status':'error', 'error':str(e)}
        return {'status':'ok'}

rest_api.add_resource(Categories, '/api/category/')


class Products(Resource):
    def get(self, category_id):
        category = Category.query.get(category_id)
        products = category.products.order_by(Product.id.desc()).all()
        p = [{'id':x.id, 'name':x.name, 'image_url':x.image_url, 'sm_image_url':x.sm_image_url, 'article':x.article} for x in products]
        return {'status':'ok','items':p}

rest_api.add_resource(Products, '/api/products/<int:category_id>')


class Countries(Resource):
    def get(self):
        countries = Country.query.all()
        return {'status':'ok','items':[{'id':x.id, 'name':x.name, 'count':'1'} for x in countries]}
    def post(self):
        resp = request.get_json()
        cous = Country.query.all()
        update_list = []
        for cou in cous:
            for item in resp:
                if cou.id == item['id'] and cou.name != item['name']:
                    cou.name = item['name']
                    update_list.append(cou)
        for item in resp:
            if item['id'] == '0':
                c = Country(name=item['name'])
                update_list.append(c)
        try:
            db.session.add_all(update_list)
            db.session.commit()
        except Exception as e:
            print(str(e))
            db.session.rollback()
            return {'status':'error', 'error':str(e)}
        return {'status':'ok'}

rest_api.add_resource(Countries, '/api/countries/')


class Pricevs(Resource):
    def get(self):
        pricevs = Price_v.query.all()
        return {'status':'ok','items':[{'id':x.id, 'name':x.name, 'count':'1'} for x in pricevs]}
    def post(self):
        resp = request.get_json()
        pris = Price_v.query.all()
        update_list = []
        for pri in pris:
            for item in resp:
                if pri.id == item['id'] and pri.name != item['name']:
                    pri.name = item['name']
                    update_list.append(pri)
        for item in resp:
            if item['id'] == '0':
                c = Price_v(name=item['name'])
                update_list.append(c)
        try:
            db.session.add_all(update_list)
            db.session.commit()
        except Exception as e:
            print(str(e))
            db.session.rollback()
            return {'status':'error', 'error':str(e)}
        return {'status':'ok'}

rest_api.add_resource(Pricevs, '/api/pricev/')


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

