# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150218_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicearea',
            name='slug',
            field=models.SlugField(default='real-estate', unique=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 0, 18, 56, 233221), auto_now=True),
            preserve_default=True,
        ),
    ]
