from flask import Blueprint, render_template
from flask_login import current_user, login_required
from grocery_store.models import Order

orders = Blueprint('orders', __name__)


@orders.route('/orders')
@login_required
def get_user_orders():
    if current_user:
        user_orders = Order.query.filter_by(user_id=current_user.user_id).all()
        return render_template('orders.html', orders=user_orders)
