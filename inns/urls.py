# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from servicespost.views import Services, Add_ServiceView

#admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^search/', SearchResults.as_view(), name = 'searchresults'),
    #url(r'^add/', Add_ServiceView, name='Add_Service'),
    url(r'^$', Services, name='Services'),
    url(r'^agregar/', Add_ServiceView, name='Add_Service'),
    url(r'^(?P<slug_type>[a-zA-Z0-9_-]+)/(?P<slug_city>[a-zA-Z0-9_-]+)/(?P<slug_zone>[a-zA-Z0-9_-]+)/$', Services, name='Services'),
    url(r'^(?P<slug_type>[a-zA-Z0-9_-]+)/(?P<slug_city>[a-zA-Z0-9_-]+)/$', Services, name='Services'),
    url(r'^(?P<slug_type>[a-zA-Z0-9_-]+)/$', Services, name='Services'),

    url(r'^(?P<slug_city>[a-zA-Z0-9_-]+)/(?P<slug_zone>[a-zA-Z0-9_-]+)/$', Services, name='Services'),
    url(r'^(?P<slug_city>[a-zA-Z0-9_-]+)/$', Services, name='Services'),

    #url(r'^servicedetails/(?P<slug>[a-zA-Z0-9_-]+)/?$', ServiceDetails.as_view(), name='detalles'),
    #url(r'^servicedetails/(?P<slug>[-\w]+)$','servicespost.views.view_service', name='service_detail'),
    url(r'^(?P<slug_type>[a-zA-Z0-9_-]+)/(?P<slug_city>[a-zA-Z0-9_-]+)/(?P<slug_zone>[a-zA-Z0-9_-]+)/(?P<slug>[-\w]+)/$','servicespost.views.view_service',
        name='service_detail'),
    url(r'^(?P<slug_type>[a-zA-Z0-9_-]+)/(?P<slug_city>[a-zA-Z0-9_-]+)/(?P<slug_zone>[a-zA-Z0-9_-]+)/(?P<slug>[-\w]+)/reservacion/$','servicespost.views.view_reservation',
        name='Reservation'),
    url(r'^(?P<slug_type>[a-zA-Z0-9_-]+)/(?P<slug_city>[a-zA-Z0-9_-]+)/(?P<slug_zone>[a-zA-Z0-9_-]+)/(?P<slug>[-\w]+)/reservacion/(?P<bookroom_id>[0-9_-]+)$',
    'servicespost.views.view_confirmation', name='Confirmation'),
    #url(r'^detalles/(?P<slug_city>[a-zA-Z0-9_-]+)/(?P<slug_zone>[a-zA-Z0-9_-]+)/(?P<slug>[a-zA-Z0-9_-]+)/?$', Detalles.as_view(), name='detalles'),

)
