"""Views for the Imager Site."""
from django.views.generic import TemplateView, DetailView, UpdateView
from imager_images.models import Photo, Album
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from imager_profile.models import ImagerProfile
from .forms import UserForm, ProfileForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy



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


class PhotoEdit(UpdateView):
    model = Photo
    fields = ['title', 'description', 'published']
    template_name = 'edit_photo.html'

    def get_success_url(self):
        return reverse_lazy('view_photo', kwargs={'pk': self.object.pk})


class AlbumEdit(UpdateView):
    model = Album
    fields = ['title', 'description', 'published']
    template_name = 'edit_album.html'

    def get_success_url(self):
        return reverse_lazy('view_album', kwargs={'pk': self.object.pk})


def logout_view(request):
    """Logout."""
    logout(request)
    return redirect('homepage')


def edit_profile(request):
    """Edit profile."""
    current_user = User.objects.get(pk=request.user.id)
    my_profile = current_user.profile
    if request.method == 'POST':
        form1 = ProfileForm(request.POST, instance=my_profile)
        form2 = UserForm(request.POST, instance=current_user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return render(request, 'profile.html')
    else:
        form1 = ProfileForm(instance=my_profile)
        form2 = UserForm(instance=current_user)
    return render(request, 'edit_profile.html', {"form1": form1, "form2": form2})
