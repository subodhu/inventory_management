from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from ..models import Inventory
from .filters import InventoryFilter
from .serializers import InventorySerializer


class InventoryListApiView(ListAPIView):
    filter_backends = (filters.DjangoFilterBackend, rest_filters.OrderingFilter)
    filterset_class = InventoryFilter
    ordering_fields = ['name', 'stock', 'created_at']
    queryset = Inventory.objects.select_related('supplier')
    serializer_class = InventorySerializer


inventories_view = InventoryListApiView.as_view()
