from django.test import TestCase
from . import factory


class CarModelsTests(TestCase):

    def test_cartable(self):
        car1 = factory.CarFactory()
        car2 = factory.CarFactory()
        car3 = factory.CarFactory()
        print(car1, car2, car3)
        assert True == False
