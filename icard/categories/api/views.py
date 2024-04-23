from rest_framework.viewsets import ModelViewSet
from categories.models import categories
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from categories.api.serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]