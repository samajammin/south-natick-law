# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attorney',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.BigIntegerField(default=5086511000)),
                ('phone_extension', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('submission_date', models.DateField(auto_now_add=True, null=True)),
                ('points', models.SmallIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.BigIntegerField(null=True)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('llp', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=75)),
                ('street_address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.IntegerField()),
                ('domain', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('slug', models.SlugField(unique=True, max_length=150)),
                ('published', models.BooleanField(default=True)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(default=datetime.datetime(2015, 2, 17, 2, 22, 41, 349954), auto_now=True)),
                ('author', models.ForeignKey(related_name='posts', to='website.Attorney')),
            ],
            options={
                'ordering': ['-published_date'],
                'verbose_name': 'Blog Entry',
                'verbose_name_plural': 'Blog Entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticeArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('attorneys', models.ManyToManyField(related_name='practice_areas', to='website.Attorney')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='website.PracticeArea'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='practice_area',
            field=models.ForeignKey(related_name='contacts', to='website.PracticeArea'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='website.Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attorney',
            name='firm',
            field=models.ForeignKey(related_name='attorneys', to='website.Firm'),
            preserve_default=True,
        ),
    ]
