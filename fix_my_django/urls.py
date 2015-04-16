# coding: utf-8

from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap

from errors.sitemaps import ErroSitemap


urlpatterns = patterns('',
    url(r'^', include('errors.urls', namespace='errors')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'error': ErroSitemap}},
    name='django.contrib.sitemaps.views.sitemap')
)