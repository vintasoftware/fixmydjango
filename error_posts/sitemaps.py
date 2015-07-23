# coding: utf-8

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from .models import Answer, ErrorPost


class ErrorPostSitemap(Sitemap):
    changfreq = 'daily'
    priority = 0.5

    def items(self):
        return ErrorPost.publisheds.all()

    def location(self, item):
        return reverse('error_posts:detail', args=(item.id,))

    def lastmod(self, item):
        try:
            return item.answers.latest('modified').modified
        except Answer.DoesNotExist:
            return item.modified
