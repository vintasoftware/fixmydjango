# coding: utf-8

from django.conf.urls import patterns, url

from .views import ErrorPostListView, ErrorPostDetailView

urlpatterns = patterns('',
    url(r'^$', ErrorPostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ErrorPostDetailView.as_view(), name='detail'),
)
