"""Views for the Imager Site."""
from django.views.generic import TemplateView
from imager_images.models import Photo
from django.contrib.auth import authenticate, login
from django.shortcuts import render


def logins(request):
    """A."""
    # import pdb; pdb.set_trace()
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)  # redirect to a success page
            return render(request, 'home.html')
        else:
            # return a 'diabled account'
            pass
    else:
        # return invalid login
        pass


def logout(request):
    logout(request)
    # redirect to success page


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






