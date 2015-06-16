# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('error_posts', '0004_auto_20150615_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorpost',
            name='parsed_traceback',
            field=jsonfield.fields.JSONField(default={}),
            preserve_default=False,
        ),
    ]
