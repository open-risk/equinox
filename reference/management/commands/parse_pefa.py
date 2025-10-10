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

from reference.settings import PEFA_PATH

"""

Load PEFA dataset from TSV file

'freq', 'stk_flow', 'nace_r2', 'prod_nrg', 'unit', 'geo\\TIME_PERIOD', '2000 ', '2001 ', '2002 ', '2003 ', '2004 ', '2005 ', '2006 ', '2007 ', '2008 ', '2009 ', '2010 ', '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 ', '2020 ', '2021 ', '2022 ', '2023'


stk_flow: ER_USE, SUP, USE, USE_END, USE_TRS

"""


class Command(BaseCommand):
    help = 'Parse PEFA tsv and insert into Database'

    def handle(self, *args, **kwargs):
        file = PEFA_PATH + 'estat_env_ac_pefasu.tsv'
        print('Reading file')

        data = pd.read_csv(file, header='infer', sep='[,\t]', engine='python', na_values=[': m',':'])
        # print(list(data.columns.values))

        print(data.head(2))
        i = 0
        for index, entry in data.iterrows():
            if entry['stk_flow'] == 'SUP':
                # print(80*'=')
                # print(entry['freq'])
                # print(entry['unit'])
                print(entry['nace_r2'], entry['prod_nrg'], entry['geo\\TIME_PERIOD'],  entry['2023'])

            i += 1
            # if i > 3:
            #     break
