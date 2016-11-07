from django.db import models


class PublishedManager(models.Manager):

    def get_queryset(self):
        qs = super(PublishedManager, self).get_queryset()
        qs = qs.filter(is_published=True)
        return qs


class NonPublishedManager(models.Manager):

    def get_queryset(self):
        qs = super(NonPublishedManager, self).get_queryset()
        qs = qs.filter(is_published=False)
        return qs
