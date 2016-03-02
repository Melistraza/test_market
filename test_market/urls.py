from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('apps.product.urls')),
    url(r'^/$', RedirectView.as_view(pattern_name='product_list')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='product_list')),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout', name='logout'),
)
urlpatterns += staticfiles_urlpatterns()
