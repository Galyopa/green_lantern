import pytest
from rest_framework.reverse import reverse

from apps.orders.models import Order
from tests.fixtures.cars import CarFactory, OrderFactory


@pytest.mark.django_db()
def test_order_create(client):
    car = CarFactory()
    data = {
        'first_name': 'Denys',
        'last_name': 'Halopa',
        'email': 'galyopa@gmail.com',
        'phone': '+380675189343',
        'car': car.id,
    }

    assert Order.objects.count == 0

    resp = client.post(
        path=reverse('orders:create'),
        data=data
    )

    assert resp.status_code == 201
    orders = Order.objects.all()
    assert len(orders) == 1
    assert orders[0].first_name == 'Denys'
    assert orders[0].last_name == 'Halopa'
    assert orders[0].email == 'galyopa@gmail.com'
    assert orders[0].phone == '+380675189343'
    assert orders[0].car_id == car.id


@pytest.mark.django_db()
def test_order_create_unique(client):
    car = CarFactory()
    order = OrderFactory(email='order1@gmail.com', car=car)
    data = {
        'first_name': 'Denys',
        'last_name': 'Halopa',
        'email': 'order1@gmail.com',
        'phone': '+380675189343',
        'car': car.id,
    }

    resp = client.post(
        path=reverse('orders:create'),
        data=data
    )

    assert resp.status_code == 400
    assert Order.objects.count == 1
