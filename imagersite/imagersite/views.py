"""Views for the Imager Site."""
from django.views.generic import TemplateView, DetailView
from imager_images.models import Photo, Album
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from imager_profile.models import ImagerProfile
# from .forms  # import NameForm
# from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


class ClassView(TemplateView):
    """Home page template."""

    template_name = 'base.html'

    def get_context_data(self):
        """Pass image to the homepage."""
        try:
            img = Photo.objects.all().order_by("?")[0]
        except IndexError:
            img = None
        return {'img': img}


class ProfileView(TemplateView):
    """Profile view."""

    template_name = 'profile.html'


class LibraryView(TemplateView):
    """Library view."""

    template_name = 'library.html'

    def get_context_data(self):
        """Return a dictionary of the photo instances."""
        albums = Album.objects.all()
        return {'albums': albums}


def logout_view(request):
    """Logout."""
    logout(request)
    return redirect('homepage')
