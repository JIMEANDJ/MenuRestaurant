from rest_framework.serializers import ModelSerializer

from products.models import Product
from categories.api.serializer import CategorySerializer

class ProductSerializer(ModelSerializer):
    category_data = CategorySerializer(source='categories', read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'description', 'price', 'active', 'categories', 'category_data']