from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.api.serializers import ProductSerializerS

from products.models import Product

class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    seriializer_class = ProductSerializer
    queryset = Product.objects.all()
    filters = ['title', 'description', 'price', 'active', 'categories']