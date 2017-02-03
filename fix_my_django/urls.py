# coding: utf-8

from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from error_posts.sitemaps import (
    IndexSitemap, ErrorPostSitemap
)


urlpatterns = [
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('error_posts.urls', namespace='error_posts')),
    url(r'^', include('users.global_urls')),

    # SEO
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {
            'index': IndexSitemap,
            'error_posts': ErrorPostSitemap
        }},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^google44a604e6db8d2224\.html$', TemplateView.as_view(
        template_name='gwm-verify.html'), name='gwm-verify'),
    url(r'^robots\.txt$', cache_page(7 * 24 * 60 * 60)(TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain')), name='robots-txt'),

    url(r'^', include('authtools.urls')),
]
