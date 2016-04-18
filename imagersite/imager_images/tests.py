# """Test that Photo and Album models work as expected."""
# from __future__ import unicode_literals
# from django.db.models.fields.files import ImageFieldFile
# from django.test import TestCase, override_settings
# from django.conf import settings
# from django.utils import timezone
# from .models import Photo, Album, PUBLISHED
# import factory
# import random

# TMP_MEDIA_ROOT = 'tmp/media/'


# class UserFactory(factory.django.DjangoModelFactory):
#     """Test using factory for user model.."""

#     class Meta:
#         """Establish User model as the product of this factory."""

#         model = settings.AUTH_USER_MODEL
#         django_get_or_create = ('username',)

#     first_name = factory.Faker('first_name')
#     last_name = factory.Faker('last_name')
#     email = factory.Faker('email')
#     username = factory.LazyAttribute(
#         lambda object: ''.join((object.first_name, object.last_name)))
#     password = factory.PostGenerationMethodCall('set_password', 'password')


# class PhotoFactory(factory.django.DjangoModelFactory):
#     """Creates Photo models for testing."""

#     class Meta:
#         """Assign Photo model as product of factory."""

#         model = Photo

#     owner = factory.SubFactory(UserFactory, username='UserDude')
#     title = factory.Faker('sentence')
#     description = factory.Faker('text')
#     published = random.choice(PUBLISHED)


# class AlbumFactory(factory.django.DjangoModelFactory):
#     """Creates Album models for testing."""

#     class Meta:
#         """Assign Album model as product of factory."""

#         model = Album

#     title = factory.Faker('sentence')
#     description = factory.Faker('text')
#     published = random.choice(PUBLISHED)
#     owner = factory.SubFactory(UserFactory, username='UserDude')


# class OnePhotoOrAlbumCase(object):
#     """Base case testing same named attributes of single Album or Photo."""

#     def test_instance_exists(self):
#         """Test that the instance set up from the factory does exist."""
#         self.assertTrue(self.instance)

#     def test_instance_pk(self):
#         """Test that new Album or Photo has an integer primary key."""
#         self.assertIsInstance(self.instance.pk, int)
#         self.assertTrue(self.instance.pk)

#     def test_instance_has_title(self):
#         """Check that photo/album has its title attribute."""
#         self.assertTrue(self.instance.title)

#     def test_instance_has_desc(self):
#         """Check that photo/album has its description attribute."""
#         self.assertTrue(self.instance.description)

#     def test_instance_has_mod_date(self):
#         """Check that photo/album date_modified is a datetime before now."""
#         self.assertGreater(timezone.now(), self.instance.date_modified)

#     def test_instance_published(self):
#         """Check that photo/album published is in correct choices set."""
#         self.assertIn(self.instance.published, PUBLISHED)


# @override_settings(MEDIA_ROOT=TMP_MEDIA_ROOT)
# class OnePhotoCase(TestCase, OnePhotoOrAlbumCase):
#     """Test case for a single Photo."""

#     def setUp(self):
#         """Add one Photo to the database for testing."""
#         # import pdb; pdb.set_trace()
#         self.instance = PhotoFactory.create()

#     def test_photo_has_up_date(self):
#         """Check that photo uploaded_date is a datetime before now."""
#         self.assertGreater(timezone.now(), self.instance.date_uploaded)

#     def test_init_no_albums(self):
#         """Check that Photo initializes with no albums."""
#         self.assertFalse(self.instance.albums.count())

#     def test_file_false(self):
#         """Check that file doesn't exists."""
#         self.assertFalse(self.instance.file)

#     def test_file_type(self):
#         """Check that file exists."""
#         self.assertIsInstance(self.instance.file, ImageFieldFile)


# @override_settings(MEDIA_ROOT=TMP_MEDIA_ROOT)
# class OneAlbumCase(TestCase, OnePhotoOrAlbumCase):
#     """Test case for a single Album."""

#     def setUp(self):
#         """Add one Album to the database for testing."""
#         self.instance = AlbumFactory.create()

#     def test_init_no_photos(self):
#         """Check that Album initializes with no photos."""
#         self.assertFalse(self.instance.photos.count())

#     def test_album_has_created_date(self):
#         """Check that album date_created is a datetime before now."""
#         self.assertGreater(timezone.now(), self.instance.date_uploaded)
