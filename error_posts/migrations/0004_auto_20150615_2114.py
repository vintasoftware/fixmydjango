# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('error_posts', '0003_auto_20150615_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='message',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
