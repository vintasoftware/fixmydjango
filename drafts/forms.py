import requests

from django import forms
from django.conf import settings

from core.utils import get_client_ip
from drafts.models import Draft


class DraftForm(forms.ModelForm):
    recaptcha = forms.CharField()

    class Meta:
        model = Draft
        fields = ['author', 'email', 'exception_type',
                  'error_message', 'traceback', 'how_to_reproduce',
                  'django_version']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial')

        if initial:
            for field in initial:
                if field in self.fields:
                    self.fields[field].widget.attrs['readonly'] = True

    def clean_recaptcha(self):
        code = self.cleaned_data['recaptcha']
        if not getattr(settings, 'RECAPTCHA_SECRETE_KEY'):
            ip_address = get_client_ip(self.request)
            response = requests.post('https://www.google.com/recaptcha/api/siteverify',
                                     data={'secret': settings.RECAPTCHA_SECRETE_KEY,
                                           'response': code,
                                           'remoteip': ip_address})
            res = response.json()
            if not res['success']:
                raise forms.ValidationError('Invalid Recaptcha')

        return code

