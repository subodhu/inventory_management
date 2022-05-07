from django.test import TestCase
from django.shortcuts import reverse

from .models import Inventory, Supplier


class InventoryTest(TestCase):

    def _create_inventory(self):
        supplier = Supplier.objects.create(name='Famous Supplier')
        inventory = Inventory.objects.create(
            name="Jersy Inventory",
            description="jersy for everyone",
            note="Stocked everyday.",
            stock=12,
            availability=True,
            supplier=supplier,

        )
        return inventory

    def test_inventory_list_page(self):
        url = reverse('inventory:inventory_list')
        # explicitly added HTTP_HOST since the inventory list is fetched from inventory api
        # which is running at HTTP_HOST
        response = self.client.get(path=url, HTTP_HOST='localhost:8000')
        self.assertEqual(response.status_code, 200)
        self._create_inventory()
        response = self.client.get(path=url, HTTP_HOST='localhost:8000')
        self.assertEqual(response.status_code, 200)

    def test_inventory_list_api(self):
        url = reverse('inventory_api:inventory_list')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self._create_inventory()
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_page(self):
        inventory = self._create_inventory()
        url = reverse('inventory:inventory_detail', args=[inventory.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
