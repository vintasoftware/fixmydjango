# coding: utf-8

from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.sitemaps.views import sitemap

from django.views.generic import TemplateView

from error_posts.sitemaps import ErrorPostSitemap


urlpatterns = patterns('',
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('error_posts.urls', namespace='error_posts')),

    # SEO
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'error': ErrorPostSitemap}},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^google44a604e6db8d2224\.html$', TemplateView.as_view(
        template_name='gwm-verify.html'), name='gwm-verify'),
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt'), name='robots-txt')
)
