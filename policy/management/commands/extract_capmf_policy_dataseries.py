# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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


Input OECD CAPMF CSV Dump

Output DF/DF.XX.json dataseries files per dataflow directory

{
    "Dates" : []
    "Values" : []
    "Identifier"
    etc.
}

"""

import json
import time
from datetime import datetime

import pandas as pd
from django.core.management.base import BaseCommand

import policy.settings as settings
from policy.settings import countryISOMapping, country_dict


class Command(BaseCommand):
    help = 'Extract CAPMF dataseries data from csv'
    Debug = True
    Logging = False
    dataflowpath = settings.DATA_PATH + 'dataflows/'

    start_time = time.time()
    start_timestamp = datetime.isoformat(datetime.now())
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    if Logging:
        logfile = open(settings.logfile_path, 'a')
        logfile.write('> Extracting Dataseries \n')
        logfile.write('> Starting at: ' + str(date) + '\n')

    dataseries_list_file = settings.dataseries_file

    count = 0
    filepath = settings.CSV_FILE_PATH
    mydata = pd.read_csv(filepath, sep='\t')
    mydata = mydata.fillna(0.0)
    total_rows = mydata.shape[0]

    if Logging:
        logfile.write('> Found total data rows: ' + str(total_rows) + '\n')

    # store identified dataseries dicts into a list
    dataseries_group_list = []
    dataseries_dict = {}

    # Iterate over the rows of the CSV file
    # Construct a dataseries identifier from row data
    # If it exists, add measurement value to array, if not, create it

    REF_AREA = 1
    MEASURE = 2
    CLIM_ACT_POL = 3
    TITLE = 4
    TIME_PERIOD = 5
    OBS_VALUE = 6
    OBS_STATUS = 7

    for row in mydata.itertuples(index=True):

        if Debug:
            print('Extracting ', row[0])

        country_region_code = countryISOMapping[row[REF_AREA]]
        country_region = country_dict[country_region_code]

        # Some type issues of pandas
        if type(country_region_code) is float:
            country_region_code = 'NA'

        # Construct the dataflow identifier
        df_identifier = country_region_code

        # Construct the dataseries identifier
        ds_identifier = df_identifier + '.' + row[MEASURE][4:] + '.' + row[CLIM_ACT_POL][5:]

        # Compile the dataseries data

        # The observation date
        raw_date = row[TIME_PERIOD]
        observation_date = datetime.strptime(str(raw_date), '%Y').date().isoformat()

        # The observed value
        value = row[OBS_VALUE]

        # The status of the observations
        status = row[OBS_STATUS]

        # Record the aggregation level (Currently Country Only)
        aggregation_level = 'Country'

        print('DS ID: ', ds_identifier)

        # Create new dataseries object (if needed)
        if ds_identifier not in dataseries_group_list:
            # start new dataseries object
            dataseries_group_list.append(ds_identifier)
            # Create the dataseries dict
            dataseries = {'Identifier': ds_identifier, 'Dates': [], 'Values': [], 'Status': []}

            # Add data
            dataseries['Dates'].append(observation_date)
            dataseries['Values'].append(value)
            dataseries['Status'].append(status)

            # Add attributes
            title = row[TITLE]
            dataseries['TITLE'] = title
            title_compl = title + ' in ' + country_region
            dataseries['TITLE_COMPL'] = title_compl
            dataseries['REF_AREA'] = df_identifier
            dataseries['ACTIVITY'] = title
            dataseries['AGG_LEVEL'] = aggregation_level

            # Store the dataseries
            dataseries_dict[ds_identifier] = dataseries
        # or modify an existing one
        else:

            dataseries = dataseries_dict[ds_identifier]
            dataseries['Dates'].append(observation_date)
            dataseries['Values'].append(value)
            dataseries['Status'].append(status)
            title = row[TITLE]
            dataseries['TITLE'] = title
            title_compl = title + ' in ' + country_region
            dataseries['TITLE_COMPL'] = title_compl
            dataseries['REF_AREA'] = df_identifier
            dataseries['ACTIVITY'] = title
            dataseries['AGG_LEVEL'] = aggregation_level

            dataseries_dict[ds_identifier] = dataseries

        count += 1
        print(str(int(100 * count / total_rows)) + " %", end='\r')

    # Save the dataseries data into the dataflow directory structure
    for ds in dataseries_dict:
        dataseries_file = dataflowpath + ds[:2] + '/' + ds + '.json'
        json.dump(dataseries_dict[ds], open(dataseries_file, 'w'), sort_keys=True, indent=4, separators=(',', ': '))
        # print(dataseries_file)

    # Save a Dataseries summary fingerprint into a cumulative json list
    dataseries_list = []
    for ds in dataseries_dict:
        if Debug:
            print('Saving ', ds)
        ds_data = {}
        ds_data['DF_NAME'] = ds[:2]
        ds_data['FREQ'] = 'A'
        ds_data['ID'] = ds
        ds_data['REF_AREA'] = dataseries_dict[ds]['REF_AREA']
        ds_data['Status'] = 'Live'
        ds_data['TITLE'] = dataseries_dict[ds]['TITLE']
        ds_data['TITLE_COMPL'] = dataseries_dict[ds]['TITLE_COMPL']
        ds_data['UNIT'] = 'CHECK'
        ds_data['URL'] = 'https://www.equinox.com/api/policy_data'
        ds_data['ACTIVITY'] = dataseries_dict[ds]['ACTIVITY']
        ds_data['AGG_LEVEL'] = dataseries_dict[ds]['AGG_LEVEL']
        dataseries_list.append(ds_data)

    json.dump(dataseries_list, open(dataseries_list_file, 'w'), sort_keys=True, indent=4, separators=(',', ': '))

    if Logging:
        logfile.write("> Execution Time: %s seconds --- \n" % (time.time() - start_time))
        logfile.write(80 * '=' + '\n')
        logfile.close()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully extracted CAPMF dataseries from csv file'))
