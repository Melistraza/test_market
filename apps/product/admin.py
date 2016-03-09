from django.contrib import admin
from apps.product.models import Product, Comment


class AdminProduct(admin.ModelAdmin):
    list_display = ('name',)


class AdminComment(admin.ModelAdmin):
    list_display = ('text',)

admin.site.register(Comment, AdminComment)
admin.site.register(Product, AdminProduct)
