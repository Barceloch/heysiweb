from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heysiweb.views.home', name='home'),
    # url(r'^heysiweb/', include('heysiweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^contacto/', 'heysiweb.views.view_contact'),
    url(r'^captcha/', include('captcha.urls')),    
    url(r'^$', 'heysiweb.views.home', name='home'),
    url(r'^inicio$', 'heysiweb.views.home'),
    url(r'^faqs$', 'heysiweb.views.view_faqs'),    
    url(r'^hostales/', 'inns.views.inns'),
    url(r'^agregar/', 'inns.views.Add_InnView'),
    url(r'^(?P<slug>[-\w]+)/$','inns.views.view_inn', name='inn-details'),
    url(r'^(?P<slug>[-\w]+)/reservacion/$','inns.views.view_reservation', name='Reservation'),
    url(r'^(?P<slug>[-\w]+)/reservacion/(?P<bookroom_id>[0-9_-]+)$','inns.views.view_confirmation', name='Confirmation'),
)
urlpatterns += staticfiles_urlpatterns()
