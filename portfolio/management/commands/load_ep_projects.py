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

import json

from django.core.management.base import BaseCommand

from portfolio.Portfolios import ProjectPortfolio, PortfolioSnapshot
from portfolio.Project import Project
from portfolio.ProjectCategory import ProjectCategory


class Command(BaseCommand):
    help = 'Imports Equator Principles project data'

    ep_data = json.load(open('bt_ep.json', 'r'))

    # Delete existing objects
    Project.objects.all().delete()

    indata = []
    for e in ep_data:
        category = ProjectCategory.objects.get(name=e['Sector'])
        portfolio = ProjectPortfolio.objects.get(name=e['Bank'])
        snap = PortfolioSnapshot.objects.get(name=e['Year'])
        print(category.name, portfolio.name, snap.name)
        project = Project(project_identifier=e['Project'],
                          project_category=category,
                          snapshot=snap,
                          portfolio=portfolio
                          )
        indata.append(project)
    Project.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted equator principles portfolio data into db'))
