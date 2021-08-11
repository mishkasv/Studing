from django.db import models


class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

# Create your models here.
