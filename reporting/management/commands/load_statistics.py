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

import pandas as pd
from django.core.management import BaseCommand

from reporting.models import SummaryStatistics


class Command(BaseCommand):
    help = 'Load summary statistics as a csv file into equinox'

    def handle(self, *args, **kwargs):
        # Delete existing objects
        SummaryStatistics.objects.all().delete()

        mode = 'Multicurrency'
        mode = 'Singlecurrency'

        # Import data from file
        data = pd.read_csv("reporting/fixtures/country_summary_statistics.csv", header='infer', delimiter=',')

        """
        fields = ('year', 'country', 'sector', 'contracts', 'currency', 'value_total')
    
        """
        indata = []

        if mode == 'Multicurrency':
            for index, entry in data.iterrows():
                co = SummaryStatistics(
                    year=entry['year'],
                    country=entry['country'],
                    sector=entry['cpa'],
                    contracts=entry['contract_count'],
                    currency=entry['currency'],
                    value_total=entry['value_total'])
                indata.append(co)

        elif mode == 'Singlecurrency':
            for index, entry in data.iterrows():
                country = None
                if entry['country'] == 'UK':
                    country = 'GB'
                else:
                    country = entry['country']
                co = SummaryStatistics(
                    year=entry['year'],
                    country=country,
                    sector=entry['cpa'],
                    contracts=entry['contract_count'],
                    currency='EUR',
                    value_total=entry['total_value'])
                indata.append(co)

        SummaryStatistics.objects.bulk_create(indata)
