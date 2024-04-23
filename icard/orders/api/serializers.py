from rest_framework.serializers import ModelSerializer

from orders.models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'table', 'product', 'status', 'created_at', 'close']
        