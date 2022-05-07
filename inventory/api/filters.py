from django_filters import rest_framework as filters

from ..models import Inventory


class InventoryFilter(filters.FilterSet):

    class Meta:
        model = Inventory
        fields = {"name": ['iexact', 'icontains']}
