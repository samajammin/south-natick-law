# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('phone_extension', models.SmallIntegerField()),
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
                ('phone_number', models.BigIntegerField(blank=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
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
                ('publish_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='posts', to='website.Attorney')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticeArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('attorneys', models.ManyToManyField(related_name='practice_areas', to='website.Attorney')),
                ('posts', models.ManyToManyField(related_name='practice_areas', to='website.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='practice_area',
            field=models.ForeignKey(related_name='contacts', to='website.PracticeArea'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attorney',
            name='firm',
            field=models.ForeignKey(related_name='attorneys', to='website.Firm'),
            preserve_default=True,
        ),
    ]
