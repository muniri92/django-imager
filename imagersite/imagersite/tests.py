"""Test the login and auth views."""
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase


class TestProfile(TestCase):
    """Test views class."""

    def setUp(self):
        """Set up a user profile for testing."""
        # import pdb; pdb.set_trace()
        self.user = User.objects.create_user(
            'milkytown',
            'milky@town.com',
            'password'
        )
        self.user.save()
        self.not_authorized = Client()

    # TEST STATUS CODES
    def test_home(self):
        """Test the status code for a non authorized user."""
        resp = self.not_authorized.get('/').status_code
        self.assertEquals(resp, 200)

    def test_registration(self):
        """Test the status code for registration."""
        resp = self.not_authorized.get('/accounts/register').status_code
        self.assertEquals(resp, 301)

    def test_login(self):
        """Test the status code for a non authorized user."""
        resp = self.not_authorized.get('/accounts/login').status_code
        self.assertEquals(resp, 301)

    def test_profile(self):
        """Test the status code for a non authorized user."""
        resp = self.not_authorized.get('/accounts/success').status_code
        self.assertEquals(resp, 404)
