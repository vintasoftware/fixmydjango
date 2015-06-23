# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('error_posts', '0008_auto_20150618_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorpost',
            name='raised_by',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='errorpost',
            name='raised_by_line',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='errorpost',
            name='exception_type',
            field=models.CharField(max_length=255),
        ),
    ]
