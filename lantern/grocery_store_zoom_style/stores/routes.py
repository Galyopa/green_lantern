from flask import request
from flask_restful import Resource, marshal_with, reqparse

from db import db_post

from stores.marshal_structure import stores_structure
from models.table_model import StoresModel
import json

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', required=False, type=str)


class Stores(Resource):
    # method_decorators = [check_login]  # add decorator check_login to all methods from Main

    @marshal_with(stores_structure)
    def get(self, store_id=None):
        if store_id:
            store = StoresModel.query.get(store_id)
            return store
        elif store_id is None:
            # reqparse do not work
            args = parser.parse_args()
            name = args['name']
            store = StoresModel.query.filter(StoresModel.name == name)
            return store
        else:
            return StoresModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_store = StoresModel(**data)
        db_post.session.add(new_store)
        db_post.session.commit()
        return "Successfully added a new store"

    def put(self, store_id):
        data = json.loads(request.data)
        update_store = StoresModel.query.get(store_id)

        update_store.name = data.get("name")
        update_store.location = data.get("location")

        db_post.session.commit()
        return "Successfully updated store"

    def delete(self, store_id):
        post = StoresModel.query.get(store_id)
        db_post.session.delete(post)
        db_post.session.commit()
        return "Successfully deleted store"
