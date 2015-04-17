# coding: utf-8

from django.views.generic import DetailView

from django_filters.views import FilterView

from .models import Error
from .filtersets import ErrorFilter


class ErrorListView(FilterView):
    template_name = 'errors/list.html'
    model = Error
    filterset_class = ErrorFilter

    def get_context_data(self, **kwargs):
        context = super(ErrorListView, self).get_context_data(**kwargs)
        exception_list = []
        exception_list = context['error_list'].values('exception_type')
        description =  map(lambda x: x['exception_type'], exception_list)
        context['metatags'] = {'description': ','.join(description)}

        return context



class ErrorDetailView(DetailView):
    template_name = 'errors/detail.html'
    model = Error

    def get_context_data(self, **kwargs):
        context = super(ErrorDetailView, self).get_context_data(**kwargs)
        error = context['error']
        description = '{} , {}'.format(
            error.exception_type, error.error_message)
        context['metatags'] = {'description': description}

        return context
