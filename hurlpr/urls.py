from django.conf.urls import patterns, include, url
#from django.contrib import admin
from hurl import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^(|about|copyright)$', include('hurl.urls')),
    url(r'^create/(?P<addfile>[a-z]+\.txt)$', views.add_url_file),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^(?P<layout>[a-z]{2,3}\-[a-zA-Z\-]{2,10})/?$', views.view_layout),
    url(r'^(?P<layout>[a-zA-Z\-]{2,12})/(?P<url_name>[\.\-\w]+)$', views.show_url),
    url(r'^(?P<url_name>[\.\-\w]+)/create/$', views.create_url),
    # url(r'^hurlpr/', include('hurlpr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
