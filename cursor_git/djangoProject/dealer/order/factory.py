from . import models
from dealer.car.factory import CarFactory
import factory, faker
import factory.fuzzy


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order

    status = factory.fuzzy.FuzzyChoice(models.Order.STATUS_OF_ORDER)
    firstname = faker.Faker().first_name()
    lastname = faker.Faker().last_name()
    email = '{}.{}@exemple.com'.format(firstname, lastname)
    phone = faker.Faker().phone_number()
    car = factory.SubFactory(CarFactory)
    message = 'I wanna order a {}'.format(car)
