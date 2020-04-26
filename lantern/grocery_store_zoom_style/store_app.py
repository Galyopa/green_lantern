# import inject
from flask import Flask

# from flask_restful import Api
from config import run_config
from create_db import create_db
from db import db_post
from errors import NoSuchUserError, my_error_handler, NoSuchStoreError
# from fake_storage import FakeStorage
# from routes.stores import Store
# from routes.users import Users
# from routes.goods import Goods
from users import users
from stores import stores



# def configure(binder):
#     db = FakeStorage()
#     binder.bind('DB', db)


def make_app():
    # configure our database
    # inject.clear_and_configure(configure)

    app = Flask(__name__)
    # API
    # api = Api(app)
    app.config.from_object(run_config())
    db_post.init_app(app)
    app.register_blueprint(create_db)
    app.register_blueprint(users)
    app.register_blueprint(stores)
    # api.add_resource(Store, "/stores", "/stores/<int:store_id>")
    #   api.add_resource(Users, "/users", "/users/<int:user_id>")
    #    api.add_resource(Goods, "/goods")

    # register blueprints and error handlers

    app.register_error_handler(NoSuchUserError, my_error_handler)
    app.register_error_handler(NoSuchStoreError, my_error_handler)
    return app
