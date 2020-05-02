import json

from flask import request
from flask_restful import Resource, marshal_with

from db import db_post
from models.table_model import UsersModel
from users.marshal_structure import users_structure


class Users(Resource):

    @marshal_with(users_structure)
    def get(self, user_id):
        user = UsersModel.query.get(user_id)
        return user

    def post(self):
        data = json.loads(request.data)
        new_user = UsersModel(**data)
        db_post.session.add(new_user)
        db_post.session.commit()
        return "Successfully added a new user", 201

    def put(self, user_id):
        data = json.loads(request.data)
        update_user = UsersModel.query.get(user_id)
        update_user.username = data.get("username")
        db_post.session.commit()
        return "Successfully updated the username", 200

    def delete(self, user_id):
        post = UsersModel.query.get(user_id)
        db_post.session.delete(post)
        db_post.session.commit()
        return "Successfully deleted the user", 200
