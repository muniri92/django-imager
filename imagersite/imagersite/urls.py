"""imagersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from .views import logins, logout
from django.contrib.auth.decorators import login_required

from .views import ClassView, ProfileView, LibraryView, PhotoEdit, AlbumEdit, edit_profile
from imager_images.models import Album, Photo
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import DetailView
from imager_api.views import APIPhotoList


urlpatterns = [
    url(r'^api/', login_required(APIPhotoList.as_view())),
    url(r'^admin/', admin.site.urls),
    url(r'^$', ClassView.as_view(), name='homepage'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': "homepage"}, name='logout'),
    url(r'^accounts/profile/$', ProfileView.as_view(), name="profile"),
    url(r'^accounts/profile/edit/$', edit_profile, name="edit_profile"),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^images/library/$', login_required(LibraryView.as_view()), name='library_view'),
    url(r'^images/photo/(?P<pk>[0-9]+)/edit$',
        login_required(PhotoEdit.as_view()), name='edit_photo'),
    url(r'^images/album/(?P<pk>[0-9]+)/edit$',
        login_required(AlbumEdit.as_view()), name='edit_album'),
    url(r'^images/album/(?P<pk>[0-9]+)/$',
        login_required(DetailView.as_view(model=Album,
                                          template_name="album.html")),
        name='view_album'),
    url(r'^images/photo/(?P<pk>[0-9]+)/$',
        login_required(DetailView.as_view(model=Photo,
                                          template_name="photo.html")),
        name='view_photo'),
    url(r'^images/', include('imager_images.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
