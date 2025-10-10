# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
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
from django.core.management import BaseCommand

from reference.IOGraph import IOMatrix, IOMatrixEntry
from reference.settings import EXIOBASE_PATH


class Command(BaseCommand):
    help = 'Load EXIOBASE x.txt data file into equinox'

    def handle(self, *args, **kwargs):

        # Delete existing objects if appropriate

        # IOMatrixEntry.objects.all().delete()
        # IOMatrix.objects.all().delete()

        # Import metadata from file
        file = EXIOBASE_PATH + 'metadata.json'
        metadata = json.load(open(file))

        x = IOMatrix(
            io_year='2022',
            io_family='EXIOBASE 3',
            io_part='X',
            nrows=9800,
            ncols=3,
            dtype='float64',
            metadata=metadata
        )
        x.save()

        # Import matrix data from file
        file = EXIOBASE_PATH + 'x.txt'
        print('Reading file')
        data = pd.read_csv(file, header='infer', delimiter='\t')

        for index, entry in data.iterrows():
            print(entry['region'], entry['sector'], entry['indout'])

        indata = []

        for index, entry in data.iterrows():
            datum = IOMatrixEntry(
                matrix=x,
                row_idx=index,
                col_idx=0,
                col_lbl='X',
                row_lbl=entry['region'] + "::" + entry['sector'],
                value=entry['indout'])

            indata.append(datum)

        IOMatrixEntry.objects.bulk_create(indata)
