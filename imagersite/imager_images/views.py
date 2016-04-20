from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Album, Photo, AlbumForm, PhotoForm

# Create your views here.

# class AddAlbumView(CreateView):
#     model = Album
#     # exclude = ['date_published', 'owner']
#     fields = ['cover', 'title', 'description', 'published']
#     template_name = "add_album.html"]


def add_album(request):
    form = AlbumForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
    return render(request, 'add_album.html', context={'form': form})


def add_photo(request):
    form = PhotoForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
    return render(request, 'add_photo.html', context={'form': form})

