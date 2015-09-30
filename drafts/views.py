# coding: utf-8

from django.contrib import messages

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from .forms import DraftForm


class DraftCreateView(CreateView):
    form_class = DraftForm
    template_name = 'drafts/create.html'

    def form_valid(self, form):
        messages.info(self.request, "Thank you for adding a new exception! "
                      "Soon its solution will be available.")
        return super(DraftCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('error_posts:list')
