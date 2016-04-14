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
# from django.contrib.auth.decorators import login_required

from .views import ClassView, success_login
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ClassView.as_view(), name='homepage'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    # url(r'^account/profile$', login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/profile/$', success_login, name="success"),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    # {'login': 'imagersite/templates/login.html'}),
    # url(r'^account/profile/', include('imager_profile.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
