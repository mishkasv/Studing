from django.db import IntegrityError
from django.test import TestCase,Client
from dealer.cars.factory import CarFactory, ColorFactory, ModelcarFactory, BrandFactory, PictureFactory, FuelTypeFactory
from dealer.dealers.factory import UserFactory, DealerFactory
import datetime
from dealer.cars.models import Car

class TestCar(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory(username='user1')
        self.dealer = DealerFactory(user = self.user)
        self.request = Client()

    def test_FuelType(self):
        fueltype = FuelTypeFactory(name = 'gas')
        self.assertEqual(fueltype.name, 'gas')

        with self.assertRaises(IntegrityError):
            FuelTypeFactory(name='gas')

    def test_Color(self):
        color = ColorFactory(name = 'Green')
        self.assertEqual(color.name, 'Green')

        with self.assertRaises(IntegrityError):
            ColorFactory(name='Green')

    def test_Brand(self):
        brand = BrandFactory(name = 'BMW')
        self.assertEqual(brand.name, 'BMW')

        with self.assertRaises(IntegrityError):
            BrandFactory(name = 'BMW')

    def test_Model(self):
        brand = BrandFactory(name = 'BMW')
        model = ModelcarFactory(name='Q7', brand = brand)
        self.assertEqual(model.name, 'Q7')

        with self.assertRaises(IntegrityError):
            ModelcarFactory(name='Q7')


    def test_Car(self):
        today = datetime.date.today()
        color = ColorFactory(name='Green')
        model = ModelcarFactory(name='Q7')
        car = CarFactory(model = model, dealer = self.dealer, color = color,)
        self.assertEqual(car.dealer.user.username,'user1')
        self.assertEqual(car.model.name, 'Q7')
        self.assertEqual(car.color.name, 'Green')
        self.assertEqual(car.view_for_statistic, {str(today.year):{today.strftime('%Y-%m-%d'):0}})
        response = self.request.get('/api/car/1')
        self.assertEqual(Car.objects.get(id = car.id).view_for_statistic, {str(today.year):{today.strftime('%Y-%m-%d'):1}})



