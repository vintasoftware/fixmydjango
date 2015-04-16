# coding: utf-8

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from .models import Error


class ErroSitemap(Sitemap):
	changfreq = 'yearly'

	def items(self):
		return Error.objects.all()

	def location(self, item):
		return reverse('errors:detail', args=(item.id,))