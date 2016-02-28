from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
