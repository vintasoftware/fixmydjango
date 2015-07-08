# coding: utf-8
from collections import OrderedDict

from django.db.models import Q

import django_filters

from core.filters import AllValuesFilterWithEmpty
from .models import ErrorPost


RAISED_BY_LINE_DIFF = 4


def _filter_raised_by_line(queryset, value):
    try:
        value_int = int(value)
        return (
            queryset.filter(
                raised_by_line__gte=value_int - RAISED_BY_LINE_DIFF,
                raised_by_line__lte=value_int + RAISED_BY_LINE_DIFF).
            extra(
                select=OrderedDict([('diff', 'ABS(raised_by_line - %s)')]),
                select_params=[value_int],
                order_by=['diff']
            ))
    except ValueError:
        return queryset


def _filter_search(queryset, value):
    return queryset.filter(
        Q(exception_type__icontains=value) |
        Q(error_message__icontains=value))


class ExceptionSearchFilter(django_filters.FilterSet):
    exception_type = AllValuesFilterWithEmpty(empty_label="All types")
    raised_by_line = django_filters.NumberFilter(
        action=_filter_raised_by_line,
        min_value=0)
    search = django_filters.Filter(action=_filter_search)

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
