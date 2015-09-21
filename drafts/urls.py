# coding: utf-8

from django.conf.urls import patterns, url

from .views import DraftCreateView


urlpatterns = patterns('',
    url(r'^create/$', DraftCreateView.as_view(), name='create'),
)
