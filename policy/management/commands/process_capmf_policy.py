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

import json
import math
import time
from datetime import datetime

import numpy as np
from django.core.management.base import BaseCommand
from scipy import stats

import policy.settings as settings
# The field names as they are in the CSV header
from policy.capmf_settings import field_codes, field_description, field_description_long, field_code_list, field_type

"""
Starting with downloaded data
{
    "Dates" : []
    "Values" : []
    "Status" : []
    "Identifier"
    etc.
}

Produce an updated JSON dictionary from each downloaded / extracted dataseries json file
{
    "Title": "GP AE Abu Dhabi",
    "Values": [19997374.81, 18222694.97, 17420941.66, 16218983.09, 15905939.33,
    "Metrics": {"Orders": 8, "Max": 21706797.74, "T": 4512955.39, "Frequency": "M", "Q75": 19619744.39, "Median": 18003532.99, "Min": 4512955.39, "T-1": 4603992.16, "FirstDate": "2002-01-01", "ObsCount": 179, "T-2": 4678552.62, "Mean": 16726940.325, "LastDate": "2016-11-01", "Q25": 15734007.27, "Vol": 4248327.84, "T-3": 4785115.37},
    "Definition": "Grocery and Pharmacy Mobility in United Arab Emirates Abu Dhabi",
    "Identifier": "AE.Abu_Dhabi.GP",
    "Df_Name": "AE",
    "LastDate": "2016-11-01",
    "Delta": [0, -1774679.8399999999, -801753.3099999987, -1201958.5700000003,
    "PDelta: : [0, -1774679.8399999999, -801753.3099999987, -1201958.5700000003,
    "Dates": ["2002-01-01", "2002-02-01", "2002-03-01", "2002-04-01", "2002-05-01",
    "Frequency": "D".
    "Geometry_1D": {"Current": }
    "Units" : "% decline from baseline"
}

# The original downloaded dataseries catalog is augmented with an indicator of processing status

STATUS INDICATORS
- Valid -> sufficient data for presentation
- Discontinued -> Has not been updated (SET THRESHOLD)
- Stale -> Values do not change
- Insufficient -> insufficient data
- Invalid -> Cannot parse
"""


