# coding: utf-8

from django.db import models
from django.core.exceptions import ValidationError

from .choices import DJANGO_VERSIONS
from .sanitize import sanitize_traceback


class ErrorPost(models.Model):
    exception_type = models.CharField(max_length=80)
    error_message = models.TextField()
    traceback = models.TextField()
    sanitized_traceback = models.TextField()
    django_version = models.CharField(choices=DJANGO_VERSIONS, max_length=5)

    def __unicode__(self):
        return '{} - Version: {} - Exception type: {}'.format(
            self.pk, DJANGO_VERSIONS[self.django_version], self.exception_type
        )

    def clean(self):
        if self.traceback:
            try:
                sanitize_traceback(self.traceback)
            except ValueError as e:
                raise ValidationError(e.message)

    def save(self, *args, **kwargs):
        self.sanitized_traceback = sanitize_traceback(self.traceback)
        super(ErrorPost, self).save(*args, **kwargs)


class Answer(models.Model):
    error = models.ForeignKey(ErrorPost, related_name='answers')
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
