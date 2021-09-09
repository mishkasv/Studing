from django.db import IntegrityError
from django.test import TestCase
from dealer.orders.factory import OrderFactory
from dealer.cars.factory import CarFactory


class OrderTest(TestCase):
    def setUp(self):
        self.car = CarFactory()
        pass

    def test_Order(self):
        order = OrderFactory(car = self.car, email='alish@sfls.sdoc',phone = '1111111')
        self.assertEqual(order.car, self.car)

        with self.assertRaises(IntegrityError):
            OrderFactory(car=self.car,email='alish@sfls.sdoc',phone = '2222222')
            OrderFactory(car=self.car, email='sdfsdfsfls.sdoc', phone='1111111')




# Create your tests here.
