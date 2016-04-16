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

    template_name = 'home.html'

    def get_context_data(self):
        """Pass image to the homepage."""
        try:
            img = Photo.objects.all().order_by("?")[0]
        except IndexError:
            img = None
        return {'img': img}


class ProfileView(TemplateView):
    """Profile view."""

    template_name = 'success.html'


class LibraryView(TemplateView):
    """Library view."""

    # import pdb; pdb.set_trace()
    template_name = 'library.html'

    def get_context_data(self):
        albums = Album.objects.all()[0]
        img = Photo.objects.all()[0]
        return {'albums': albums, 'img': img}


class AlbumView(DetailView):
    """Album View."""

    template_name = 'album.html'


class PhotoView(DetailView):
    """Photo View."""

    template_name = 'photo.html'


def logout_view(request):
    """Logout."""
    logout(request)
    return redirect('homepage')


# def get_login(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = LoginForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = LoginForm()

#     return render(request, 'home.html', {'form': form})


# def logins(request):
#     """A."""
#     # import pdb; pdb.set_trace()
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)  # redirect to a success page
#             return render(request, 'home.html')
#         else:
#             # return a 'diabled account'
#             pass
#     else:
#         # return invalid login
#         pass
