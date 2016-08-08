from django.contrib import messages
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.conf import settings

from templated_email import send_templated_mail

from .forms import DraftForm


class DraftCreateView(CreateView):
    form_class = DraftForm
    template_name = 'drafts/create.html'

    def get_initial(self):
        initial = {}
        for key, values in self.request.GET.items():
            initial[key] = values
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.info(self.request,
                      "Thank you for adding a new exception! "
                      "Soon its solution will be available.")
        draft_url = self.request.build_absolute_uri(
            reverse('admin:drafts_draft_change', args=[self.object.id]))
        send_templated_mail(
            template_name='new_draft',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['contact@vinta.com.br'],
            context={
                'draft': self.object,
                'draft_url': draft_url})

        return response

    def get_success_url(self):
        return reverse('error_posts:list')
