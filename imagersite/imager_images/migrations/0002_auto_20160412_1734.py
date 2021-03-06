# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 17:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='date_published',
        ),
        migrations.AddField(
            model_name='album',
            name='published',
            field=models.CharField(choices=[('private', 'Private'), ('shared', 'Shared'), ('public', 'Public')], default='Public', max_length=30),
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.CharField(default=datetime.datetime(2016, 4, 12, 17, 34, 17, 92350, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='published',
            field=models.CharField(choices=[('private', 'Private'), ('shared', 'Shared'), ('public', 'Public')], default='Public', max_length=30),
        ),
    ]
