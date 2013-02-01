from django.conf.urls import patterns, include, url
from crypt_key.views import main
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'crypt_key.views.main', name='main'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    # url(r'^$', 'cryptography.views.home', name='home'),
    # url(r'^cryptography/', include('cryptography.foo.urls')),
)
