from django.db import models

from apps.models.categories import Category
from apps.models.products import Product


class CategoryProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('category', 'product')