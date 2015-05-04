# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20150416_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 4, 17, 31, 40, 965246), auto_now=True),
            preserve_default=True,
        ),
    ]
