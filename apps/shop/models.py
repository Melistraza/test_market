from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField()
