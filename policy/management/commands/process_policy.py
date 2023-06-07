"""
Created on Tue Aug 23 19:41:00 2016
Updated on Thu Oct  6 23:02:43 2016
Merged into equinox Commands Tue Mar  6 11:43:38 CET 2018
Adapted for mobility data Tue Apr 28 19:41:59 CEST 2020
Adapted for policy data Wed Jun 10 12:48:51 CEST 2020

Update Step 3
Process data from local json files into json
- impute missing data (if possible)
- calculate metrics
- pre-calculate graphical elements

Updated at 3/2/21 (management command)
"""

import json
import math
import time
from datetime import datetime

import numpy as np
from django.core.management.base import BaseCommand
from scipy import stats

import policy.settings as settings

# The field names as they are in the CSV header
from policy.settings import field_codes, field_description, field_description_long, field_code_list, field_type

"""
Starting with downloaded data
{
    "Dates" : []
    "Values" : []
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
    help = 'Process policy dataseries'
    Debug = True
    Logging = True

    datapath = settings.DATA_PATH

    start_time = time.time()
    start_timestamp = datetime.isoformat(datetime.now())
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    if Logging:
        logfile = open(settings.logfile_path, 'a')
        logfile.write('> Creating Dataflow Directory \n')
        logfile.write('> Starting at: ' + str(date) + '\n')

    if Debug:
        print('> Script 3: Process Oxford Policy Data')
        print('> ' + str(date) + '\n')

    # Read the list of downloaded dataseries
    dataseries_list_file = settings.dataseries_file
    dataseries_list_update_file =  settings.dataseries_update_file

    series_list = json.load(open(dataseries_list_file))
    if Debug:
        print('N = ', len(series_list))
    count = 0

    # Select the series to be processed
    # TODO Currently All
    download_list = series_list
    static_list = []

    # # # TODO This must be set to all dataseries if there is a change in the dataflows
    # # # Otherwise the file is incomplete (missing processing Status)
    # # Download_Type = 'A'
    # #
    # # if Download_Type == 'D':
    # #     for series in series_list:
    # #         if series['FREQ'] == 'D' or series['FREQ'] == 'B':
    # #             download_list.append(series)
    # #         else:
    # #             static_list.append(series)
    # #
    # # if Download_Type == 'A':
    # #     download_list = series_list
    #
    # Structure to store updated dataseries records
    series_list_update = []
    #
    # Loop over all dataseries listed in catalog
    for series in download_list:

        count += 1
        processing_start = time.time()

        dataflow = series['DF_NAME']
        series_id = series['ID']

        # validity markers (for debugging only)
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

        field_id = series['ID'][3:]
        Data['Activity'] = field_id

        field_index = field_codes.index(field_id)

        Data['Description'] = field_description[field_index]
        Data['Long Description'] = field_description_long[field_index]
        Data['Code List'] = field_code_list[field_id]
        Data['Field Type'] = field_type[field_index]
        # print(field_index, Data['Description'], Data['Long Description'])

        # Load and parse the saved JSON files

        input_file = str(datapath) + '/policy/policy_data/dataflows/' + dataflow + '/' + series_id + '.json'

        Dates = []
        Values = []
        # Try to load the data
        try:
            mydata = json.load(open(input_file))
            Dates = mydata['Dates']
            Values = mydata['Values']
        except Exception as e:
            logfile.write('Could not load/parse ' + series_id + '\n')
            continue

        # Total number of observations
        ObsCount = len(Values)
        # Actual measurements (excluding NaN)
        ValidCount = np.count_nonzero(~np.isnan(Values))

        if Debug:
            print(ObsCount, ValidCount)

        LastDate = Dates[len(Dates) - 1]
        lastDate = datetime.strptime(LastDate, "%Y-%m-%d").date()

        now = datetime.now()
        nowDate = now.date()

        #
        # OVERRIDE For now we keep only full observation sets
        #

        # if ValidCount == ObsCount:

        if ObsCount > 6:  # Filter out insufficiently long timeseries

            if Logging:
                check1 = " len > 6"
                logfile.write(dataflow + ' : ' + series_id + check1 + '\n')

            # Compute absolute and percent differences
            Diffs = []
            PDiffs = []
            Diffs.append(0)
            PDiffs.append(0)
            for k in range(1, len(Values)):
                Diffs.append(Values[k] - Values[k - 1])
                if math.fabs(Values[k - 1]) > 0:
                    PDiffs.append((Values[k] - Values[k - 1]) / Values[k - 1])
                else:
                    PDiffs.append(0)

            series['Status'] = 'Valid'
            Data['Dates'] = Dates
            Data['Values'] = Values
            Data['Delta'] = Diffs
            Data['PDelta'] = PDiffs

            # Compute Metrics
            Metrics = {}
            Value = np.array(Values)
            FirstDate = Dates[0]
            # ObsCount = len(Value)

            # TODO CONVERT TO UTC DATE
            Data['LastDate'] = LastDate

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

            Data['Metrics'] = Metrics

            if std_value > 0:  # Ignore flat timeseries
                check2 = " vol > 0"
                if Logging:
                    logfile.write(dataflow + ' : ' + series_id + check2 + '\n')

                # Compute Geometry (For Volatility Gauge Visualization)

                # VOLATILITY GAUGE SETTINGS
                # Map key values onto circle
                # Average is at 90
                # 1 std is 30
                # angle_unit = 3.1415 / 6.0
                # theta_current = angle_unit * (last_value - mean_value) / std_value
                # theta_m1 = angle_unit * (value_m1 - mean_value) / std_value
                # theta_m2 = angle_unit * (value_m2 - mean_value) / std_value
                # theta_m3 = angle_unit * (value_m3 - mean_value) / std_value
                # theta_max = angle_unit * (max_value - mean_value) / std_value
                # theta_min = angle_unit * (min_value - mean_value) / std_value

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

                Geometry = {'Max': theta_max, 'Min': theta_min, 'Current': theta_current, 'Min1': theta_m1,
                            'Min2': theta_m2, 'Min3': theta_m3}
                Data['Geometry_1D'] = Geometry

            else:
                check2 = " vol = 0"
                if Logging:
                    logfile.write(dataflow + ' : ' + series_id + check2 + '\n')
                series['Status'] = 'Stale Dataset'
        else:
            check1 = " len < 6"
            if Logging:
                logfile.write(dataflow + ' : ' + series_id + check1 + '\n')
            series['Status'] = 'Insufficient Length Dataset'
        # else:
        #     check4 = " Missing Data"
        #     if Logging:
        #         logfile.write(dataflow + ' : ' + series_id + check4 + '\n')
        #     series['Status'] = 'Missing Data'

        processing_end = time.time()
        processing_time = round(processing_end - processing_start, 4)
        if Debug:
            print(count, len(series_list), processing_time)

        # if Debug:
        #     print(Data)
        #     if series['Status'] is 'Valid':
        #         print(dataflow, " : ", series_id, LastDate, processing_time, " sec")
        #     else:
        #         print(dataflow, " : ", series_id, series['Status'], check1, check2, check3, check4)
        #
        #
        output_file = str(datapath) + '/policy/policy_data/dataflows/' + dataflow + '/' + series_id + '.P' + '.json'
        json.dump(Data, open(output_file, 'w'), sort_keys=True, indent=4, separators=(',', ': '))
        series_list_update.append(series)

    # store an updated list of dataseries dicts
    json.dump(series_list_update, open(dataseries_list_update_file, 'w'), sort_keys=True, indent=4,
              separators=(',', ': '))

    # Attach series we have not processed
    # series_list_update.extend(static_list)
    # if Debug:
    #     print("Processed :", len(download_list))
    #     print("Untouched :", len(static_list))

    if Logging:
        logfile.write("> Processed  Policy Data  \n")
        logfile.write("> Execution Time: %s seconds --- \n" % (time.time() - start_time))
        logfile.write(80 * '=' + '\n')
        logfile.close()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully processed policy data'))
