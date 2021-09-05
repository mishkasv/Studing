from . import models
import datetime, pytz
import factory.fuzzy
from faker_vehicle.vehicle_dict import vehicles

url_car = open('scr/dealer/cars/picture.txt', 'r').readlines()
vehicle_model = [v['Model'] for v in vehicles]
vehicle_category = [v['Category'] for v in vehicles]
vehicle_make = [v['Make'] for v in vehicles]
FUELTYPE = ('gas', 'gasolin', 'disel', 'electrical')
ENGINETYPE = ('Straight Engine', 'Inline Engine', 'Flat Engine', 'V Engine')


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Car
        # django_get_or_create = ('model',)

    dealer = factory.SubFactory('dealer.dealers.factory.DealerFactory')
    color = factory.SubFactory('dealer.cars.factory.ColorFactory')
    model = factory.SubFactory('dealer.cars.factory.ModelcarFactory')
    enginetype = factory.fuzzy.FuzzyChoice(ENGINETYPE)
    pollutant_class = factory.fuzzy.FuzzyChoice(models.Car.POLLUTE)
    price = factory.fuzzy.FuzzyInteger(3000, 500001, 100)
    fueltype = factory.SubFactory('dealer.cars.factory.FuelTypeFactory')
    status = factory.fuzzy.FuzzyChoice(models.Car.STATUS)
    doors = factory.fuzzy.FuzzyChoice([3, 5])
    capacity = factory.fuzzy.FuzzyChoice([20, 25, 30, 35, 40, 45, 50])
    gearcase = factory.fuzzy.FuzzyChoice([
        'Manual transmission',
        'Automatic transmission',
        'Continuously variable transmission',
        'Semi-automatic and dual-clutch transmissions'
    ])
    number = factory.fuzzy.FuzzyChoice([5, 6, 7])
    slug = factory.fuzzy.FuzzyChoice(vehicle_model).fuzz() + '/' + factory.fuzzy.FuzzyChoice(vehicle_make).fuzz()
    sittingplace = factory.fuzzy.FuzzyChoice([2, 4, 5, 6, 7, 8, 9])
    firstragistrationdate = factory.fuzzy.FuzzyDateTime(
        datetime.datetime(1990, 1, 1, tzinfo=pytz.UTC),
        datetime.datetime(2021, 6, 6, tzinfo=pytz.UTC))
    enginepower = factory.fuzzy.FuzzyInteger(50, 500)


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Color
        # django_get_or_create = ('name',)

    name = factory.Faker('color_name')


class ModelcarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Model_car
        # django_get_or_create = ('name',)

    name = factory.fuzzy.FuzzyChoice(vehicle_model)
    brand = factory.SubFactory('dealer.cars.factory.BrandFactory')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand
        # django_get_or_create = ('name',)

    name = factory.fuzzy.FuzzyChoice(vehicle_make)


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Picture
        # django_get_or_create = ('url',)

    car = factory.SubFactory('dealer.cars.factory.CarFactory')
    url = factory.fuzzy.FuzzyChoice(url_car)
    position = 'position'
    metadata = 'metadata'


class FuelTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.FuelType
        # django_get_or_create = ('name',)

    name = factory.fuzzy.FuzzyChoice(FUELTYPE)
