from . import models
import factory, faker, random, datetime
import factory.fuzzy
import faker_vehicle

FUELTYPE = ('gas', 'gasolin', 'dizel', 'electrical')
ENGINETYPE = ('Straight Engine', 'Inline Engine', 'Flat Engine', 'V Engine')


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Car
        #django_get_or_create = ('model',)

    color = factory.SubFactory('dealer.car.factory.ColorFactory')
    model = factory.SubFactory(
        'dealer.car.factory.ModelcarFactory',
        name = random.choice(faker_vehicle.vehicles)['Model'],
    )
    enginetype = factory.fuzzy.FuzzyChoice(ENGINETYPE)
    pollutant_class = factory.fuzzy.FuzzyChoice(models.Car.POLLUTE)
    price = factory.fuzzy.FuzzyInteger(3000,500001,100)
    fueltype = factory.fuzzy.FuzzyChoice(FUELTYPE)
    status = factory.fuzzy.FuzzyChoice(models.Car.STATUS)
    doors = factory.fuzzy.FuzzyChoice([3,5])
    capacity = factory.fuzzy.FuzzyChoice([20, 25, 30, 35, 40, 45, 50])
    gearcase = factory.fuzzy.FuzzyChoice([
        'Manual transmission',
        'Automatic transmission',
        'Continuously variable transmission',
        'Semi-automatic and dual-clutch transmissions'
    ])
    number = factory.fuzzy.FuzzyChoice([5, 6, 7])
    slug = factory.fuzzy.FuzzyText(random.choice(faker_vehicle.vehicles)['Make'] + '/' + random.choice(faker_vehicle.vehicles)['Model'])
    sittingplace = factory.fuzzy.FuzzyChoice([2, 4, 5, 6, 7, 8, 9])
    firstragistrationdate = factory.fuzzy.FuzzyDate(datetime.datetime(1990, 1, 1), datetime.datetime(2021, 6, 6))
    enginepower = factory.fuzzy.FuzzyInteger(50,500)


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Color
        django_get_or_create = ('name',)

    name = faker.Faker().color_name()


class ModelcarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Model_car
        django_get_or_create = ('name',)

    name = factory.fuzzy.FuzzyChoice(faker_vehicle.vehicles).fuzz()['Model']
    brand = factory.SubFactory('dealer.car.factory.BrandFactory')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand
        django_get_or_create = ('name',)

    name = factory.fuzzy.FuzzyChoice(faker_vehicle.vehicles).fuzz()['Make']


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Picture
        #django_get_or_create = ('url',)

    car = factory.SubFactory('dealer.car.factory.CarFactory')
    url = faker.Faker().file_path(depth=5, category='image', extension='img')
    position = 'position'
    metadata = 'metadata'
