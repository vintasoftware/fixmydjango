# coding: utf-8

from django import forms

from .models import Draft


class DraftForm(forms.ModelForm):

    class Meta:
        model = Draft
        fields = ['author', 'email', 'exception_type',
                  'error_message', 'traceback', 'how_to_reproduce']
