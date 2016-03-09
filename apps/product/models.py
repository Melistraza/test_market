from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)  # SlugField
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # At first it was DecimalField but I do not know why I changed
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse('product_page', kwargs={'product_slug': self.slug})


class Comment(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse(
            'product_page',
            kwargs={'product_slug': self.product.slug}) + '#%i' % self.id
