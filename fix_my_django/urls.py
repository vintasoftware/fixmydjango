# coding: utf-8

from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap

from django.views.generic import TemplateView

from errors.sitemaps import ErrorSitemap


urlpatterns = patterns('',
    url(r'^', include('errors.urls', namespace='errors')),
    url(r'^admin/', include(admin.site.urls)),

    # SEO
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'error': ErrorSitemap}},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^google44a604e6db8d2224\.html$',
        TemplateView.as_view(template_name='gwm-verify.html'), name='gwm-verify')
)