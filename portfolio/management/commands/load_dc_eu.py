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

import json
import pandas as pd
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

from portfolio.DataCenter import DataCenter
from portfolio.Operator import Operator
from portfolio.Portfolios import ProjectPortfolio, PortfolioSnapshot
from provenance.models import Agent


class Command(BaseCommand):
    help = 'Imports data center / operator data from the euDataCenterDB Dataset'

    # Import data from GeoJSON file

    filename = 'dc.json'

    """
    Create Data Center Operators if they do not exist already

    """

    operators = []
    with open(filename) as f:
        data = json.load(f)
        if isinstance(data.get('features'), list):
            features = data.get('features')
            for feature in features:
                props = feature['properties']
                if 'operator' in props.keys():
                    operators.append(props['operator'])
        operators = list(set(operators))
    f.close()

    for operator in operators:
        op = Operator.objects.get_or_create(operator_identifier=operator)
    Operator.objects.get_or_create(operator_identifier='Unknown')


    """
     Create Portfolio, Portfolio Snapshot and Provenance Data

    """

    portfolio_id, portfolio_created = ProjectPortfolio.objects.get_or_create(name='EU Data Centers')
    portfolio_snapshot_id, snapshot_created = PortfolioSnapshot.objects.get_or_create(name='2025')
    agent_id, agent_created = Agent.objects.get_or_create(name='OSM')


    """
    Create Data Centers
    """

    indata = []
    with open(filename) as f:
        data = json.load(f)
        if isinstance(data.get('features'), list):
            features = data.get('features')
            for feature in features:
                props = feature['properties']

                if 'operator' in props.keys():
                    operator_name = props['operator']
                else:
                    operator_name = 'Unknown'
                op = Operator.objects.get(operator_identifier=operator_name)

                if 'name' in props.keys():
                    data_center_name = props['name']
                else:
                    data_center_name = 'Unknown'

                dc = DataCenter(
                    portfolio=portfolio_id,
                    snapshot=portfolio_snapshot_id,
                    datacenter_id=props['@id'],
                    datacenter_name=data_center_name,
                    country=props['country'],
                    operator=op,
                    prov_operator=agent_id)
        
                indata.append(dc)

    print(len(indata))
    # DataCenter.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted data center data into db'))
