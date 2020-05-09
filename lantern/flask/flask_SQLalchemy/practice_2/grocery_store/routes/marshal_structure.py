from flask_restful import fields

users_structure = {
    "user_id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "password": fields.Raw
}

goods_structure = {
    "product_id": fields.Integer,
    "name": fields.String,
    "brand": fields.String,
    "price": fields.Float,
}

stores_structure = {
    "store_id": fields.Integer,
    "name": fields.String,
    "city": fields.String,
    "address": fields.String,
    "manager_id": fields.Integer
}
