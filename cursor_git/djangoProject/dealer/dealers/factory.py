from . import models
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User
        django_get_or_create = ('username',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('username')
    email = factory.Faker('email')


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Dealer
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'title %s' % n)
    email = factory.Faker('email')
    city = factory.SubFactory('dealer.dealers.factory.CityFactory')


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.City
        django_get_or_create = ('name',)

    name = factory.Faker('city')
    country = factory.SubFactory('dealer.dealers.factory.CountryFactory')


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Country
        django_get_or_create = ('name',)

    name = factory.Faker('country')
    code = factory.Faker('country_code')
