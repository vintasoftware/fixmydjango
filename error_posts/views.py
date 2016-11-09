# coding: utf-8
from copy import copy

from django.views import generic
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages

from templated_email import send_templated_mail

from core.generic_views import FilterViewWithPagination
from .mixins import ErrorPostListMetadataMixin, ErrorPostMetadataMixin
from .filtersets import ExceptionSearchFilter
from .models import ErrorPost
from .forms import ErrorPostForm


class ErrorPostListView(ErrorPostListMetadataMixin, FilterViewWithPagination):
    template_name = 'error_posts/published_list.html'
    filterset_class = ExceptionSearchFilter
    paginate_by = 50

    def get_queryset(self):
        return ErrorPost.publisheds.all()


class ErrorPostDetailView(ErrorPostMetadataMixin, generic.DetailView):
    template_name = 'error_posts/detail.html'

    def get_queryset(self):
        return ErrorPost.objects.all()


class NonPublishedErrorPostListView(ErrorPostListMetadataMixin, FilterViewWithPagination):
    template_name = 'error_posts/non_published_list.html'
    filterset_class = ExceptionSearchFilter
    paginate_by = 50

    def get_queryset(self):
        return ErrorPost.non_publisheds.all()


class ErrorPostCreateView(generic.CreateView):
    template_name = 'error_posts/create.html'
    form_class = ErrorPostForm

    def get_initial(self):
        initial = {}
        for key, values in self.request.GET.items():
            initial[key] = values
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['RECAPTCHA_KEY'] = settings.RECAPTCHA_KEY
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'POST':
            data = copy(kwargs.get('data', {}))
            data['recaptcha'] = data.get('g-recaptcha-response')
            kwargs['data'] = data
            kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.info(self.request,
                      "Thank you for adding a new exception! "
                      "Soon its solution will be available.")
        error_post_url = self.request.build_absolute_uri(
            reverse('admin:error_posts_errorpost_change', args=[self.object.id]))
        send_templated_mail(
            template_name='new_error_post',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['contact@vinta.com.br'],
            context={
                'error_post': self.object,
                'error_post_url': error_post_url})
        return response

    def get_success_url(self):
        return reverse('error_posts:non_published_list')
