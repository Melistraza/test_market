from django.conf.urls import patterns, include, url
import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^products/', views.product_list, name='home'),
)

