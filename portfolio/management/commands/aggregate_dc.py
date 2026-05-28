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

from portfolio.DataCenter import DataCenterCampus
from portfolio.Operator import Operator
from portfolio.Portfolios import ProjectPortfolio, PortfolioSnapshot
from provenance.models import Agent


class Command(BaseCommand):
    help = 'Aggregate facility data center area into campus area'

    portfolio_id = ProjectPortfolio.objects.get(name='Apple Data Center Portfolio')
    portfolio_snapshot_id = PortfolioSnapshot.objects.get(name='2023')
    agent_id = Agent.objects.get(name='IM3')
    operator_id = Operator.objects.get(operator_identifier='Apple')

    selection = DataCenterCampus.objects.filter(portfolio=portfolio_id, snapshot=portfolio_snapshot_id).annotate(sum_surface_area=Sum('datacenter__surface_area'))

    for campus in selection:
        campus.surface_area = campus.sum_surface_area

    DataCenterCampus.objects.bulk_update(selection, ['surface_area'], batch_size=1000)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully aggregated floor space into campuses'))
