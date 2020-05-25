from flask import Blueprint
from flask_restful import Api

from grocery_store.routes.users import Users
from grocery_store.routes.goods import Goods
from grocery_store.routes.stores import Stores
from grocery_store.routes.auth import auth
from grocery_store.routes.main import main
from grocery_store.routes.orders import Orders, orders, OrderLines, order_lines

users = Blueprint("users", __name__)
goods = Blueprint("goods", __name__)
stores = Blueprint("stores", __name__)

api_users = Api(users)
api_goods = Api(goods)
api_stores = Api(stores)
api_orders = Api(orders)
api_order_lines = Api(order_lines)

api_users.add_resource(Users, "/users", "/users/<user_id>")
api_goods.add_resource(Goods, "/goods", "/goods/<good_id>")
api_stores.add_resource(Stores, "/stores", "/stores/<store_id>")
api_stores.add_resource(Orders, "/orders_api", "/orders_api/<order_id>")
api_stores.add_resource(OrderLines, "/order_lines_api", "/order_lines_api/<order_id>")

__all__ = ['users', 'goods', 'stores', 'auth', 'main', 'orders', 'order_lines']
