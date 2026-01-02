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

from reference.PEFA import PEFASUT
from reference.settings import PEFA_PATH


class Command(BaseCommand):
    help = 'Load PEFA data into equinox'

    def handle(self, *args, **kwargs):
        # Delete existing objects
        PEFASUT.objects.all().delete()
        # Import Supply data from file
        file = PEFA_PATH + 'supply_table.csv'
        print('Reading Supply Table')
        data = pd.read_csv(file, header='infer', delimiter=',')
        print('Parsing Supply Table')
        indata = []
        for index, entry in data.iterrows():
            row = PEFASUT(
                role=0,
                year=entry['year'],
                product=entry['prod_nrg'],
                region=entry['geo'],
                industry=entry['nace_r2'],
                value=entry['value'])

            indata.append(row)
        print('Inserting Supply Table')
        PEFASUT.objects.bulk_create(indata)

        # Import Use data from file
        file = PEFA_PATH + 'use_table.csv'
        print('Reading Use Table')
        data = pd.read_csv(file, header='infer', delimiter=',')
        print('Parsing Use Table')
        indata = []
        for index, entry in data.iterrows():
            row = PEFASUT(
                role=1,
                year=entry['year'],
                product=entry['prod_nrg'],
                region=entry['geo'],
                industry=entry['nace_r2'],
                value=entry['value'])

            indata.append(row)
        print('Inserting Use Table')
        PEFASUT.objects.bulk_create(indata)
