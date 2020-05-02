from flask_restful import Resource
from db import db_post


class CreateDB(Resource):

    def post(self):
        db_post.create_all()
        db_post.session.commit()
        return "ok"
