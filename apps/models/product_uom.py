from django.db import models

from apps.models.products import Product
from apps.models.uoms import UOM


class ProductUOM(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    uom = models.ForeignKey(UOM, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('product', 'uom')