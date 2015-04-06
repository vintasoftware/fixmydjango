# coding: utf-8

from django.views.generic import ListView

from .models import Error


class ErrorListView(ListView):
	template_name = 'errors/list.html'
	model = Error
