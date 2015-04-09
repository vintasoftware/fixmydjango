# coding: utf-8

from django.db import models

from .choices import DJANGO_VERSIONS


class Error(models.Model):
    exception_type = models.CharField(max_length=80)
    error_message = models.TextField()
    traceback = models.TextField()
    django_version = models.CharField(choices=DJANGO_VERSIONS, max_length=5)

    def __unicode__(self):
        return '{} - Version: {} - Exception type: {}'.format(
            self.pk, DJANGO_VERSIONS[self.django_version], self.exception_type
        )


class Answer(models.Model):
    error = models.ForeignKey(Error, related_name='answers')
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)