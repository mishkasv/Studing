from http import HTTPStatus

from django.test import TestCase, Client

from django.urls import reverse


class StatusViewTests(TestCase):
    client = Client()

    def test_status_view(self):
        response = self.client.get('/status/')
        assert response.status_code == HTTPStatus.OK
