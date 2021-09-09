from django import forms
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from dealer.users.models import CustomToken


class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, label=_('Username'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))

    remember_me = forms.BooleanField(required=False, initial=False, label=_('Remember me'))

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data['username']
        password = cleaned_data['password']

        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError(_('User not found'))
        token, created = CustomToken.objects.get_or_create(user=user)
        token.is_active = True
        token.save()
        self.cleaned_data['user'] = user
