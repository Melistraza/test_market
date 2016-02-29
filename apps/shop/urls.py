import views
from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^products/(?P<product_slug>[0-9A-Za-z._%+-]+)/$', views.product_page, name='product_page'),
    url(r'^products/', views.product_list, name='product_list'),
)

