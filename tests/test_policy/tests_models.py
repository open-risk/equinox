# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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

from policy.models import DashBoardParams, DataFlow, DataSeries, GeoSlice


class PolicyModelTests(TestCase):

    def test_contractor_str(self):
        DashBoardParams.objects.create()
        instance = DashBoardParams.objects.get()
        self.assertEquals("1", str(instance))

    def test_dataflow_str(self):
        DataFlow.objects.create(name='test')
        instance = DataFlow.objects.get()
        self.assertEquals("test", str(instance))

    def test_dataseries_str(self):
        DataSeries.objects.create(identifier='test')
        instance = DataSeries.objects.get()
        self.assertEquals("test", str(instance))

    def test_geoslice_str(self):
        GeoSlice.objects.create(identifier='test')
        instance = GeoSlice.objects.get()
        self.assertEquals("test", str(instance))
