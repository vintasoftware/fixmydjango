# coding: utf-8

from django.conf.urls import patterns, url

from .views import ErrorListView

urlpatterns = patterns('',
    url(r'^$', ErrorListView.as_view(), name='list'),
)
