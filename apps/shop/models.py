from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
