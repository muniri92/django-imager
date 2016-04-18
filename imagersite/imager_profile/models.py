# # -*- coding: utf-8 -*-
"""User Profile Model."""
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


class ActiveUserManager(models.Manager):
    u"""Convenience manager which returns only active profiles."""

    def get_queryset(self):
        u"""B."""
        qs = super(ActiveUserManager, self).get_queryset()
        return qs.filter(user__is_active=True)


PHOTOGRAPHY_TYPES = [
    ('portrait', 'Portrait'),
    ('landscape', 'Landscape'),
    ('sports', 'Sports'),
]
US_REGIONS = [
    ('pnw', 'Pacific Northwest'),
    ('ne', 'New England'),
    ('ma', 'Mid-Atlantic'),
    ('se', 'Southeast'),
    ('mw', 'Midwest'),
    ('ds', 'Deep South'),
    ('sw', 'Southwest'),
    ('cf', 'California'),
    ('ak', 'Alaska'),
    ('hi', 'Hawaii'),
]


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    u"""A."""

    def __str__(self):
        """WTF is this?."""
        return self.user.username

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile'
    )

    camera_type = models.CharField(
        max_length=250,
    )

    type_of_photography = models.CharField(
        max_length=128,
        choices=PHOTOGRAPHY_TYPES,
    )

    region = models.CharField(
        max_length=3,
        choices=US_REGIONS,
    )

    friends = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='friend_of',
        max_length=255,
    )

    # friends = models.CharField(
    #     max_length=3,
    # )

    objects = models.Manager()
    active = ActiveUserManager()

    @property
    def is_active(self):
        u"""Are users active or not."""
        return self.user.is_active

