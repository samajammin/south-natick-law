# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20150405_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default="http://upload.wikimedia.org/wikipedia/commons/0/01/Fenway_from_Legend's_Box.jpg", upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image_alt_text',
            field=models.CharField(default='Fenway', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 2, 47, 49, 808749), auto_now=True),
            preserve_default=True,
        ),
    ]
