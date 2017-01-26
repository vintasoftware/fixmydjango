# coding: utf-8

from django.conf.urls import url

from .views import SignUpView


urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
]
