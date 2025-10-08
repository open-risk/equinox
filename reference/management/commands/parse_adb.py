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
from contextlib import nullcontext

from django.core.management import BaseCommand
from openpyxl import load_workbook
import pandas as pd
import numpy as np

from reference.settings import ADB_PATH

"""
For more robustness, parsing and inserting ADB data is done in two steps

* Step 1: parse the xlsx spreadsheet and create "canonical" csv files for nodes and edges
* Step 2: bulk load nodes and edges into the database

"""


class Command(BaseCommand):
    help = 'Parse ADB spreadsheet and insert into Database'

    def handle(self, *args, **kwargs):
        file = ADB_PATH + 'ADB-MRIO-2024-August 2025.xlsx'
        print('Reading file')

        wb = load_workbook(file, read_only=True, data_only=True)
        ws = wb.active

        colsize = 3009
        zsize = 2625
        ysize = 375
        vsize = 6

        Z = np.zeros((zsize, zsize), dtype=float, order='C')
        FD = np.zeros((zsize, ysize), dtype=float, order='C')
        VA = np.zeros((vsize, zsize + ysize), dtype=float, order='C')
        X = np.zeros((zsize, 1), dtype=float, order='C')

        i = 1
        for row in ws.values:
            print(i)
            if i < 5:
                pass
            elif i == 5:
                col_industry = row[4:colsize - 4]
            elif i == 6:
                col_country = row[4:colsize - 4]
            elif i == 7:
                col_industry_idx = row[4:colsize - 5]
            elif 7 < i < 8 + zsize:
                row_industry = row[1]
                row_country = row[2]
                row_industry_idx = row[3]
                all_values = row[4:colsize - 4]
                X[i - 8] = all_values[zsize + ysize]
                Z[i - 8, :] = all_values[:zsize]
                FD[i - 8, :] = all_values[zsize:zsize + ysize]
            elif i == 8 + zsize:
                print(i, row[1], row[2], row[3])  # intermediate total
            elif 8 + zsize < i < 14 + zsize:
                all_values = row[4:colsize - 4]
                VA[i - 14 - zsize] = all_values[:-1]
            elif i == 15 + zsize:
                print(i, row[1], row[2], row[3])  # total
            else:
                pass  # last text / empty rows
            i += 1
        wb.close()

        # # Save node and edge data to csv files
        # pd.to_csv(ADB_PATH + 'nodes.csv', nodes, delimiter='\t')
        # np.savetxt(ADB_PATH + 'edges.csv', edges, delimiter='\t')

        # # Import node and edge data from csv files
        # file = ADB_PATH + 'nodes.csv'
        # nodes = pd.read_csv(file, delimiter='\t')
        # file = ADB_PATH + 'edges.csv'
        # edges = pd.read_csv(file, delimiter='\t')
