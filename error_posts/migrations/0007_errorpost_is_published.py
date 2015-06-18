# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('error_posts', '0006_errorpost_how_to_reproduce'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorpost',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
