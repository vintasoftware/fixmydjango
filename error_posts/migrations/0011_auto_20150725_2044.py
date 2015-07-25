# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from autoslug.utils import generate_unique_slug
import error_posts.models


def fill_slug(apps, schema_editor):
    ErrorPost = apps.get_model('error_posts', 'ErrorPost')
    for error_post in ErrorPost.objects.all():
        error_post.slug = generate_unique_slug(
            field=ErrorPost._meta.get_field('slug'),
            instance=error_post,
            slug=error_posts.models._generate_slug(error_post),
            manager=None)
        error_post.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('error_posts', '0010_errorpost_slug'),
    ]

    operations = [
        migrations.RunPython(fill_slug, noop),
        migrations.AlterField(
            model_name='errorpost',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=error_posts.models._generate_slug, unique=True, editable=False),
        ),
    ]
