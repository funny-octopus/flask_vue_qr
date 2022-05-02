from flask import request
from flask_login import login_required
from flask_restful import Resource, reqparse
from app import db
from app.models import *

class Item(Resource):
    @login_required
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
                    'provider':{'title':'Поставщик','value':p.provider},
                    'country':{'title':'Страна','value':co.name, 'id':co.id},
                    'collection':{'title':'Коллекция','value':p.collection},
                    'size':{'title':'Размер','value':p.size},
                    'name':{'title':'Название','value':p.name},
                    'price':{'title':'Цена','value':p.price},
                    'currency':{'title':'Ден.ед.','value':cu.name,'id':cu.id},
                    'course':{'title': 'Курс', 'value': p.course},
                    'price_v':{'title':'Ед.изм','value':pr.name, 'id':pr.id},
                    'percent':{'title':'Наценка(%)','value':p.percent},
                    'count':{'title':'Количество в упаковке','value':p.count},
                    'notes':{'title':'Примечания','value':p.notes}
                    }
                }

    @login_required
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
        prod.provider = resp['provider']['value']
        prod.country = country_id.id
        prod.collection = resp['collection']['value']
        prod.size = resp['size']['value']
        prod.price = str(resp['price']['value']).strip().replace(' ', '').replace(',','.')
        prod.course = resp['course']['value']
        prod.price_v = pricev_id.id
        prod.price_m = cur_id.id
        prod.percent = str(resp['percent']['value']).strip().replace(' ', '').replace(',','.')
        prod.count = str(resp['count']['value']).strip().replace(' ', '').replace(',','.')
        prod.notes = resp['notes']['value']
        prod.set_article()
        try:
            db.session.add(prod)
            db.session.commit()
            return {'status':'ok','article':prod.article}
        except Exception as e:
            print(str(e))
            db.session.rollback()
            return {'status':'error',}, 500

    @login_required
    def delete(self, product_id):
        prod = Product.query.get_or_404(product_id)
        try:
            db.session.delete(prod)
            db.session.commit()
            return {'status':'ok',}
        except Exception as e:
            db.session.rollback()
            return {'status':'error',}, 500


class Categories(Resource):
    @login_required
    def get(self):
        c = Category.query.all()
        cs = [{'id':x.id, 'name':x.name, 'article':'0', 'count':'1'} for x in c]
        return {'status':'ok', 'items':cs}
    @login_required
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
            db.session.rollback()
            return {'status':'error', 'error':str(e)}, 500
        return {'status':'ok'}


class Products(Resource):
    @login_required
    def get(self, category_id):
        parser = reqparse.RequestParser()
        parser.add_argument('factory')
        parser.add_argument('collection')
        parser.add_argument('provider')
        args = parser.parse_args()
        category = Category.query.get(category_id)
        # products = category.products.order_by(Product.name).all()
        products = category.products
        items = {}
        if args.get('factory'): items.update({'factory': args.get('factory')})
        if args.get('collection'): items.update({'collection': args.get('collection')})
        if args.get('provider'): items.update({'provider': args.get('provider')})
        # print(products.statement)
        if items:
            products = products.filter_by(**items)
        products = products.order_by(Product.name).all()
        pr = [{'id':x.id,\
                'name':x.name,\
                'image_url':x.image_url,\
                'sm_image_url':x.sm_image_url,\
                'article':x.article,\
                'factory':x.factory,\
                'collection':x.collection} for x in products]

        category = Category.query.get(category_id)
        items = category.products
        props = {}
        if args.get('collection'): props.update({'collection': args.get('collection')})
        if args.get('provider'): props.update({'provider': args.get('provider')})
        if props: items = items.filter_by(**props) 
        f = [x.factory for x in items.all()]

        category = Category.query.get(category_id)
        items = category.products
        props = {}
        if args.get('factory'): props.update({'factory': args.get('factory')})
        if args.get('provider'): props.update({'provider': args.get('provider')})
        if props: items = items.filter_by(**props) 
        c = [x.collection for x in items.all()]

        category = Category.query.get(category_id)
        items = category.products
        props = {}
        if args.get('collection'): props.update({'collection': args.get('collection')})
        if args.get('factory'): props.update({'factory': args.get('factory')})
        if props: items = items.filter_by(**props) 
        p = [x.provider for x in items.all()]

        return {'status':'ok','items':pr, 'factories':f, 'collections':c, 'providers':p}


class Countries(Resource):
    @login_required
    def get(self):
        countries = Country.query.order_by(Country.name).all()
        return {'status':'ok','items':[{'id':x.id, 'name':x.name, 'count':'1'} for x in countries]}
    @login_required
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
            db.session.rollback()
            return {'status':'error', 'error':str(e)}, 500
        return {'status':'ok'}


class Pricevs(Resource):
    @login_required
    def get(self):
        pricevs = Price_v.query.all()
        return {'status':'ok','items':[{'id':x.id, 'name':x.name, 'count':'1'} for x in pricevs]}
    @login_required
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
            db.session.rollback()
            return {'status':'error', 'error':str(e)}, 500
        return {'status':'ok'}


class Items(Resource):
    @login_required
    def get(self):
        cats = Category.query.all()
        cou = Country.query.all()
        cur = Currency.query.all()
        pr = Price_v.query.all()
        c = {'category': [x.name for x in cats],
             'country': [x.name for x in cou],
             'currency': [x.name for x in cur],
             'price_v': [x.name for x in pr],
             'course': ['ЦБ', 'Курс №1', 'Курс №2'],
             }
        return {'status':'ok', 'items':c}

