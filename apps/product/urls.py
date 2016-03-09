from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.cache import cache_page
from django.conf.urls import patterns, url
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    # cache page with 5s
    url(r'^products/(?P<product_slug>[0-9A-Za-z._%+-]+)/$',
        views.product_page, name='product_page'),
    url(r'^products/',
        cache_page(5)(views.product_list), name='product_list'),
    url(r'^like/(?P<product_slug>[0-9A-Za-z._%+-]+)/$',
        views.like, name='like'),
)

urlpatterns += staticfiles_urlpatterns()
