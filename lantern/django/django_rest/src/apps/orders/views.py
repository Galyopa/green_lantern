# Create your views here.
from apps.orders.models import Order
from apps.orders.serializers import SimpleOrderSerializer
from rest_framework import permissions
from rest_framework.generics import CreateAPIView


class OrderGenericView(CreateAPIView):
    queryset = Order.objects.all()
    # serializer_class = OrderSerializer
    serializer_class = SimpleOrderSerializer
    permission_classes = (permissions.AllowAny, )
