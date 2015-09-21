# coding: utf-8

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import DraftForm


class DraftCreateView(CreateView):
    form_class = DraftForm
    template_name = 'drafts/create.html'

    def get_success_url(self):
        url = '{}?error_added=1'.format(reverse('error_posts:list'))
        return url
