# coding: utf-8

from django.views import generic

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


class ErrorPostDetailView(ErrorPostMetadataMixin, generic.DetailView):
    template_name = 'error_posts/detail.html'

    def get_queryset(self):
        return ErrorPost.publisheds.all()
