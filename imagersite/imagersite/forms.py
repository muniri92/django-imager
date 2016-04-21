"""Docstring."""
from django.forms import ModelForm
from imager_profile.models import ImagerProfile
# from django.conf import settings
from django.contrib.auth.models import User


class UserForm(ModelForm):
    """Form to edit profile."""

    class Meta:
        """Docstring."""

        model = User
        fields = ["first_name", "last_name", "email", "password"]


class ProfileForm(ModelForm):
    """Form to edit profile."""

    class Meta:
        """Docstring."""

        model = ImagerProfile
        exclude = ["user", "friends"]
