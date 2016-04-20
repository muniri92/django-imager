from django.conf.urls import url, include
from django.contrib import admin
# from .views import logins, logout
from django.contrib.auth.decorators import login_required
from .views import add_album
from imager_images.models import Album, Photo
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import DetailView

urlpatterns = [
    url(r'^add/$', login_required(add_album), name='add_album_view'),
]