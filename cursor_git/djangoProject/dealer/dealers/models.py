from django.db import models
from django.contrib.auth.models import User


class Dealer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=False, default='example@example.com')
    city = models.ForeignKey(
        'dealers.City',
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилери'

    def __str__(self):
        return self.user.first_name


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва міста', unique=True)
    country = models.ForeignKey(
        'dealers.Country',
        on_delete=models.CASCADE,
        verbose_name='Назва країни'
    )

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва країни', unique=True)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'
