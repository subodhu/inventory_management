from django.contrib import admin

from .models import Inventory, Supplier


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'availability', 'supplier')
    list_filter = ('name',)
    ordering = ['-created_at']
    select_related_fields = ('supplier', )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    ordering = ['-created_at']
