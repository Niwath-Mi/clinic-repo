from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    description = models.TextField()

    def __str__(self):
        return self.name