from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ziolupo.ricette.views',
    # Examples:
    url(r'^ricette/$', 'ricette_list', name='api_ricette_list'),
    url(r'^ricette/(?P<pk>[0-9]+)/$', 'ricette_detail', name='api_ricette_detail'),
    url(r'^categorie/(?P<pk>[0-9]+)/$', 'categorie_detail', name='api_categorie_detail'),
    url(r'^categorie/$', 'categorie_list', name='api_categorie_list'),
    url(r'^portate/(?P<nome>[-\w]+)/$', 'portate_detail', name='api_portate_detail'),
    url(r'^portate/$', 'portate_list', name='api_portate_list'),

    # url(r'^$', 'ziolupo.views.home', name='home'),
    # url(r'^ziolupo/', include('ziolupo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
