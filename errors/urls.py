# coding: utf-8

from django.conf.urls import patterns, url

from .views import ErrorListView, ErrorDetailView

urlpatterns = patterns('',
    url(r'^$', ErrorListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ErrorDetailView.as_view(), name='detail'),
)
