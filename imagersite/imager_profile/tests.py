"""Tests for the Imager Profile."""
from __future__ import unicode_literals
from django.test import TestCase
from django.conf import settings
import factory
from django.db.models import QuerySet, Manager
from .models import ImagerProfile
import random


class UserFactory(factory.django.DjangoModelFactory):
    """Test using factory for user model.."""

    class Meta:
        """Establish User model as the product of this factory."""

        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('username',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    username = factory.LazyAttribute(
        lambda object: ''.join((object.first_name, object.last_name)))
    password = factory.PostGenerationMethodCall('set_password', 'password')


class OneUserCase(TestCase):
    """Base case setting up one User."""

    def setUp(self):
        """Set up User models."""
        self.user = UserFactory.create()


class BuiltUserCase(TestCase):
    """Single user not saved to database."""

    def setUp(self):
        """Set up user stub (NOT SAVED)."""
        self.user = UserFactory.build(
            username='',
            email='',
        )

    def test_user_not_saved(self):
        """Ensure set up user has not been saved yet."""
        self.assertIsNone(self.user.id)

    def test_init_imager_profile(self):
        """Ensure set up user has not been saved yet."""
        profile = ImagerProfile(user=self.user)
        self.assertIs(profile, self.user.profile)


class BasicUserProfileCase(OneUserCase):
    """Simple test case for Photos."""

    def test_user_has_profile(self):
        """Test that newly created User does have a profile attached."""
        self.assertTrue(self.user.profile)

    def test_profile_pk(self):
        """Test that newly created User's profile has a primary key."""
        self.assertIsInstance(self.user.profile.pk, int)
        self.assertTrue(self.user.profile.pk)

    def test_profile_is_active(self):
        """Test that profile of new User is active."""
        self.assertTrue(self.user.profile.is_active)

    def test_profile_active_manager(self):
        """Test that active attr is a Manager class."""
        self.assertIsInstance(ImagerProfile.active, Manager)

    def test_profile_active_query(self):
        """Test that active manager can give a QuerySet."""
        self.assertIsInstance(ImagerProfile.active.all(), QuerySet)

    def test_active_count(self):
        """Test that counting the active manager returns expected int."""
        self.assertEqual(ImagerProfile.active.count(), 1)


class ManyUserCase(TestCase):
    """Test cases where many Users are registered."""

    def setUp(self):
        """Add multiple users to tests."""
        self.user_batch = UserFactory.create_batch(50)

    def test_active_count(self):
        """Confirm that users count are correct."""
        self.assertEqual(ImagerProfile.active.count(), 50)

    def test_many_deleted(self):
        """Confirm that count is changed when multiple users are deleted."""
        for user in random.sample(self.user_batch, 50 // 2):
            user.delete()
        self.assertEqual(ImagerProfile.active.count(), 50 // 2)


class DeletedUserCase(OneUserCase):
    """Base case setting up one User, and then deleting it."""

    def setUp(self):
        """Set up User models."""
        super(DeletedUserCase, self).setUp()
        self.user.delete()

    def test_no_profile_pk_after_delete(self):
        """Test that profile is deleted with User, losing its primary key."""
        self.assertIsNone(self.user.profile.pk)

    def test_profile_is_active_false(self):
        """Test that profile of deleted User is not active."""
        self.assertTrue(self.user.profile.is_active)

    def test_active_count(self):
        """Test that counting the active manager returns expected int."""
        self.assertFalse(ImagerProfile.active.count())

    def test_active_not_contains(self):
        """Test that counting the active manager returns expected int."""
        # import pdb; pdb.set_trace()
        self.assertNotIn(self.user, ImagerProfile.active.all())
