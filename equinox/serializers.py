# Copyright (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)
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


from rest_framework import serializers
from equinox.settings import ROOT_VIEW
from risk_analysis.Scorecard import Scorecard


class ScorecardSerializer(serializers.ModelSerializer):
    """
    Serialize Scorecard Inventory
    """
    link = serializers.SerializerMethodField()

    class Meta:
        model = Scorecard
        fields = ('id', 'scorecard_identifier', 'link')

    def get_link(self, obj):
        link = ROOT_VIEW + "/api/portfolio_data/scorecards/" + str(obj.pk)
        return link


class ScorecardDetailSerializer(serializers.ModelSerializer):
    """
    Serialize Scorecard Data
    """

    class Meta:
        model = Scorecard
        fields = '__all__'
