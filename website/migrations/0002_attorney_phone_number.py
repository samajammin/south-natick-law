# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney',
            name='phone_number',
            field=models.BigIntegerField(default=5086511000),
            preserve_default=True,
        ),
    ]
