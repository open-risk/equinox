# Copyright (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)
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

Input csv
Output DF/DF.XX.json dataseries file

ds_data['DF_NAME'] = ds[:2]
ds_data['FREQ'] = 'D'
ds_data['ID'] = ds
ds_data['REF_AREA'] = dataseries_dict[ds]['REF_AREA']
ds_data['Status'] = 'Live'
ds_data['TITLE'] = dataseries_dict[ds]['TITLE']
ds_data['TITLE_COMPL'] = dataseries_dict[ds]['TITLE_COMPL']
ds_data['UNIT'] = 'CHECK'
ds_data['URL'] = 'https://www.equinox.com/api/policy_data'
ds_data['ACTIVITY'] = dataseries_dict[ds]['ACTIVITY']
ds_data['AGG_LEVEL'] = dataseries_dict[ds]['AGG_LEVEL']

Updated at 2/19/21 productionize
"""

import json
from datetime import datetime
import pandas as pd
import json
import time
from django.core.management.base import BaseCommand

import policy.settings as settings
from policy.settings import countryISOMapping
from policy.settings import field_names, field_codes, field_description


class Command(BaseCommand):
    help = 'Extract policy dataseries metadata from csv'
    Debug = False
    Logging = True

    start_time = time.time()
    start_timestamp = datetime.isoformat(datetime.now())
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    if Logging:
        logfile = open(settings.logfile_path, 'a')
        logfile.write('> Extracting Dataseries \n')
        logfile.write('> Starting at: ' + str(date) + '\n')

    dataseries_list_file = settings.ROOT_PATH + settings.dataseries_file

    count = 0
    filepath = settings.CSV_FILE_PATH
    mydata = pd.read_csv(filepath)
    mydata = mydata.fillna(0)
    total_rows = mydata.shape[0]

    if Logging:
        logfile.write('> Found total data rows: ' + str(total_rows) + '\n')

    # store dataseries dicts into a list
    dataseries_group_list = []
    dataseries_dict = {}

    for index, row in mydata.iterrows():
        if Debug:
            print('Extracting ', index)

        country_region_code = countryISOMapping[row['CountryCode']]
        country_region = row['CountryName']

        # Some type issues of pandas
        if type(country_region_code) is float:
            country_region_code = 'NA'


        # The dataseries data

        # The date
        raw_date = row['Date']

        observation_date = datetime.strptime(str(raw_date), '%Y%m%d').date().isoformat()

        # Construct the dataseries identifier
        root_identifier = country_region_code

        # Extract the different dimensions of measurement
        # Construct collection of identifiers for this dataflow
        values = []
        identifier = []
        # ATTN WE FILL NAN WITH ZERO
        for field in field_names:
            values.append(row[field])
            f_index = field_names.index(field)
            identifier.append(root_identifier + '.' + field_codes[f_index])

        # Record the aggregation level (Country Only)
        aggregation_level = 'Country'

        # Create new dataseries group
        if root_identifier not in dataseries_group_list:
            # start new dataseries group
            dataseries_group_list.append(root_identifier)
            # Create the dataseries dicts
            for i in range(len(identifier)):
                dataseries = {'Identifier': identifier[i], 'Dates': [], 'Values': []}
                dataseries['Dates'].append(observation_date)
                dataseries['Values'].append(values[i])
                title = field_description[i]
                dataseries['TITLE'] = title
                title_compl = title + ' in ' + country_region
                dataseries['TITLE_COMPL'] = title_compl
                dataseries['REF_AREA'] = root_identifier
                dataseries['ACTIVITY'] = title
                dataseries['AGG_LEVEL'] = aggregation_level

                # Store the dataseries
                dataseries_dict[identifier[i]] = dataseries
        # or modify an existing one
        else:
            for i in range(len(identifier)):
                dataseries = dataseries_dict[identifier[i]]
                dataseries['Dates'].append(observation_date)
                dataseries['Values'].append(values[i])
                title = field_description[i]
                dataseries['TITLE'] = title
                title_compl = title + ' in ' + country_region
                dataseries['TITLE_COMPL'] = title_compl
                dataseries['REF_AREA'] = root_identifier
                dataseries['ACTIVITY'] = title
                dataseries['AGG_LEVEL'] = aggregation_level

                # Store the dataseries
                dataseries_dict[identifier[i]] = dataseries

        count += 1
        print(str(int(100 * count / total_rows)) + " %", end='\r')

    # Save the dataseries data into the dataflow directory structure
    for ds in dataseries_dict:
        dataseries_file = settings.ROOT_PATH + '/policy/policy_data/dataflows/' + ds[:2] + '/' + ds + '.json'
        json.dump(dataseries_dict[ds], open(dataseries_file, 'w'), sort_keys=True, indent=4, separators=(',', ': '))
        # print(dataseries_file)

    # Save the dataseries fingerprint into a cumulative json list
    dataseries_list = []
    for ds in dataseries_dict:
        if Debug:
            print('Saving ', ds)
        ds_data = {}
        ds_data['DF_NAME'] = ds[:2]
        ds_data['FREQ'] = 'D'
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
        logfile.write(80*'=' + '\n')
        logfile.close()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully extracted policy dataseries from csv file'))
