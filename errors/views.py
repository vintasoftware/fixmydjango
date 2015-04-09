# coding: utf-8

from django.views.generic import DetailView

from django_filters.views import FilterView

from .models import Error
from .filtersets import ErrorFilter


class ErrorListView(FilterView):
    template_name = 'errors/list.html'
    model = Error
    filterset_class = ErrorFilter

    def get_context_data(self, *args, **kwargs):
        context = super(ErrorListView, self).get_context_data(*args, **kwargs)
        errors_filter = {}

        for error in context['error_list']:
            exception_type = error.exception_type
            errors_filter[exception_type] = filter(
                lambda x: x.exception_type == exception_type,
                context['error_list']
            )

        context['errors_filter'] = errors_filter
        return context



class ErrorDetailView(DetailView):
    template_name = 'errors/detail.html'
    model = Error
