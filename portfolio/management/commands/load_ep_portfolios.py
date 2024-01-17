# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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


class Command(BaseCommand):
    help = 'Imports Equator Principles portfolio data'

    ep_data = json.load(open('bt_ep.json', 'r'))
    ps = []  # portfolio snapshot (year)
    po = []  # portfolio (bank)

    for entry in ep_data:
        ps.append(entry['Year'])
        po.append(entry['Bank'])
    ps = list(set(ps))
    po = list(set(po))

    # Delete existing objects
    ProjectPortfolio.objects.all().delete()
    PortfolioSnapshot.objects.all().delete()

    indata = []
    for e in ps:
        snap = PortfolioSnapshot(name=e)
        indata.append(snap)
    PortfolioSnapshot.objects.bulk_create(indata)

    indata = []
    for e in po:
        portfolio = ProjectPortfolio(name=e)
        indata.append(portfolio)
    ProjectPortfolio.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted equator principles portfolio data into db'))
