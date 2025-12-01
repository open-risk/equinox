# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from django.test import TestCase

from reference.CPVData import CPVData
from reference.EmissionFactor import BuildingEmissionFactor
from reference.EmissionIntensity import ReferenceIntensity
from reference.GPCSector import GPCSector
from reference.NUTS3Data import NUTS3PointData


class ReferenceModelTests(TestCase):

    def test_building_emisssion_factor_str(self):
        BuildingEmissionFactor.objects.create(id=1)
        instance = BuildingEmissionFactor.objects.get()
        self.assertEqual("1", str(instance))

    def test_cpvdata_str(self):
        CPVData.objects.create(CPV_ID='test')
        instance = CPVData.objects.get()
        self.assertEqual("test", str(instance))

    def test_gpcsector_str(self):
        # ATTN MP Node
        GPCSector.objects.create(name='test', depth=1)
        instance = GPCSector.objects.get()
        self.assertEqual('GPC Sector: {}'.format('test'), str(instance))

    def test_nutspoint_data_str(self):
        point = 'POINT(0 0)'
        NUTS3PointData.objects.create(nuts_id='test', coordinates=point)
        instance = NUTS3PointData.objects.get()
        self.assertEqual("test", str(instance))

    def test_references_intensity_str(self):
        ReferenceIntensity.objects.create()
        instance = ReferenceIntensity.objects.get()
        self.assertEqual("1", str(instance))
