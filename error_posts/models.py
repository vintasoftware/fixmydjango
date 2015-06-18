# coding: utf-8

from django.db import models
from django.core.exceptions import ValidationError

from model_utils.models import TimeStampedModel
from django_markdown.models import MarkdownField
from jsonfield import JSONField
from boltons.tbutils import ParsedException

from .choices import DJANGO_VERSIONS
from .sanitize import clean_traceback, sanitize_traceback


class ErrorPost(TimeStampedModel):
    exception_type = models.CharField(max_length=80)
    error_message = models.TextField()
    traceback = models.TextField()
    sanitized_traceback = models.TextField()
    parsed_traceback = JSONField()
    django_version = models.CharField(choices=DJANGO_VERSIONS, max_length=5)
    how_to_reproduce = MarkdownField()

    def __unicode__(self):
        return '{} - Version: {} - Exception type: {}'.format(
            self.pk, DJANGO_VERSIONS[self.django_version], self.exception_type
        )

    @property
    def raised_by(self):
        if self.parsed_traceback:
            filepath = self.parsed_traceback['frames'][-1]['filepath']
            return filepath[filepath.index('django/'):]

    def clean(self):
        if self.traceback:
            try:
                clean_traceback(self.traceback)
            except ValueError as e:
                raise ValidationError({'traceback': e.message})

    def save(self, *args, **kwargs):
        self.traceback = clean_traceback(self.traceback)
        self.sanitized_traceback = sanitize_traceback(self.traceback)
        self.parsed_traceback = ParsedException.from_string(self.sanitized_traceback).to_dict()
        super(ErrorPost, self).save(*args, **kwargs)


class Answer(TimeStampedModel):
    error = models.ForeignKey(ErrorPost, related_name='answers')
    message = MarkdownField()
    date = models.DateTimeField(auto_now=True)
