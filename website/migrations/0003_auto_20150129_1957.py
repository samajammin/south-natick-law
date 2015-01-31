# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_attorney_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicearea',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='website.PracticeArea'),
            preserve_default=True,
        ),
    ]
