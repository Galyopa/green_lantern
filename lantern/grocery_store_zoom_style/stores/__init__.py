from flask import Blueprint
from flask_restful import Api
from stores.routes import Stores

stores = Blueprint("stores", __name__)
api_stores = Api(stores)

api_stores.add_resource(Stores, "/stores", "/stores/<store_id>")
