import requests
from requests.exceptions import ConnectionError
from django.http import HttpResponse
from django.shortcuts import reverse, render
from django.views.generic import DetailView

from .models import Inventory


def inventory_list(request):
    template_name = 'inventory/inventories.html'
    url = request.build_absolute_uri(reverse('inventory_api:inventory_list'))
    msg = 'Inventory fetching api is not working properly. Try again later.'
    try:
        response = requests.get(url)
    except ConnectionError:
        return HttpResponse(msg, status_code=503)
    else:
        if response.status_code == 200:
            return render(request, template_name, {'object_list': response.json()})
        else:
            return HttpResponse(msg, status=503)


class InventoryDetailView(DetailView):
    template_name = 'inventory/detail.html'

    def get_queryset(self):
        return Inventory.objects.select_related('supplier')


inventory_detail = InventoryDetailView.as_view()
