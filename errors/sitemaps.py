# coding: utf-8

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from .models import Answer, Error


class ErrorSitemap(Sitemap):
	changfreq = 'yearly'

	def items(self):
		return Error.objects.all()

	def location(self, item):
		return reverse('errors:detail', args=(item.id,))

	def lastmod(self, item):
		last_answer = Answer.objects.filter(error=item)
		if last_answer:
			return sorted(last_answer)[-1].date