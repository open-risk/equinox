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

from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse

from risk_analysis.Scorecard import Scorecard
from equinox.serializers import ScorecardSerializer, ScorecardDetailSerializer
from portfolio.Revenue import Revenue
from portfolio.Sponsor import Sponsor
from portfolio.Contractor import Contractor
from portfolio.Operator import Operator
from portfolio.Stakeholders import Stakeholders
from portfolio.Loan import Loan

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    Returns a list of all active API endpoints in the Equinox installation, grouped by functionality


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
            project_company = scorecard.project_company
            project = project_company.project
            revenue = Revenue.objects.filter(project_company=project_company).first()
            sponsor = Sponsor.objects.filter(project_company=project_company).first()
            operator = Operator.objects.filter(project_company=project_company).first()
            contractor = Contractor.objects.filter(project_company=project_company).first()
            stakeholders = Stakeholders.objects.filter(project_company=project_company).first()
            loan = Loan.objects.filter(project_company=project_company).first()

            scorecard_data = {
                "1.1": revenue.market_conditions,
                "1.2": project_company.financial_ratios,
                "1.3": revenue.stress_analysis,
                "1.4.1": project_company.refinancing_risk,
                "1.4.2": loan.amortisation_schedule,
                "1.4.3": loan.foreign_exchange_risk,
                "2.1": stakeholders.political_risk,
                "2.2": stakeholders.force_majeure_risk,
                "2.3": stakeholders.government_support,
                "2.4": stakeholders.legal_and_regulatory_risk,
                "2.5": stakeholders.project_approval_risk,
                "2.6": stakeholders.legal_regime,
                "3.1": project.design_and_technology_risk,
                "3.2.1": contractor.permitting_and_siting,
                "3.2.2": contractor.type_of_construction_contract,
                "3.2.3": project.completion_risk,
                "3.2.4": contractor.completion_guarantees_and_liquidated_damages,
                "3.2.5": contractor.contractor_track_record,
                "3.3.1": operator.o_and_m_contract,
                "3.3.2": operator.operator_track_record,
                "3.4.1": revenue.revenue_contract_robustness,
                "3.4.2": revenue.offtake_contract_case,
                "3.4.3": revenue.no_offtake_contract_case,
                "3.5.1": revenue.supply_cost_risks,
                "3.5.2": revenue.reserve_risk,
                "4.1": sponsor.sponsor_financial_strength,
                "4.2": sponsor.sponsor_track_record,
                "4.3": sponsor.sponsor_support,
                "5.1": project_company.assignment_of_contracts_and_accounts,
                "5.2": project_company.pledge_of_assets,
                "5.3": project_company.control_over_cash_flow,
                "5.4": project_company.covenant_package,
                "5.5": project_company.reserve_funds
            }
            scorecard.scorecard_data = scorecard_data
            scorecard.save()

        except Scorecard.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ScorecardDetailSerializer(scorecard)
        return Response(serializer.data)
