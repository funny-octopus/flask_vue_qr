from app import rest_api
from app.api.routes import Item, Categories, Products, Countries, Pricevs, Items


rest_api.add_resource(Item, '/api/item/<int:product_id>')
rest_api.add_resource(Categories, '/api/category/')
rest_api.add_resource(Products, '/api/products/<int:category_id>')
rest_api.add_resource(Countries, '/api/countries/')
rest_api.add_resource(Pricevs, '/api/pricev/')
rest_api.add_resource(Items, '/api/items')

