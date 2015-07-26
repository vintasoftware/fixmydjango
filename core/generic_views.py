from django.views import generic
from django.http import Http404
from django.utils.translation import ugettext as _

from django_filters.views import FilterMixin


# Based on BasedListView at django/views/generic/list.py
class FilterViewWithPagination(FilterMixin, generic.ListView):

    def get(self, request, *args, **kwargs):
        filterset_class = self.get_filterset_class()
        self.filterset = self.get_filterset(filterset_class)
        self.object_list = self.filterset.qs
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if (self.get_paginate_by(self.object_list) is not None
                    and hasattr(self.object_list, 'exists')):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
                              % {'class_name': self.__class__.__name__})
        context = self.get_context_data(filter=self.filterset)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        data = super(FilterViewWithPagination, self).get_context_data(*args, **kwargs)

        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1

        data['page_offset'] = (int(page) - 1) * self.paginate_by
        return data
