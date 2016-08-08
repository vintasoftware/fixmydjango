# coding: utf-8

from django import forms

from .models import Draft


class DraftForm(forms.ModelForm):

    class Meta:
        model = Draft
        fields = ['author', 'email', 'exception_type',
                  'error_message', 'traceback', 'how_to_reproduce',
                  'django_version']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial')

        if initial:
            for field in initial:
                if field in self.fields:
                    self.fields[field].widget.attrs['readonly'] = True
