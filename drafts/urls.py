# coding: utf-8

from django.conf.urls import url

from .views import DraftCreateView


urlpatterns = [
    url(r'^create/$', DraftCreateView.as_view(), name='create'),
]
