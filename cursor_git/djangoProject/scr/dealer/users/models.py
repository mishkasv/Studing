from django.conf import settings
from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# class ExtUser(AbstractUser):
#     is_dealer = models.BooleanField(default=False)
#     avatar = models.ImageField(null=True, blank=True, verbose_name='Profile picture')
# # Create your models here.
from rest_framework.authtoken.models import Token

class CustomToken(Token):

    is_active = models.BooleanField(default=False)

    class Meta:
        proxy = 'rest_framework.authtoken' in settings.INSTALLED_APPS
        abstract = 'rest_framework.authtoken' in settings.INSTALLED_APPS
        verbose_name = "token"



