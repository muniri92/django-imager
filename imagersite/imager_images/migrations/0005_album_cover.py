# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import imager_images.models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20160414_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(null=True, upload_to=imager_images.models.user_directory_path),
        ),
    ]
