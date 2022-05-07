from django.urls import path

from .views import inventory_list, inventory_detail

app_name = 'inventory'

urlpatterns = [
    path('inventory/', inventory_list, name='inventory_list'),
    path('inventory/<pk>/', inventory_detail, name='inventory_detail'),
]
