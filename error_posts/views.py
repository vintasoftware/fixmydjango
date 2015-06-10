# coding: utf-8

from django.views.generic import DetailView

from django_filters.views import FilterView

from .models import ErrorPost
from .filtersets import ErrorPostFilter


class ErrorPostListView(FilterView):
    template_name = 'error_posts/list.html'
    model = ErrorPost
    filterset_class = ErrorPostFilter

    def get_context_data(self, **kwargs):
        context = super(ErrorPostListView, self).get_context_data(**kwargs)
        exception_list = context['errorpost_list'].values('exception_type')
        description = map(lambda x: x['exception_type'], exception_list)
        context['metatags'] = {'description': ','.join(description)}

        return context


class ErrorPostDetailView(DetailView):
    template_name = 'error_posts/detail.html'
    model = ErrorPost

    def get_context_data(self, **kwargs):
        context = super(ErrorPostDetailView, self).get_context_data(**kwargs)
        error_post = context['errorpost']
        description = '{} , {}'.format(
            error_post.exception_type, error_post.error_message)
        context['metatags'] = {'description': description}

        return context
