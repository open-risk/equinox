from django.test import TestCase

from reference.EmissionFactor import EmissionFactor


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.emissionsfactor = EmissionFactor()
        cls.emissionsfactor.save()
