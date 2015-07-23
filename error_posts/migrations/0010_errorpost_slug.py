# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import error_posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('error_posts', '0009_auto_20150623_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorpost',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', populate_from=error_posts.models._generate_slug, editable=False),
            preserve_default=False,
        ),
    ]
