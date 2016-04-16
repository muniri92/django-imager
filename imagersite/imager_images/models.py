# # -*- coding: utf-8 -*-
"""Photo and Album Models."""
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

PUBLISHED = [
    ('private', 'Private'),
    ('shared', 'Shared'),
    ('public', 'Public'),
]


def user_directory_path(instance, filename):
    u"""File will be uploaded to MEDIA_ROOT/user_<id>/<filename>."""
    return 'user_{0}/{1}'.format(instance.owner.id, filename)


@python_2_unicode_compatible
class Photo(models.Model):
    u"""
    Photo represents an individual picture uploaded by a user.

    It will contain the image file itself, plus metadata about that file.
    Photos are owned by a single Imager user.

    Meta-data should include a title and a description, a date_uploaded,
    date_modified and date_published field.

    You should also have a ‘published’ field
    which takes one of several possible values
    (‘private’, ‘shared’, ‘public’).
    """

    file = models.ImageField(
        upload_to=user_directory_path
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='photos',
    )

    albums = models.ManyToManyField(
        'Album',
        related_name='photos'
    )

    title = models.CharField(max_length=100)

    description = models.CharField(max_length=500)

    date_uploaded = models.DateTimeField(auto_now_add=True)

    date_modified = models.DateTimeField(auto_now=True)

    date_published = models.DateTimeField(null=True)

    published = models.CharField(
        max_length=30,
        choices=PUBLISHED,
        default='Public',
    )

    def __str__(self):
        u"""WTF."""
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    u"""Albums."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='albums'
    )

    cover = models.ImageField(
        upload_to=user_directory_path,
        null=True,
    )

    # cover = models.ForeignKey(
    #     'Photo',
    #     on_delete=models.CASCADE,
    #     related_name='covered_albums',
    #     null=True,
    #     default=None
    # )

    title = models.CharField(max_length=100)

    description = models.CharField(max_length=500)

    date_uploaded = models.DateTimeField(auto_now_add=True)

    date_modified = models.DateTimeField(auto_now=True)

    published = models.CharField(
        max_length=30,
        choices=PUBLISHED,
        default='Public',
    )

    def __str__(self):
        u"""WTF."""
        return self.title
