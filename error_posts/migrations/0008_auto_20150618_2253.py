# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('error_posts', '0007_errorpost_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorpost',
            name='how_to_reproduce',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
    ]
