from django.db import IntegrityError
from django.test import TestCase
from dealer.dealers.models import Country
from dealer.dealers.factory import CityFactory,CountryFactory,UserFactory, DealerFactory

class TestDealers(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory(username='user1')

    def test_Country(self):
        country = CountryFactory(name = 'Ukraine')
        self.assertEqual(country.name, 'Ukraine')

        with self.assertRaises(IntegrityError):
            CountryFactory(name='Ukraine').objects.create()


    def test_City(self):
        country = CountryFactory(name = 'Ukraine')
        city1 = CityFactory(country=country, name='Lviv')
        self.assertEqual(city1.name, 'Lviv')

        city2 = CityFactory(country=country, name='Kyiv')
        self.assertEqual(city2.name, 'Kyiv')

        with self.assertRaises(IntegrityError):
            CityFactory(country=country, name='Lviv')

    def test_Dealer(self):
        country = CountryFactory(name='Ukraine')
        city = CityFactory(country=country, name='Lviv')
        dealer = DealerFactory(user = self.user, city = city)
        self.assertEqual(dealer.user.username,'user1')

        city2 = CityFactory(country=country, name='Kyiv')

        with self.assertRaises(IntegrityError):
            DealerFactory(user = self.user, city =city2 )

# Create your tests here.
