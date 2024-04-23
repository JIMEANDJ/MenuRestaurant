from rest_framework.viewsets import ModelViewSet
from orders.models import Order
from .serializers import OrderSerializer

class OrderApiViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer