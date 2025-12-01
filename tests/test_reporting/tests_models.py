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


from django.contrib.auth.models import User
from django.test import TestCase

from reporting.models import AggregatedStatistics, Calculation, SummaryStatistics, ResultGroup, Visualization


class ReportingModelTests(TestCase):

    def test_aggregated_statistics_str(self):
        AggregatedStatistics.objects.create()
        instance = AggregatedStatistics.objects.get()
        self.assertEqual("1", str(instance))

    def test_summary_statistics_str(self):
        SummaryStatistics.objects.create()
        instance = SummaryStatistics.objects.get()
        self.assertEqual("1", str(instance))

    def test_visualization_str(self):
        User.objects.create()
        user = User.objects.get()
        Visualization.objects.create(name='test', user_id=user)
        instance = Visualization.objects.get()
        self.assertEqual("test", str(instance))

    def test_results_group_str(self):
        User.objects.create()
        user = User.objects.get()
        ResultGroup.objects.create(user=user)
        instance = ResultGroup.objects.get()
        self.assertEqual("1", str(instance))

    def test_calculation_str(self):
        User.objects.create()
        user = User.objects.get()
        Calculation.objects.create(user=user)
        instance = Calculation.objects.get()
        self.assertEqual("1", str(instance))
