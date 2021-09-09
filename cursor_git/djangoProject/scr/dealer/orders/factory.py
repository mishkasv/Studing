from . import models
from dealer.cars.factory import CarFactory
import factory.fuzzy


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order
        # django_get_or_create = ('firstname', 'lastname',)

    status = factory.fuzzy.FuzzyChoice(models.Order.STATUS_OF_ORDER)
    firstname = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    email = '{}.{}@exemple.com'.format(firstname, lastname)
    phone = factory.Faker('phone_number')
    car = factory.SubFactory(CarFactory)
    message = 'I wanna orders a {}'.format(car)
