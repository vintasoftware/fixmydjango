# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ErrorPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exception_type', models.CharField(max_length=80)),
                ('error_message', models.TextField()),
                ('traceback', models.TextField()),
                ('django_version', models.CharField(max_length=5, choices=[(b'1.2', b'1.2'), (b'1.3', b'1.3'), (b'1.4', b'1.4'), (b'1.5', b'1.5'), (b'1.6', b'1.6'), (b'1.7', b'1.7'), (b'1.8', b'1.8')])),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='error',
            field=models.ForeignKey(related_name='answers', to='error_posts.ErrorPost'),
        ),
    ]
