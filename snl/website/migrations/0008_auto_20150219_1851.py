# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20150219_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney',
            name='slug',
            field=models.SlugField(default='george-richards', unique=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 19, 18, 51, 22, 182132), auto_now=True),
            preserve_default=True,
        ),
    ]
