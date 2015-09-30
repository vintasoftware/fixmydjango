# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('author', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('exception_type', models.CharField(max_length=255)),
                ('error_message', models.TextField()),
                ('traceback', models.TextField()),
                ('how_to_reproduce', models.TextField(blank=True)),
                ('fixed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
