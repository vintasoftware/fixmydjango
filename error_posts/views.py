# coding: utf-8

from django.views.generic import DetailView

from django_filters.views import FilterView

from .mixins import ErrorPostListMetadataMixin, ErrorPostMetadataMixin
from .filtersets import ExceptionSearchFilter
from .models import ErrorPost


class ErrorPostListView(ErrorPostListMetadataMixin, FilterView):
    template_name = 'error_posts/list.html'
    filterset_class = ExceptionSearchFilter

    def get_queryset(self):
        return ErrorPost.publisheds.all()


class ErrorPostDetailView(ErrorPostMetadataMixin, DetailView):
    template_name = 'error_posts/detail.html'

    def get_queryset(self):
        return ErrorPost.publisheds.all()
