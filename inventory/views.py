import requests
from django.http import HttpResponse
from django.shortcuts import reverse
from django.views.generic import ListView, DetailView

from .models import Inventory


class InventoryListView(ListView):
    template_name = 'inventory/inventories.html'

    def get_queryset(self):
        url = self.request.build_absolute_uri(reverse('inventory_api:inventory_list'))
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return HttpResponse('Api down.', status_code=503)


inventory_list = InventoryListView.as_view()


class InventoryDetailView(DetailView):
    template_name = 'inventory/detail.html'

    def get_queryset(self):
        return Inventory.objects.select_related('supplier')


inventory_detail = InventoryDetailView.as_view()
