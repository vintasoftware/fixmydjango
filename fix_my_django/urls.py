# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^', include('errors.urls', namespace='errors')),
    url(r'^admin/', include(admin.site.urls)),
)