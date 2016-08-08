# coding: utf-8

from django.db import models

from model_utils.models import TimeStampedModel

from error_posts.choices import DJANGO_VERSIONS


class Draft(TimeStampedModel):
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    exception_type = models.CharField(max_length=255)
    error_message = models.TextField()
    traceback = models.TextField()
    how_to_reproduce = models.TextField(blank=True)
    django_version = models.CharField(choices=DJANGO_VERSIONS, max_length=5, blank=True)
    fixed = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{} - {}'.format(self.pk, self.exception_type)
