from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from .models import Album, Photo, AlbumForm, PhotoForm
from django.http import HttpResponseRedirect

# Create your views here.


def add_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('library_view'))
    return render(request, 'add_album.html', context={'form': form})


def add_photo(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
    form.fields['albums'].queryset = Album.objects.filter(owner__pk=request.user.pk)
    return render(request, 'add_photo.html', context={'form': form})
