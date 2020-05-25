from flask import Blueprint, render_template
from flask_restful import marshal, Resource
from grocery_store.models import Order, OrderLine
from grocery_store.routes.marshal_structure import orders_structure, order_lines_structure
from flask_login import current_user

orders = Blueprint('orders', __name__)
order_lines = Blueprint('order_lines', __name__)


@orders.route('/orders')
def login():
    return render_template('orders.html', orders=Order.query.filter_by(user_id=current_user.user_id).all(),
                           order_lines=OrderLine.query.filter_by().all())


class Orders(Resource):
    def get(self, order_id=None, user_id=current_user):
        if order_id:
            order = Order.query.get(order_id)
            if order:
                return marshal(order, orders_structure)
            return f"No such order with id: {order_id}"
        return marshal(Order.query.get(user_id), orders_structure)


class OrderLines(Resource):
    def get(self, order_id=None):
        if order_id:
            order_lines = OrderLine.query.get(order_id)
            if order_lines:
                return marshal(order_lines, order_lines_structure)
            return f"No such order with id: {order_id}"
        return marshal(OrderLine.query.all(), order_lines_structure)
