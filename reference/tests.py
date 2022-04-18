from django.test import TestCase, Client

from reference.EmissionFactor import EmissionFactor


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.emissionsfactor = EmissionFactor()
        cls.emissionsfactor.save()

    def test_logged(self):
        client = Client()
        client.login(username='admin', password='admin')
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
