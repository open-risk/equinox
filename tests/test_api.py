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

from equinox.serializers import ScorecardSerializer
from equinox.settings import ROOT_VIEW
from risk.Scorecard import Scorecard


# ATTN internationalization strings are not captured

class APITests(TestCase):

    def test_api_root_status_code(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)

    def test_scorecard_api_endpoint(self):
        Scorecard.objects.create(scorecard_identifier='Test')
        scorecard = Scorecard.objects.get(scorecard_identifier='Test')
        serializer = ScorecardSerializer(scorecard)
        api_link = serializer.get_link(scorecard)
        test_link = ROOT_VIEW + "/api/portfolio_data/scorecards/" + str(scorecard.pk)
        self.assertEquals(api_link, test_link)
