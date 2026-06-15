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

from reference.AIB import AIBMix
from reference.settings import AIBMIX_PATH


class Command(BaseCommand):
    help = 'Load AIB Grid Mix data into equinox'

    def handle(self, *args, **kwargs):
        # Delete existing objects
        AIBMix.objects.all().delete()
        # Import AIB Grid Mix data from file
        file = AIBMIX_PATH + 'AIB_Energy_Mix_2025.csv'
        print('Reading AIB Grid Mix Table')
        data = pd.read_csv(file, header='infer', delimiter=',', thousands=',',decimal='.')
        print('Parsing AIB Grid Mix Table')
        # Todo. This is presently hard coded
        year = 2025
        indata = []
        for index, entry in data.iterrows():
            col1 = AIBMix(
                year=year,
                country=entry['Country'],
                grid_mix_value=entry['Production'],
                grid_mix_type=0)
            col2 = AIBMix(
                year=year,
                country=entry['Country'],
                grid_mix_value=entry['Residual'],
                grid_mix_type=1)
            col3 = AIBMix(
                year=year,
                country=entry['Country'],
                grid_mix_value=entry['Supplier'],
                grid_mix_type=2)
            indata.extend([col1, col2, col3])

        print('Inserting AIB Mix Data')
        AIBMix.objects.bulk_create(indata)


