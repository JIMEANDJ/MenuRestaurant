from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from tables.models import Table
from tables.api.serializers import TableSerializer

class TableApiViewSet(ModelViewSet):
    queryset = Table.objects.all().order_by('number')
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]