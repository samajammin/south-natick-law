# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150218_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 18, 2, 53, 59, 686162), auto_now=True),
            preserve_default=True,
        ),
    ]
