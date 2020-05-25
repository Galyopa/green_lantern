from flask_restful import fields

users_structure = {
    "user_id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
}

goods_structure = {
    "good_id": fields.Integer,
    "name": fields.String,
    "brand": fields.String,
    "price": fields.Integer,
}
stores_structure = {
    "store_id": fields.Integer,
    "name": fields.String,
    "city": fields.String,
    "address": fields.String,
    "manager_id": fields.Integer,
}
orders_structure = {
    "order_id": fields.Integer,
    "user_id": fields.Integer,
    "created_time": fields.DateTime,
    "store_id": fields.Integer,

}
order_lines_structure = {
    "order_line_id": fields.Integer,
    "order_id": fields.Integer,
    "good_id": fields.Integer,
}
