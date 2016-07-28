# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drafts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='django_version',
            field=models.CharField(blank=True, max_length=5, choices=[('1.2', '1.2'), ('1.3', '1.3'), ('1.4', '1.4'), ('1.5', '1.5'), ('1.6', '1.6'), ('1.7', '1.7'), ('1.8', '1.8'), ('1.9', '1.9')]),
        ),
    ]
