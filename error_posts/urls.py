# coding: utf-8

from django.conf.urls import patterns, include, url

from .views import ErrorPostListView, ErrorPostDetailView
from .endpoints import ExceptionSearchAPIView


urlpatterns = patterns('',
    url(r'^$', ErrorPostListView.as_view(), name='list'),
    url(r'^exceptions/(?P<slug>[\w-]+)/$', ErrorPostDetailView.as_view(), name='detail'),

    url(r'api/search/$', ExceptionSearchAPIView.as_view(), name='api-search'),
)