class Command(BaseCommand):
    help = 'Process CAPMF policy dataseries'
    Debug = False
    Logging = False

    datapath = settings.DATA_PATH

    start_time = time.time()
    start_timestamp = datetime.isoformat(datetime.now())
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    if Logging:
        logfile = open(settings.logfile_path, 'a')
        logfile.write('> Creating Dataflow Directory \n')
        logfile.write('> Starting at: ' + str(date) + '\n')

    if Debug:
        print('> Process CAPMF Data')
        print('> ' + str(date) + '\n')

    # Read the list of downloaded dataseries
    dataseries_list_file = settings.dataseries_file
    dataseries_list_update_file = settings.dataseries_update_file

    series_list = json.load(open(dataseries_list_file))
    if Debug:
        print('N = ', len(series_list))
    count = 0

    # Select the series to be processed
    # TODO Currently we process all
    download_list = series_list
    static_list = []

    # TODO This must be set to all dataseries if there is a change in the dataflows
    # Structure to store updated dataseries records
    series_list_update = []

    # Loop over all dataseries listed in catalog
    for series in download_list:

        count += 1
        processing_start = time.time()

        dataflow = series['DF_NAME']
        series_id = series['ID']

        # validity markers (for debugging purposes only)
        check1 = ''
        check2 = ''
        check3 = ''
        check4 = ''

        Data = {}
        Data['Df_Name'] = dataflow
        Data['Title'] = series['TITLE']
        Data['Definition'] = series['TITLE_COMPL']
        Data['Identifier'] = series_id
        Data['Units'] = series['UNIT']
        Data['Frequency'] = series['FREQ']
        Data['Reference Area'] = series['REF_AREA']

        field_id = 'POL_' + series['ID'].split('.')[1]
        Data['Activity'] = field_id

        field_index = field_codes.index(field_id)

        Data['Description'] = field_description[field_index]
        Data['Long Description'] = field_description_long[field_index]
        Data['Code List'] = field_code_list[field_id]
        Data['Field Type'] = field_type[field_index]

        # Load and parse the saved JSON files

        input_file = str(datapath) + '/dataflows/' + dataflow + '/' + series_id + '.json'

        Dates = []
        Values = []
        Status = []


        # Try to load the data
        try:
            mydata = json.load(open(input_file))
            Dates = mydata['Dates']
            Values = mydata['Values']
            Status = mydata['Status']
            if Debug:
                print('Parsed ' + series_id + '\n')
        except Exception as e:
            if Logging:
                logfile.write('Could not load/parse ' + series_id + '\n')
            else:
                print('Could not load/parse ' + series_id + '\n')

        # Total number of observations
        ObsCount = len(Values)

        # Actual measurements (excluding NaN)
        # ValidCount = np.count_nonzero(~np.isnan(Values))

        LastDate = Dates[len(Dates) - 1]
        lastDate = datetime.strptime(LastDate, "%Y-%m-%d").date()

        # now = datetime.now()
        # nowDate = now.date()

        if Debug:
            print(ObsCount, lastDate)

        # Compute absolute and percent differences for numerical types
        # print(Data['Field Type'], Values[-10:])

        Diffs = []
        PDiffs = []
        Diffs.append(0)
        PDiffs.append(0)

        for k in range(1, len(Values)):
            if Data['Field Type'] != 'text':

                Diffs.append(Values[k] - Values[k - 1])
                if math.fabs(Values[k - 1]) > 0:
                    PDiffs.append((Values[k] - Values[k - 1]) / Values[k - 1])
                else:
                    PDiffs.append(0)
            else:
                Diffs.append(0)
                PDiffs.append(0)

        series['Status'] = 'Valid'
        Data['Dates'] = Dates
        Data['Values'] = Values
        Data['Status'] = Status
        Data['Delta'] = Diffs
        Data['PDelta'] = PDiffs

        # Compute Metrics
        Metrics = {}
        Value = np.array(Values)
        FirstDate = Dates[0]
        # ObsCount = len(Value)

        # TODO CONVERT TO UTC DATE
        Data['LastDate'] = LastDate

        if Data['Field Type'] != 'text':
            # Compute key risk metrics and recent observations
            max_value = np.max(Value)
            min_value = np.min(Value)
            q25_value = np.percentile(Value, 25)
            # mode_value = stats.mode(Value)
            median_value = np.median(Value)
            q75_value = np.percentile(Value, 75)
            mean_value = np.mean(Value)
            std_value = np.std(Value)
            skew_value = stats.skew(Value)
            kurtosis_value = stats.kurtosis(Value)
            last_value = Value[len(Value) - 1]
            value_m1 = Value[len(Value) - 2]
            value_m2 = Value[len(Value) - 3]
            value_m3 = Value[len(Value) - 4]

            # Compute scale (range)
            val_range = math.fabs(max_value - min_value)
            if val_range > 0:
                val_orders = math.ceil(math.log10(val_range))
            else:
                val_orders = 1

            # pack into dictionary
            Metrics = {
                'FirstDate': FirstDate,
                'LastDate': LastDate,
                'Frequency': Data['Frequency'],
                'ObsCount': ObsCount,
                'Min': round(min_value, 3),
                'Max': round(max_value, 3),
                'Median': round(median_value, 3),
                # 'Mode': round(mode_value, 3),
                'Q25': round(q25_value, 3),
                'Q75': round(q75_value, 3),
                'Mean': round(mean_value, 3),
                'Vol': round(std_value, 3),
                'Skew': round(skew_value, 3),
                'Kurtosis': round(kurtosis_value, 3),
                'T': round(last_value, 3),
                'T-1': round(value_m1, 3),
                'T-2': round(value_m2, 3),
                'T-3': round(value_m3, 3),
                'Orders': val_orders
            }
        else:
            Metrics = {
                'FirstDate': FirstDate,
                'LastDate': LastDate,
                'Frequency': Data['Frequency'],
                'ObsCount': ObsCount,
                'Min': 0,
                'Max': 0,
                'Median': 0,
                'Q25': 0,
                'Q75': 0,
                'Mean': 0,
                'Vol': 0,
                'Skew': 0,
                'Kurtosis': 0,
                'T': 0,
                'T-1': 0,
                'T-2': 0,
                'T-3': 0,
                'Orders': 0
            }

        Data['Metrics'] = Metrics

        if Data['Field Type'] != 'text':

            # Compute Geometry (For Volatility Gauge Visualization)

            # Zero decline / increase is at 90
            # 20% change is 30 degrees
            mean_value = 0
            std_value = 20
            angle_unit = 3.1415 / 6.0
            theta_current = angle_unit * (last_value - mean_value) / std_value
            theta_m1 = angle_unit * (value_m1 - mean_value) / std_value
            theta_m2 = angle_unit * (value_m2 - mean_value) / std_value
            theta_m3 = angle_unit * (value_m3 - mean_value) / std_value
            theta_max = angle_unit * (max_value - mean_value) / std_value
            theta_min = angle_unit * (min_value - mean_value) / std_value

            Geometry = {'Max': theta_max, 'Min': theta_min, 'Current': theta_current, 'Min1': theta_m1, 'Min2': theta_m2, 'Min3': theta_m3}

        else:
            Geometry = {'Max': 0, 'Min': 0, 'Current': 0, 'Min1': 0, 'Min2': 0, 'Min3': 0}

        Data['Geometry_1D'] = Geometry

        processing_end = time.time()
        processing_time = round(processing_end - processing_start, 4)

        if Debug:
            print(count, len(series_list), processing_time)

        output_file = str(datapath) + '/dataflows/' + dataflow + '/' + series_id + '.P' + '.json'
        print('Dumping File: ', output_file)
        print(Data)
        json.dump(Data, open(output_file, 'w'), sort_keys=True, indent=4, separators=(',', ': '))
        series_list_update.append(series)
        print('Done')

    # store an updated list of dataseries dicts
    json.dump(series_list_update, open(dataseries_list_update_file, 'w'), sort_keys=True, indent=4,
              separators=(',', ': '))

    if Logging:
        logfile.write("> Processed CAPMF Policy Data  \n")
        logfile.write("> Execution Time: %s seconds --- \n" % (time.time() - start_time))
        logfile.write(80 * '=' + '\n')
        logfile.close()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully processed CAPMF policy data'))
