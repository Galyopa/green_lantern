from flask import request
from flask_restful import Resource, marshal

from grocery_store.models import Product
from grocery_store.db import db
from grocery_store.routes.marshal_structure import goods_structure


class Goods(Resource):
    def get(self, product_id=None):
        if product_id:
            product = Product.query.get(product_id)
            if product:
                return marshal(product, goods_structure)
            return f"No such product with id: {product_id}"
        return marshal(Product.query.all(), goods_structure)

    def post(self):
        product = Product(**request.json)
        db.session.add(product)
        db.session.commit()
        return f"Successfully added a new product {product}"

    def put(self, product_id):
        product = Product.query.get(product_id)
        product.brand = request.json.get('brand', product.brand)
        product.name = request.json.get('name', product.name)
        product.price = request.json.get('price', product.price)
        db.session.commit()
        return f"Successfully updated product with id: {product_id}"

    def delete(self, product_id):
        product = Product.query.get(product_id)
        db.session.delete(product)
        db.session.commit()
        return f"Successfully deleted product with id: {product_id}"
