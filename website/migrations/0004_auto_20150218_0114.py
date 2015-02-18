# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150217_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=django_markdown.models.MarkdownField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 1, 14, 35, 273466), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='name',
            field=models.CharField(unique=True, max_length=120),
            preserve_default=True,
        ),
    ]
