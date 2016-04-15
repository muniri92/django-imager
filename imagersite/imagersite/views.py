"""Views for the Imager Site."""
from django.views.generic import TemplateView
from imager_images.models import Photo
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from imager_profile.models import ImagerProfile
# from .forms  # import NameForm
# from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


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


class ProfileView(TemplateView):
    """Profile view."""

    template_name = 'success.html'
    # import pdb; pdb.set_trace()

    # def get_context_data(self):
    #     """Pass user information to profile view page."""
    #     # try:
    #     return {'user': self.request.user}


# def success_login(request):
#     """Success for a login."""
#     return render(request, 'success.html', {})


def logout_view(request):
    logout(request)
    return redirect('homepage')



# def get_login(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = LoginForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = LoginForm()

#     return render(request, 'home.html', {'form': form})


# def logins(request):
#     """A."""
#     # import pdb; pdb.set_trace()
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)  # redirect to a success page
#             return render(request, 'home.html')
#         else:
#             # return a 'diabled account'
#             pass
#     else:
#         # return invalid login
#         pass
