# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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

from reference.CPVData import CPVData, CPV_LEVEL_DICT


class Command(BaseCommand):
    help = 'Load common procurement vocabulary as a csv file into equinox'

    def handle(self, *args, **kwargs):
        # Delete existing objects
        CPVData.objects.all().delete()

        # Import data from file
        data = pd.read_csv("cpvdata.csv", header='infer', delimiter=',')

        """
        CPV_ID, short_code, level, description
    
        """
        indata = []

        for index, entry in data.iterrows():
            co = CPVData(
                CPV_ID=entry['CPV_ID'],
                description=entry['description'],
                short_code=entry['short_code'],
                level=CPV_LEVEL_DICT[entry['level']])

            indata.append(co)

        CPVData.objects.bulk_create(indata)
