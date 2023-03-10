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

"""

Created Wed Jun 10 12:48:51 CEST 2020

"""

import json
import pickle
import pprint
from datetime import datetime
import time

from django.core.management.base import BaseCommand
from policy.settings import field_names, field_codes, field_description
import policy.settings as settings

"""
For each dataflow (country based)
A list of dimensions. A dimension is a dataflow selector variable. Currently the only selector is the
type of policy data being tracked
{
    "DE" : [
        {
            "DimName": 'Reference Area',
            "CodeListName": "CL_Reference_Area",
            'ActualCodes': {   'AUX1': 'Confirmed Cases',
                                     'AUX2': 'Confirmed Deaths',
                                     'C1': 'School closing',
        ]
}

"""


class Command(BaseCommand):
    help = 'Create policy dimension dictionary'
    Debug = False
    Logging = True

    start_time = time.time()
    start_timestamp = datetime.isoformat(datetime.now())
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    if Logging:
        logfile = open(settings.logfile_path, 'a')
        logfile.write('> Constructing Policy Data Dimensions \n')
        logfile.write('> Starting at: ' + str(date) + '\n')

    country_dict = settings.country_dict

    datapath = settings.ROOT_PATH + settings.DATA_PATH
    dimensions_dict_file = settings.ROOT_PATH + settings.dimensions_file

    dimensions_dict = {}
    dataflow_dict = pickle.load(open(datapath + '/dataflow_dict' + '.pkl', 'rb'))

    actual_codes = {}
    for field in field_codes:
        f_index = field_codes.index(field)
        actual_codes[field] = field_description[f_index]

    for dataflow in dataflow_dict:
        # print(dataflow_dict)
        dimensions_dict[dataflow] = []
        #
        # 1. The (trivial because only one) measurement dimension
        #
        dimension = {'DimName': 'Reference Area',
                     'DimDescription': 'Policy Measurement Reference Area',
                     'CodeListName': 'CL_Reference_Area',
                     'ActualCodes': actual_codes
                     }
        dimensions_dict[dataflow].append(dimension)

    json.dump(dimensions_dict, open(dimensions_dict_file, 'w'), sort_keys=True, indent=4, separators=(',', ': '))

    pp = pprint.PrettyPrinter(indent=4)
    if Debug:
        pp.pprint(dimensions_dict)

    if Logging:
        logfile.write("> Created  Policy Data dimensions \n")
        logfile.write("> Execution Time: %s seconds --- \n" % (time.time() - start_time))
        logfile.write(80*'=' + '\n')
        logfile.close()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully created policy dimension dictionary'))
