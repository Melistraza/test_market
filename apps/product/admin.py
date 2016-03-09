from django.contrib import admin
from apps.product.models import Product, Comment
from django.conf import settings
domain = settings.DOMAIN
# domain hardoce because all project must be set up on server
# i use variable in setting instead of Site object in fixtures


class AdminProduct(admin.ModelAdmin):
    list_display = ('name',)


class AdminComment(admin.ModelAdmin):
    list_display = ('text',)

admin.site.register(Comment, AdminComment)
admin.site.register(Product, AdminProduct)
