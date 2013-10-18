from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ziolupo.ricette.views',
    # Examples:
    url(r'^ricette/$', 'ricette_list', name='api_ricette_list'),
    url(r'^ricette/(?P<pk>[0-9]+)/$', 'ricette_detail', name='api_ricette_detail'),
    url(r'^categorie/(?P<pk>[0-9]+)/$', 'categorie_detail', name='api_categorie_detail'),
    url(r'^categorie/$', 'categorie_list', name='api_categorie_list'),
    url(r'^listeveloci/$', 'listeveloci_list', name='api_listeveloci_list'),
    url(r'^listeveloci/(?P<pk>[0-9]+)/$', 'listeveloci_detail', name='api_listeveloci_detail'),
    url(r'^$', 'index', name='home'),


    # url(r'^$', 'ziolupo.views.home', name='home'),
    # url(r'^ziolupo/', include('ziolupo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)