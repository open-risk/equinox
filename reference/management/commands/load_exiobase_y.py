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

import pandas as pd
from django.core.management import BaseCommand

from reference.IOData import IOMatrix, IOMatrixEntry
from reference.settings import EXIOBASE_PATH

"""
https://github.com/IndEcol/pymrio/blob/master/pymrio/mrio_models/exio3_pxp/finaldemand.tsv

Sever Final Demand Categories:
    Final consumption expenditure by households
    Final consumption expenditure by non-profit organisations serving households (NPISH)
    Final consumption expenditure by government
    Gross fixed capital formation
    Changes in inventories
    Changes in valuables
    Exports: Total (fob)
"""


class Command(BaseCommand):
    help = 'Load EXIOBASE Y.txt data file into equinox'

    def handle(self, *args, **kwargs):

        # Delete existing objects
        IOMatrixEntry.objects.all().delete()
        IOMatrix.objects.all().delete()

        Y = IOMatrix(
            io_year='2022',
            io_family='EXIOBASE 3',
            io_part='Y',
            nrows=100,
            ncols=1,
            dtype='float64')
        Y.save()

        # Import data from file
        file = EXIOBASE_PATH + 'Y.txt'
        print('Reading file')
        data = pd.read_csv(file, header=[0, 1], index_col=[0, 1], delimiter='\t')
        # Multi-index col labels -> flatten
        # First header row: Category, null, Y_Labels
        # Second header row: region, sector, null, ..., null
        data.columns = ["::".join([str(x) for x in col if x and str(x) != ""]) for col in data.columns]
        # Same with row labels
        data.reset_index(inplace=True)
        data['region::product'] = data['region'] + '::' + data['sector']
        data = data.drop(columns=['region', 'sector'])
        cols = ['region::product'] + [c for c in data.columns if c != 'region::product']
        data = data[cols]

        col_labels = list(data.columns)
        row_labels = list(data['region::product'])

        matrix = data.drop(columns=['region::product']).to_numpy()

        # 3361400 (9800, 343)
        # print(matrix.size, matrix.shape)

        indata = []
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                datum = IOMatrixEntry(
                    matrix=Y,
                    row_idx=i,
                    col_idx=j,
                    col_lbl=col_labels[j],
                    row_lbl=row_labels[i],
                    value=matrix[i, j])
                indata.append(datum)
        print('Prepared data for insert')
        IOMatrixEntry.objects.bulk_create(indata)
