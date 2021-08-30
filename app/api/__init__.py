from app import db, rest_api
from app.models import Product, Factory, Category
from flask_restful import Resource


class Prod(Resource):
    def get(self, product_id):
        prod = db.session.query(Product, Factory, Category)\
                .filter_by(id=int(product_id))\
                .join(Factory)\
                .join(Category)\
                .first()
        p = prod[0]
        f = prod[1]
        c = prod[2]
        return {'status':'ok',
                'product':{
                    'name':{'title':'Название','value':p.name},
                    'category':{'title':'Категория','value':c.name},
                    'article':{'title':'Артикул','value':p.article},
                    'factory':{'title':'Фабрика','value':f.name},
                    'country':{'title':'Страна','value':p.country},
                    'collection':{'title':'Коллекция','value':p.collection},
                    'price':{'title':'Цена','value':p.price},
                    'price_v':{'title':'Ед.изм','value':p.price_v},
                    'price_m':{'title':'Ден.ед.','value':p.price_m},
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

