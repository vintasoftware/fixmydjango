# coding: utf-8

from django.views.generic import DetailView

from core.generic_views import FilterViewWithPagination
from .mixins import ErrorPostListMetadataMixin, ErrorPostMetadataMixin
from .filtersets import ExceptionSearchFilter
from .models import ErrorPost


class ErrorPostListView(ErrorPostListMetadataMixin, FilterViewWithPagination):
    template_name = 'error_posts/list.html'
    filterset_class = ExceptionSearchFilter
    paginate_by = 50

    def get_queryset(self):
        return ErrorPost.publisheds.all()

    def get_context_data(self, **kwargs):
        context = super(ErrorPostListView, self).get_context_data(**kwargs)
        context['error_added'] = self.request.GET.get('error_added')
        return context


class ErrorPostDetailView(ErrorPostMetadataMixin, DetailView):
    template_name = 'error_posts/detail.html'

    def get_queryset(self):
        return ErrorPost.publisheds.all()
