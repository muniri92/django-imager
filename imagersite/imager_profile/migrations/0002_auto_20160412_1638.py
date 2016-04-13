# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagerprofile',
            name='friends',
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='friends',
            field=models.ManyToManyField(max_length=3, related_name='friend_of', to='imager_profile.ImagerProfile'),
        ),
    ]
