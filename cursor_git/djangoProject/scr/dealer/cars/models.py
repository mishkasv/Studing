import datetime
import json

from django.db import models, router
from django.db.models.deletion import Collector


class CarManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            'model').prefetch_related('dealer').prefetch_related(
            'color').prefetch_related('fueltype').prefetch_related(
            'dealer__user').prefetch_related('model__brand')

class ModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('brand')

def get_default_view_statistic():
    return {datetime.date.today().strftime('%Y'): {datetime.date.today().strftime('%Y-%m-%d'): 0}}

class Car(models.Model):
    objects=CarManager()

    STATUS = (
        ('New', 'new'),
        ('Used', 'used'),
        ('Forapart', 'for a part'),
        ('Hadbeencrashed', 'had been crashed'),
    )
    POLLUTE = (
        ('high_plus', 'A+'),
        ('high', 'A'),
        ('middle_high', 'B'),
        ('middle', 'C'),
        ('middle_low', 'D'),
        ('low_high', 'E'),
        ('low', 'F'),
        ('very_low', 'G')
    )
    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
        null=False,
        related_name='dealers_cars'
    )
    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.SET_NULL,
        null=True,
    )
    model = models.ForeignKey(
        'cars.Model_car',
        on_delete=models.CASCADE,
        related_name='car_model'
    )
    enginetype = models.CharField(max_length=50)
    pollutant_class = models.CharField(max_length=50, choices=POLLUTE, default='C')
    price = models.IntegerField()
    fueltype = models.ForeignKey(
        'cars.FuelType',
        on_delete=models.DO_NOTHING,
    )
    status = models.CharField(max_length=50, choices=STATUS, default='new')
    doors = models.IntegerField()
    capacity = models.IntegerField()
    gearcase = models.CharField(max_length=70)
    number = models.IntegerField()
    slug = models.SlugField()
    sittingplace = models.IntegerField()
    firstragistrationdate = models.DateTimeField()
    enginepower = models.IntegerField()
    status_public = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    view_for_statistic = models.JSONField(null=True,blank=True, default=get_default_view_statistic)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = "Машини"

    def __str__(self):
        return self.model.name

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = 'Колір'
        verbose_name_plural = 'Кольори'

    def __str__(self):
        return self.name


class Model_car(models.Model):
    objects = ModelManager()
    name = models.CharField(max_length=100, unique=True)
    brand = models.ForeignKey(
        'cars.Brand',
        on_delete=models.CASCADE,
        related_name='brand_of_car'
    )

    class Meta:
        verbose_name = 'Модель машини'
        verbose_name_plural = 'Моделі машин'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=70, unique=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'

    def __str__(self):
        return self.name


class Picture(models.Model):
    position = models.CharField(max_length=255)
    metadata = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)
    car = models.OneToOneField(
        Car,
        on_delete=models.CASCADE,
        related_name='picture'
    )

    def __str__(self):
        return self.car.model.name


class FuelType(models.Model):
    GAS = 'gas'
    GASOLIN = 'gasolin'
    DISEL = 'disel'
    ELECTRICAL = 'electrical'
    FUELTYPE = (
        (GAS, 'gas'),
        (DISEL, 'disel'),
        (GASOLIN, 'gasolin'),
        (ELECTRICAL, 'electrical')
    )
    name = models.CharField(max_length=20, choices=FUELTYPE, default=DISEL, unique=True)
