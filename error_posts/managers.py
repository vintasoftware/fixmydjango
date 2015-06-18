from django.db import models


class ErrorPostPublishedManager(models.Manager):

    def get_queryset(self):
        qs = super(ErrorPostPublishedManager, self).get_queryset()
        qs = qs.filter(is_published=True)
        return qs
