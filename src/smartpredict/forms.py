from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from smartpredict.models import UserDetails


class EditProfileForm(UserChangeForm):
    #template_name='/something/else'

    class Meta:
        model = UserDetails
        fields = (
            'first_name',
            'last_name',
            'forex_api',
        )