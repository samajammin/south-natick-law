# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 2, 22, 58, 752277), auto_now=True),
            preserve_default=True,
        ),
    ]
