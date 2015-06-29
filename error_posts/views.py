# coding: utf-8

from django.views.generic import DetailView

from django_filters.views import FilterView

from .models import ErrorPost
from .filtersets import ExceptionSearchFilter


class ErrorPostListView(FilterView):
    template_name = 'error_posts/list.html'
    filterset_class = ExceptionSearchFilter

    def get_queryset(self):
        return ErrorPost.publisheds.all()

    def get_context_data(self, **kwargs):
        context = super(ErrorPostListView, self).get_context_data(**kwargs)
        exception_list = context['errorpost_list'].values('exception_type')
        description = map(lambda x: x['exception_type'], exception_list)
        context['metatags'] = {'description': ','.join(description)}

        return context


class ErrorPostDetailView(DetailView):
    template_name = 'error_posts/detail.html'

    def get_queryset(self):
        return ErrorPost.publisheds.all()

    def get_context_data(self, **kwargs):
        context = super(ErrorPostDetailView, self).get_context_data(**kwargs)
        error_post = context['errorpost']
        description = '{} , {}'.format(
            error_post.exception_type, error_post.error_message)
        context['metatags'] = {'description': description}

        return context
