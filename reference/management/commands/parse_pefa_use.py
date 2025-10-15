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

from reference.settings import PEFA_PATH

# TODO there are empty values despite data cleaning

"""

Load PEFA dataset from TSV file

'freq', 'stk_flow', 'nace_r2', 'prod_nrg', 'unit', 'geo\\TIME_PERIOD', '2000 ', '2001 ', '2002 ', '2003 ', '2004 ', '2005 ', '2006 ', '2007 ', '2008 ', '2009 ', '2010 ', '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 ', '2020 ', '2021 ', '2022 ', '2023'

stk_flow: ER_USE, SUP, USE, USE_END, USE_TRS

"""


class Command(BaseCommand):
    help = 'Parse PEFA USE table tsv file and insert into Database'

    def handle(self, *args, **kwargs):

        # file = PEFA_PATH + 'estat_env_ac_pefasu.tsv'
        file = PEFA_PATH + 'USE.tsv'
        print('Reading USE file')

        data = pd.read_csv(file, header=None, sep='[,\t]', engine='python')
        data = data.fillna(0)
        data = data.replace(':', '0')
        data = data.replace(': ', '0')
        data = data.replace(': m', '0')
        data = data.replace('0 i', '0')
        column_index = 5
        for col in data.columns[column_index + 1:]:
            data[col] = data[col].apply(lambda x: x.split(' ')[0])
            data[col] = pd.to_numeric(data[col], errors='coerce')

        columns = ['freq', 'stk_flow', 'nace_r2', 'prod_nrg', 'unit', 'geo', '2000', '2001', '2002', '2003', '2004',
                   '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                   '2017', '2018', '2019', '2020', '2021', '2022', '2023']
        data.columns = columns

        columns = ['nace_r2', 'prod_nrg', 'geo', 'year', 'value']
        i = 0
        new_rows = []
        for index, entry in data.iterrows():
            for column, value in entry.items():
                if data.columns.get_loc(column) > 5 and value != 0.0:
                    row = {'nace_r2': entry['nace_r2'], 'prod_nrg': entry['prod_nrg'], 'geo': entry['geo'], 'year': column, 'value': value}
                    # out.loc[len(out)] = row_values
                    new_rows.append(row)
            i += 1
            print(i)
            # if i > 100:
            #     break
        out = pd.DataFrame(new_rows, columns=columns)
        out.to_csv(PEFA_PATH + 'use_table.csv', index=False)
