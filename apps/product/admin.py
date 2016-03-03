from django.contrib import admin
from apps.product.models import Product, Comment
from django.core.urlresolvers import reverse
from django.conf import settings
domain = settings.DOMAIN
# domain hardoce because all project must be set up on server
# i use variable in setting instead of Site object in fixtures


class AdminProduct(admin.ModelAdmin):
    list_display = ('name',)

    def view_on_site(self, obj):
        return domain + reverse(
            'product_page', kwargs={'product_slug': obj.slug})


class AdminComment(admin.ModelAdmin):
    list_display = ('text',)

    def view_on_site(self, obj):
        return domain + reverse(
            'product_page', kwargs={'product_slug': obj.product.slug}
        ) + '#' + str(obj.id)

admin.site.register(Comment, AdminComment)
admin.site.register(Product, AdminProduct)
