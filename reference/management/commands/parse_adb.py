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

from reference.settings import ADB_PATH

"""
1 Multiregional Input-Output Table 2024 None ...
2 75 economies, at current prices (industry by industry) None ...
3 In millions of US$ ...
4 None None None None None None ...
5 None None None None Agriculture, hunting, forestry, and fishing | Mining and quarrying ...
6 None None None None AUS AUS ...
7 None None None None c1 c2 ...
8 None Agriculture, hunting, forestry, and fishing AUS c1 15255.198275409259 208.59987660651302

"""

class Command(BaseCommand):
    help = 'Parse ADB spreadsheet'

    def handle(self, *args, **kwargs):
        file = ADB_PATH + 'ADB-MRIO-2024-August 2025.xlsx'
        print('Reading file')

        wb = load_workbook(file, read_only=True, data_only=True)
        ws = wb.active  # or wb[sheet_name]
        i = 1
        colsize = 3009
        col_industry_idx = None
        col_country = None
        col_industry = None
        row_industry_idx = None
        row_country = None
        row_industry = None
        for row in ws.values:
            print(i, row[1], row[2], row[3])
            # if i == 5:
            #     col_industry = row[4:colsize-4]
            # if i == 6:
            #     col_country = row[4:colsize-4]
            # if i == 7:
            #     col_industry_idx = row[4:colsize-5]
            # else:
            #     row_industry = row[1]
            #     row_country = row[2]
            #     row_industry_idx = row[3]
            #     values = row[4:colsize-4]
            i += 1
            # if i > 8:
            #     break
        wb.close()

# 2665 rows total