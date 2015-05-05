# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20150504_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 22, 13, 3, 456463), auto_now=True),
            preserve_default=True,
        ),
    ]
