# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150217_0222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='publish',
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 2, 32, 20, 963605), auto_now=True),
            preserve_default=True,
        ),
    ]
