import factory, faker
from . import models


class NewsLetterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.NewsLetter

    email = faker.Faker().email()
