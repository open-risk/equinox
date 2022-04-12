from django.test import TestCase

from django.test import Client


class SimpleTest(TestCase):

    def test_logged(self):
        client = Client()
        client.login(username='admin', password='admin')
        response = client.get('/policy/about')
        self.assertEqual(response.status_code, 200)

    def test_not_logged(self):
        client = Client()
        response = client.get('/policy/about')
        self.assertEqual(response.status_code, 200)
