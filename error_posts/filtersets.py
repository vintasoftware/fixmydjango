# coding: utf-8

from django.db.models import Q

import django_filters

from core.filters import AllValuesFilterWithEmpty
from .models import ErrorPost


class ExceptionSearchFilter(django_filters.FilterSet):
    exception_type = AllValuesFilterWithEmpty(empty_label="All types")
    search = django_filters.MethodFilter(action='filter_exception')

    class Meta:
        model = ErrorPost
        fields = ['exception_type', 'raised_by', 'raised_by_line',
                  'django_version', 'search']

    def __init__(self, *args, **kwargs):
        super(ExceptionSearchFilter, self).__init__(*args, **kwargs)

        # allow empty in django_version
        django_version_choices = self.filters['django_version'].extra['choices']
        self.filters['django_version'].extra['choices'] = (
            (('', 'All'),) + django_version_choices)

    def filter_exception(self, queryset, value):
        return queryset.filter(
            Q(exception_type__icontains=value) |
            Q(error_message__icontains=value))
