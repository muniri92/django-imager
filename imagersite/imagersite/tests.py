from django.test import Client
from django.test import TestCase, override_settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from imager_images.models import Photo
from django.conf import settings
import factory
import os


class PublicViewTest(TestCase):
    """Testing views not signed in."""

    @override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'tmp'))
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
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(self.photo.file, response.context['img'].file)

    def test_login_get(self):
        response = self.client.get(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_post(self):
        response = self.client.post(reverse('login'),
                                    {'username': u'Test_User',
                                     'password': u'Secret'},
                                    follow=True)
        self.assertTemplateUsed(response, 'success.html')

    def test_login_home(self):
        """Test home view has the username after login."""
        resp = self.client.get(reverse('homepage'))
        self.assertNotContains(resp, self.User.username, status_code=200)
        self.client.login(username=u'Test_User', password=u'Secret')
        resp = self.client.get(reverse('homepage'))
        self.assertContains(resp, self.User.username, status_code=200)

    def test_profile_view(self):
        """Test profile view works as expected.

        Should only display user info when logged in.
        """
        response = self.client.get(reverse('success'))
        self.assertTemplateUsed(response, 'success.html')
        self.assertNotContains(response, self.User.username, status_code=200)
        self.assertNotContains(response, self.User.email, status_code=200)
        self.client.login(username=u'Test_User', password=u'Secret')
        response = self.client.get(reverse('success'))
        self.assertContains(response, self.User.username, status_code=200)
        self.assertContains(response, self.User.email, status_code=200)

    def test_registration_get(self):
        """Test going to registration page redirects to correct template."""

        response = self.client.get('/accounts/register/')
        self.assertTemplateUsed(response,
                                'registration/registration_form.html')

    def test_regsitration_post_good(self):
        """test post to the registration page goes through user creation.

        Tests redirects, email sending.
        """

        response = self.client.post('/accounts/register/',
                                    {'username': u'New_User',
                                     'email': u'user@gmail.com',
                                     'password1': u'testpw34',
                                     'password2': u'testpw34'},
                                    follow=True)
        # check it redirected correctly
        self.assertTemplateUsed(response,
                                'registration/registration_complete.html')
        # check an email has been sent to the new user
        mail_sent = mail.outbox[0]
        self.assertIn(u'user@gmail.com', mail_sent.to)
        # check there is a new inactive user made using form contents.
        self.assertEqual(User.objects.filter(is_active=False)[0].username,
                         u'New_User')

    def test_regsitration_post_bad(self):
        """test post to the registration page

        Redirects back if bad form entry(bad password in this case)
        """
        response = self.client.post('/accounts/register/',
                                    {'username': u'New_User',
                                     'email': u'user@gmail.com',
                                     'password1': u'bad',
                                     'password2': u'bad'},
                                    follow=True)
        self.assertTemplateUsed(response,
                                'registration/registration_form.html')


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo
