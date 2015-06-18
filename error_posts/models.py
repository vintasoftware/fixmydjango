# coding: utf-8

from django.db import models
from django.core.exceptions import ValidationError

from model_utils.models import TimeStampedModel
from django_markdown.models import MarkdownField
from jsonfield import JSONField
from boltons.tbutils import ParsedException

from .choices import DJANGO_VERSIONS
from .sanitize import clean_traceback, sanitize_traceback
from .managers import ErrorPostPublishedManager


class ErrorPost(TimeStampedModel):
    exception_type = models.CharField(max_length=80)
    error_message = models.TextField()
    traceback = models.TextField()
    sanitized_traceback = models.TextField()
    parsed_traceback = JSONField()
    django_version = models.CharField(choices=DJANGO_VERSIONS, max_length=5)
    how_to_reproduce = MarkdownField(blank=True)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    publisheds = ErrorPostPublishedManager()

    def __unicode__(self):
        return u'{} - Version: {} - Exception type: {}'.format(
            self.pk, DJANGO_VERSIONS[self.django_version], self.exception_type
        )

    def _last_frame(self):
        if self.parsed_traceback:
            return self.parsed_traceback['frames'][-1]

    @property
    def raised_by(self):
        last_frame = self._last_frame()

        if last_frame:
            filepath = last_frame['filepath']
            return filepath[filepath.index('django/'):]

    @property
    def raised_by_line(self):
        last_frame = self._last_frame()

        if last_frame:
            return last_frame['lineno']

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

    def __unicode__(self):
        return u'{} - Answer to [{}]'.format(
            self.pk, self.error
        )
