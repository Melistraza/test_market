from django.contrib import admin
from apps.shop.models import Product, Comments


class AdminProduct(admin.ModelAdmin):
    list_display = ('name',)

    # def view_on_site(self, obj):
    #     return 'http://127.0.0.1:8000/' + reverse('product-details',
    #                                           kwargs={'slug': obj.pk})


class AdminComments(admin.ModelAdmin):
    list_display = ('text',)

admin.site.register(Comments, AdminComments)
admin.site.register(Product, AdminProduct)
