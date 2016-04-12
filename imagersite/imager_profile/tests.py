
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory

from imager_profile.models import ImagerProfile


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(
            username='',
            email='',
        )

    def test_user_has_profile(self):
        self.assertTrue(self.user.profile)
