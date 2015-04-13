# coding: utf-8

from django.views.generic import DetailView

from django_filters.views import FilterView

from .models import Error
from .filtersets import ErrorFilter


class ErrorListView(FilterView):
    template_name = 'errors/list.html'
    model = Error
    filterset_class = ErrorFilter


class ErrorDetailView(DetailView):
    template_name = 'errors/detail.html'
    model = Error
