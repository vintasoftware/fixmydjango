# coding: utf-8

from django.db.models import Q

import django_filters
from django_filters import MethodFilter

from .models import ErrorPost


class ErrorPostFilter(django_filters.FilterSet):
    exception_type = MethodFilter(action='filter_exception')

    class Meta:
        model = ErrorPost
        fields = ['exception_type']
        order_by = ['exception_type']

    def filter_exception(self, queryset, value):
        return queryset.filter(
            Q(exception_type__icontains=value) |
            Q(error_message__icontains=value))
