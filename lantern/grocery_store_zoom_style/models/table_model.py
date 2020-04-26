from db import db_post


class UsersModel(db_post.Model):
    __tablename__ = 'users_table'

    id = db_post.Column(db_post.Integer, primary_key=True, autoincrement=True)
    username = db_post.Column(db_post.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class GoodsModel(db_post.Model):
    __tablename__ = 'goods_table'

    id = db_post.Column(db_post.Integer, primary_key=True, autoincrement=True)
    name = db_post.Column(db_post.String(120), unique=True, nullable=False)
    price = db_post.Column(db_post.Float, nullable=False)


class StoresModel(db_post.Model):
    __tablename__ = 'stores_table'

    id = db_post.Column(db_post.Integer, primary_key=True, autoincrement=True)
    name = db_post.Column(db_post.String(120), unique=True, nullable=False)
    location = db_post.Column(db_post.String(120), nullable=False)
    manager_id = db_post.Column(db_post.Integer, db_post.ForeignKey('users_table.id'))
