# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def fill_slug(apps, schema_editor):
    ErrorPost = apps.get_model('error_posts', 'ErrorPost')
    for error_post in ErrorPost.objects.all():
        error_post.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('error_posts', '0010_errorpost_slug'),
    ]

    operations = [
        migrations.RunPython(fill_slug, noop),
    ]
