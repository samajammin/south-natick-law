# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150219_0019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date'], 'verbose_name': 'Blog Post', 'verbose_name_plural': 'Blog Posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 0, 42, 12, 827067), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='slug',
            field=models.SlugField(unique=True, max_length=150),
            preserve_default=True,
        ),
    ]
