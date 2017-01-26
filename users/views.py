from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth

from braces.views import AnonymousRequiredMixin

from .forms import SignUpForm


class SignUpView(AnonymousRequiredMixin, generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('error_posts:list')

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        user = auth.authenticate(email=form.cleaned_data['email'],
                                 password=form.cleaned_data['password'])
        auth.login(self.request, user)
        return valid
