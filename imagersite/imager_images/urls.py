from django.conf.urls import url, include
from django.contrib import admin
# from .views import logins, logout
from django.contrib.auth.decorators import login_required
from .views import add_album, add_photo
from imager_images.models import Album, Photo
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import DetailView

urlpatterns = [
    url(r'^albums/add/$', login_required(add_album), name='add_album_view'),
    url(r'^photos/add/$', login_required(add_photo), name='add_photo_view'),
]