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

import numpy as np
import pandas as pd
from django.core.management.base import BaseCommand

from django.contrib.gis.geos import Point
from portfolio.Portfolios import ProjectPortfolio, PortfolioSnapshot
from portfolio.Asset import DataCenter
from portfolio.Operator import Operator
from provenance.models import Agent

class Command(BaseCommand):
    help = 'Imports data center / operator data from the IM3 Dataset'

    # Delete existing Operator / DataCenter / Provenance objects
    ProjectPortfolio.objects.all().delete()
    PortfolioSnapshot.objects.all().delete()
    Agent.objects.all().delete()
    Operator.objects.all().delete()
    DataCenter.objects.all().delete()

    # Import data from CSV file
    # data = pd.read_csv("im3.csv", header='infer', delimiter=',')
    data = pd.read_csv("im3.clean.csv", header='infer', delimiter=',')



    """
     Create Portfolio, Portfolio Snapshot and Provenance Data

    """

    portfolio = ProjectPortfolio(name='US Data Centers')
    portfolio.save()
    portfolio_id = ProjectPortfolio.objects.get(name='US Data Centers')

    portfolio_snapshot = PortfolioSnapshot(name='2023')
    portfolio_snapshot.save()
    portfolio_snapshot_id = PortfolioSnapshot.objects.get(name='2023')

    agent = Agent(name='IM3', url='https://data.msdlive.org/records/p147s-4h760')
    agent.save()
    agent_id = Agent.objects.get(name='IM3')

    """
    Create Data Center Operators

    """

    operators = list(set(data[data['operator'].notna()]['operator'].values.tolist()))
    ops = []
    for operator in operators:
        op =  Operator(operator_identifier=operator)
        ops.append(op)
    ops.append(Operator(operator_identifier='Unknown'))
    Operator.objects.bulk_create(ops)

    """
    Create Data Centers
    id,state,state_abb,state_id,county,county_id,operator,ref,name,sqft,lon,lat,type
    """
    indata = []
    for index, entry in data.iterrows():
        name = entry['operator']
        if isinstance(name, float):
            name = 'Unknown'
        print(name)
        op = Operator.objects.get(operator_identifier=name)

        dc = DataCenter(
            portfolio=portfolio_id,
            snapshot=portfolio_snapshot_id,
            datacenter_id=entry['id'],
            datacenter_name=entry['name'],
            surface_area=entry['sqft'],
            prov_surface_area=agent_id,
            country='United States',
            county=entry['county'],
            county_id=entry['county_id'],
            state=entry['state'],
            state_id=entry['state_id'],
            state_abb=entry['state_abb'],
            datacenter_location=Point(entry['lon'],entry['lat']),
            operator=op,
            prov_operator=agent_id)

        indata.append(dc)

    DataCenter.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted data center data into db'))
