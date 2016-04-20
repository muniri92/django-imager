from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Album, Photo

# Create your views here.

class AddAlbumView(CreateView):
    model = Album
    exclude = ['date_published', 'owner']
    fields = ['cover', 'title', 'description']
    template_name = "add_album.html"
