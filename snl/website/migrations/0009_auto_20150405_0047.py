# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20150219_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 5, 0, 47, 24, 212679), auto_now=True),
            preserve_default=True,
        ),
    ]
