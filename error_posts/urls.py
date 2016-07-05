# coding: utf-8

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import ErrorPostListView, ErrorPostDetailView
from .endpoints import ExceptionSearchAPIView


urlpatterns = patterns('',
    url(r'^$', ErrorPostListView.as_view(), name='list'),
    url(r'^exceptions/(?P<slug>[\w-]+)/$', ErrorPostDetailView.as_view(), name='detail'),

    url(r'^how-it-works/$',
        TemplateView.as_view(template_name='error_posts/how_it_works.html'),
        name='how_it_works'),

    url(r'api/search/$', ExceptionSearchAPIView.as_view(), name='api-search'),
)
