# coding: utf-8

from django.db import models
from django.core.exceptions import ValidationError

from model_utils.models import TimeStampedModel
from django_markdown.models import MarkdownField
from jsonfield import JSONField
from boltons.tbutils import ParsedException
from autoslug import AutoSlugField
from autoslug.settings import slugify

from fixmydjango.sanitize_tb import clean_traceback, sanitize_traceback
from .choices import DJANGO_VERSIONS, ERROR_POST_DATA_CAME_FROM
from .managers import PublishedManager, NonPublishedManager


def _generate_slug(error_post):
    return '{}-{}'.format(
        slugify(error_post.raised_by[7:-3].replace('/', '-')),
        slugify(error_post.exception_type))


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
    slug = AutoSlugField(populate_from=_generate_slug, unique=True)
    data_came_from = models.CharField(choices=ERROR_POST_DATA_CAME_FROM, max_length=255)

    objects = models.Manager()

    def __unicode__(self):
        return u'{} - {} - {}'.format(
            self.pk, self.raised_by, self.exception_type
        )

    def clean(self):
        if self.traceback:
            try:
                clean_traceback(self.traceback)
            except ValueError as e:
                raise ValidationError({'traceback': e})

    def _get_raised_by(self):
        last_frame = self.parsed_traceback['frames'][-1]
        filepath = last_frame['filepath']
        return filepath[filepath.index('django/'):]

    def _get_raised_by_line(self):
        last_frame = self.parsed_traceback['frames'][-1]
        return int(last_frame['lineno'])

    def save(self, *args, **kwargs):
        self.traceback = clean_traceback(self.traceback)
        self.sanitized_traceback = sanitize_traceback(self.traceback)
        self.parsed_traceback = ParsedException.from_string(
            self.sanitized_traceback
        ).to_dict()
        self.raised_by = self._get_raised_by()
        self.raised_by_line = self._get_raised_by_line()
        super(ErrorPost, self).save(*args, **kwargs)


class ErrorPostPublished(ErrorPost):
    objects = PublishedManager()

    class Meta:
        proxy = True


class ErrorPostNonPublished(ErrorPost):
    objects = NonPublishedManager()

    class Meta:
        proxy = True


class Answer(TimeStampedModel):
    error = models.ForeignKey(ErrorPost, related_name='answers')
    message = MarkdownField()
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{} - Answer to [{}]'.format(
            self.pk, self.error
        )
