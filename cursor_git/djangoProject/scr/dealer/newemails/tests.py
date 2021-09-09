from django.db import IntegrityError
from django.test import TestCase
from dealer.newemails.factory import NewsLetterFactory


class NewLetterTest(TestCase):
    def test_email(self):
        email="email@example"
        new_email = NewsLetterFactory(email=email)
        self.assertEqual(new_email.email,email)
        with self.assertRaises(IntegrityError):
            NewsLetterFactory(email=email)

# Create your tests here.
