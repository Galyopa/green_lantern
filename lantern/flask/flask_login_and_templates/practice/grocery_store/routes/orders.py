from flask import Blueprint, render_template
from flask_login import current_user, login_required

orders = Blueprint('orders', __name__)


@orders.route('/orders')
@login_required
def get_user_orders():
    orders_list = []
    for order in current_user.orders:
        order_data = {"store": order.store.name,
                      "order_date": order.created_time,
                      "order_price": sum([good.good.price for good in order.order_lines]),
                      "order_goods": {good.good.name: good.good.price for good in order.order_lines}
                      }
        orders_list.append(order_data)
    return render_template('orders.html', orders=orders_list)
