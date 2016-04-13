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
from django.conf.urls import url
from django.contrib import admin
from .views import logins, logout
from .views import ClassView
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'login': 'imagersite/templates/login.html'}),

    url(r'^$', ClassView.as_view(), name='homepage'),
    # url(r'^profile/', include('imager_profile.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# YOU'LL NEED THIS FOR MEDIA STUFF
# if settings.DEBUG:
# 	urlpatterns += static(settings.[**MEDIA_URL**], document_root=settings.[
# **MEDIA_URL**])
