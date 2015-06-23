# coding: utf-8

from django.db import models
from django.core.exceptions import ValidationError

from model_utils.models import TimeStampedModel
from django_markdown.models import MarkdownField
from jsonfield import JSONField
from boltons.tbutils import ParsedException

from fixmydjango.sanitize_tb import clean_traceback, sanitize_traceback
from .choices import DJANGO_VERSIONS
from .managers import ErrorPostPublishedManager


class ErrorPost(TimeStampedModel):
    exception_type = models.CharField(max_length=255)
    error_message = models.TextField()
    traceback = models.TextField()
    sanitized_traceback = models.TextField()
    parsed_traceback = JSONField()
    raised_by = models.CharField(max_length=255)
    raised_by_line = models.IntegerField()
    django_version = models.CharField(choices=DJANGO_VERSIONS, max_length=5)
    how_to_reproduce = MarkdownField(blank=True)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    publisheds = ErrorPostPublishedManager()

    def __unicode__(self):
        return u'{} - Version: {} - Exception type: {}'.format(
            self.pk, DJANGO_VERSIONS[self.django_version], self.exception_type
        )

    def clean(self):
        if self.traceback:
            try:
                clean_traceback(self.traceback)
            except ValueError as e:
                raise ValidationError({'traceback': e.message})

    def _get_raised_by(self, last_frame):
        filepath = last_frame['filepath']
        return filepath[filepath.index('django/'):]

    def _get_raised_by_line(self, last_frame):
        return int(last_frame['lineno'])

    def save(self, *args, **kwargs):
        self.traceback = clean_traceback(self.traceback)
        self.sanitized_traceback = sanitize_traceback(self.traceback)
        self.parsed_traceback = ParsedException.from_string(self.sanitized_traceback).to_dict()

        last_frame = self.parsed_traceback['frames'][-1]
        self.raised_by = self._get_raised_by(last_frame)
        self.raised_by_line = self._get_raised_by_line(last_frame)

        super(ErrorPost, self).save(*args, **kwargs)


class Answer(TimeStampedModel):
    error = models.ForeignKey(ErrorPost, related_name='answers')
    message = MarkdownField()
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{} - Answer to [{}]'.format(
            self.pk, self.error
        )
