from . import models
import factory, faker

faker_data = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = faker_data.first_name()
    last_name = faker_data.last_name()
    username = faker_data.user_name()
    email = faker_data.email()


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Dealer

    user = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'title %s' % n)
    email = faker_data.email()
    city = factory.SubFactory('dealer.dealers.factory.CityFactory')


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.City

    name = faker_data.city()
    country = factory.SubFactory('dealer.dealers.factory.CountryFactory')


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Country

    name = faker_data.country()
    code = faker_data.country_code()
