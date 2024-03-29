from rest_framework.serializers import ModelSerializer
from categories.models import categories

class CategorySerializer(ModelSerializer):
    class Meta:
        model = categories
        fields = 'id', 'title', 'image'