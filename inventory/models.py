from django.db import models
from django.utils.translation import gettext_lazy as _


class Inventory(models.Model):
    name = models.CharField(_('Name'), max_length=56, unique=True)
    description = models.CharField(_("Description"), max_length=256)
    note = models.TextField(_("Note"))
    stock = models.PositiveIntegerField(_("Stock"))
    availability = models.BooleanField(_("Availiability"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("inventory")
        verbose_name_plural = _("inventorys")

    def __str__(self):
        return f'{self.name}: {self.stock}'


class Suplier(models.Model):
    name = models.CharField(_('Supplier Name'), max_length=56)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("supplier")
        verbose_name_plural = _("suppliers")

    def __str__(self):
        return self.name
