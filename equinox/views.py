# Copyright (c) 2021 Open Risk (https://www.openriskmanagement.com)
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

from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse

from portfolio.Scorecard import Scorecard
from equinox.serializers import ScorecardSerializer, ScorecardDetailSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    Returns a list of all active API endpoints in the eauinox installation, grouped by functionality


    """

    data = [
        {'Scorecard Data Endpoints':
            [
                {'scorecard': reverse('portfolio:scorecard_api', request=request, format=format)},
            ]},
    ]

    return Response(data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def scorecard_api(request):
    """
    List Scorecards (EBA Template)
    """
    if request.method == 'GET':
        scorecard = Scorecard.objects.all()
        serializer = ScorecardSerializer(scorecard, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def scorecard_detail(request, pk):
    if request.method == 'GET':
        """
        List the data of a specific Scorecard in JSON Format
        
        """
        try:
            scorecard = Scorecard.objects.get(pk=pk)
            # Get all the scorecard data from the various models
            print('1.2', scorecard.project_company.financial_ratios)
            print('1.4.1', scorecard.project_company.refinancing_risk)
            print('3.2.1', scorecard.project_company.project)

            scorecard.scorecard_data = {'1.2': 0}
            scorecard.save()

        except Scorecard.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ScorecardDetailSerializer(scorecard)
        return Response(serializer.data)
