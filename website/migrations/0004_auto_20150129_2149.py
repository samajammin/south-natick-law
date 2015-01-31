# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150129_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicearea',
            name='name',
            field=models.CharField(max_length=120),
            preserve_default=True,
        ),
    ]
