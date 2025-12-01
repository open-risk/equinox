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

from risk.ActivityBarrier import ActivityBarrier
from risk.Scenarios import Scenario
from risk.Scorecard import Scorecard
from risk.Workflows import Limitflow


class RiskModelTests(TestCase):

    def test_activity_barrier_str(self):
        ActivityBarrier.objects.create(barrier_identifier='test', barrier_description='')
        instance = ActivityBarrier.objects.get()
        self.assertEqual("test", str(instance))

    def test_scenario_str(self):
        Scenario.objects.create(name='test')
        instance = Scenario.objects.get()
        self.assertEqual("test", str(instance))

    def test_scorecard_str(self):
        Scorecard.objects.create(scorecard_identifier='test')
        instance = Scorecard.objects.get()
        self.assertEqual("test", str(instance))

    def test_limitflow_str(self):
        User.objects.create()
        user = User.objects.get()
        Limitflow.objects.create(name='test', user_id=user)
        instance = Limitflow.objects.get()
        self.assertEqual("test", str(instance))
