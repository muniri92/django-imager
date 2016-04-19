from django.test import Client
from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from imager_images.models import Photo
from .settings import BASE_DIR
import factory
import os

TMP_MEDIA_ROOT = 'tmp/media/'


class PublicViewTest(TestCase):
    """Testing views."""

    @override_settings(MEDIA_ROOT=os.path.join(BASE_DIR, 'tmp'))
    def setUp(self):
        self.client = Client()
        self.User = User.objects.create_user(u'Test_User', password=u'Secret')
        self.photo = PhotoFactory(owner=self.User,
                                  file=factory.django.ImageField())
        self.photo.save()

    def test_home(self):
        """Test the home view has the proper template and contains an expected image."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('home.html', response.templates[0].name)
        self.assertEqual(self.photo.file, response.context['img'].file)


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo
