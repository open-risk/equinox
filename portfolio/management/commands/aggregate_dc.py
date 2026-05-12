# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
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

from django.core.management.base import BaseCommand
from django.db.models import Sum

from portfolio.DataCenter import DataCenter, DataCenterCampus
from portfolio.Operator import Operator
from portfolio.Portfolios import ProjectPortfolio, PortfolioSnapshot
from provenance.models import Agent


class Command(BaseCommand):
    help = 'Aggregate facility data center are into campus area'

    portfolio_id = ProjectPortfolio.objects.get(name='Apple Data Center Portfolio')
    portfolio_snapshot_id = PortfolioSnapshot.objects.get(name='2023')
    agent_id = Agent.objects.get(name='IM3')
    operator_id = Operator.objects.get(operator_identifier='Apple')

    # Fetch all data centers
    # for obj in DataCenter.objects.filter(portfolio=portfolio_id):
    #     print(obj.datacenter_id, obj.datacenter_location)

    # Sum area grouped by campus key
    results = DataCenter.objects.values('campus').annotate(
        total=Sum('surface_area')
    )

    for result in results:
        DataCenterCampus.objects.filter(
            pk=result['campus']
        ).update(surface_area=result['total'])

    for result in results:
        print(f"Campus: {result['campus']}, Total: {result['total']}")

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully aggregated floor space into campuses'))
