from django.conf.urls import patterns, url

from hurl import views

urlpatterns = patterns('',
  url(r'^(|copyright|about)$', views.index, name='index')
)
