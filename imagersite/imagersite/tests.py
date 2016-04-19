from django.test import Client
from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from imager_images.models import Photo
from .settings import BASE_DIR
import factory
import os

TMP_MEDIA_ROOT = 'tmp/media/'


class PublicViewTest(TestCase):
    """Testing views not signed in."""

    @override_settings(MEDIA_ROOT=os.path.join(BASE_DIR, 'tmp'))
    def setUp(self):
        self.client = Client()
        self.User = User.objects.create_user(username=u'Test_User',
                                             email=u'test@test.com',
                                             password=u'Secret')
        self.photo = PhotoFactory(owner=self.User,
                                  file=factory.django.ImageField())
        self.photo.save()

    def test_home(self):
        """Test the home view has the proper template and contains an expected image."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(self.photo.file, response.context['img'].file)

    def test_login_get(self):
        response = self.client.get('/accounts/login', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/accounts/login/', status_code=301)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_post(self):
        response = self.client.post('/accounts/login',
                                    {'username': u'Test_User',
                                     'password': u'Secret'},
                                    follow=True)

    def test_login_home(self):
        """Test home view has the username after login."""
        resp = self.client.get('/')
        self.assertNotContains(resp, self.User.username, status_code=200)
        self.client.login(username=u'Test_User', password=u'Secret')
        resp = self.client.get('/')
        self.assertContains(resp, self.User.username, status_code=200)

    def test_profile_view(self):
        """Test profile view works as expected.

        Should only display user info when logged in.
        """
        response = self.client.get('/accounts/profile', follow=True)
        self.assertTemplateUsed(response, 'success.html')
        self.assertNotContains(response, self.User.username, status_code=200)
        self.assertNotContains(response, self.User.email, status_code=200)
        self.client.login(username=u'Test_User', password=u'Secret')
        response = self.client.get('/accounts/profile', follow=True)
        self.assertContains(response, self.User.username, status_code=200)
        self.assertContains(response, self.User.email, status_code=200)

    def test_registration_get(self):
        """Test going to registration page redirects to correct template."""

        response = self.client.get('/accounts/register/')
        self.assertTemplateUsed(response,
                                'registration/registration_form.html')

    def test_regsitration_post(self):
        """test post to the registration page goes through user creation."""

        response = self.client.post('/accounts/register',
                                    {'username': u'New_User',
                                     'email': u'email@email.com',
                                     'password1': u'testpw',
                                     'password2': u'testpw'},
                                    follow=True)
        import pdb; pdb.set_trace()



class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo
