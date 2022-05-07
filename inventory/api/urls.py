from django.urls import path

from .views import inventories_view

app_name = 'inventory'

urlpatterns = [
    path('inventory/', inventories_view, name='inventory_list'),
]
