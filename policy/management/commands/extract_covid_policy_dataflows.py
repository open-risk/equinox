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


"""

Created Wed Jun 10 12:48:51 CEST 2020

Input csv file with policy data
Output dataflow_dict.pkl, dataflow_dict.json

0.1 version only dataflow data is country name
{
    "AD": "Andorra",
    "AE": "United Arab Emirates",
    "AF": "Afghanistan",

Updated at 2/19/21 to productionize
Updated at 9/16/24 to final dataset
"""


import json
import pickle
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
from django.core.management.base import BaseCommand

import policy.settings as settings
from policy.settings import countryISOMapping


class Command(BaseCommand):
    help = 'Extract Dataflow metadata from csv into a pickle file'
    Debug = True
    Logging = True

    BASE_DIR = Path(__file__).resolve().parent.parent

    filepath = settings.CSV_FILE_PATH
    datapath = settings.DATA_PATH

    start_time = time.time()
    start_timestamp = datetime.isoformat(datetime.now())
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    if Logging:
        logfile = open(settings.logfile_path, 'a')
        logfile.write('> Extracting Policy Data Country Dataflows \n')
        logfile.write('> Starting at: ' + str(date) + '\n')

    mydata = pd.read_csv(filepath)

    total_rows = mydata.shape[0]

    if Logging:
        logfile.write('> Found total data rows: ' + str(total_rows) + '\n')

    country_dict = {}
    dataflow_dict = {}
    count = 0

    for index, row in mydata.iterrows():

        # The data columns we will work with in this script
        country_region_code = countryISOMapping[row['CountryCode']]
        country_region = row['CountryName']

        # Some type issues of pandas
        if type(country_region_code) is float:
            country_region_code = 'NA'

        if country_region_code not in country_dict:
            country_dict[country_region_code] = country_region

        # DO WE NEED THIS
        if country_region_code not in dataflow_dict:
            # start new data flow
            dataflow_dict[country_region_code] = country_region

        count += 1
        if Debug:
            print(count)
        # if count > 1000:
        #     break

    # print(dataflow_dict)
    if Debug:
        print(country_dict)

    json.dump(dataflow_dict, open(datapath + 'dataflow_dict' + '.json', 'w'), sort_keys=True, indent=4,
              separators=(',', ': '))

    file = open(datapath + '/dataflow_dict' + '.pkl', 'wb')
    pickle.dump(obj=dataflow_dict, file=file, protocol=2)

    if Logging:
        logfile.write("> Created  datafiles/dataflow_dict.json \n")
        logfile.write("> Created  datafiles/dataflow_dict.pkl   \n")
        logfile.write("> Execution Time: %s seconds --- \n" % (time.time() - start_time))
        logfile.write(80 * '=' + '\n')
        logfile.close()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully extracted Dataflow structure from csv file'))
