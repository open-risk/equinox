"""

Created Wed Jun 10 12:48:51 CEST 2020

"""

import json
from datetime import datetime

import policy.settings as settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from policy.models import DashBoardParams
from policy.models import DataSeries


class Command(BaseCommand):
    help = 'Imports dataseries data into the database (no backup!)'
    Debug = True

    datapath = settings.ROOT_PATH + settings.DATA_PATH

    # path = settings.DATA_PATH
    dataseries_file = settings.ROOT_PATH + settings.dataseries_update_file

    if Debug:
        print(dataseries_file)

    # We don't backup existing data
    # Directory backups
    # TODO think timeseries incremental backup strategy

    # Delete existing DataSeries objects
    DataSeries.objects.all().delete()

    # Import metadata from file
    metadata = json.load(open(settings.ROOT_PATH + settings.metadata_file))

    # Import valid dataseries METADATA from file
    dataseries = json.load(open(dataseries_file))

    # color the timeseries by urgency
    cutoff_change_red = settings.CUTOFF_CHANGE_RED  # very major change
    cutoff_change_orange = settings.CUTOFF_CHANGE_ORANGE  # significant change
    cutoff_change_yellow = settings.CUTOFF_CHANGE_YELLOW  # some change

    total_n = 0
    tracked_n = 0
    red = 0
    yellow = 0
    orange = 0
    gray = 0

    indata = []
    for series in dataseries:
        total_n += 1
        if Debug:
            print(series['DF_NAME'], " : ", series['ID'])
        # Create records for valid timeseries
        if series['Status'] == 'Valid':

            tracked_n += 1
            dataflow = series['DF_NAME']
            series_id = series['ID']
            load_path = datapath + 'dataflows/' + dataflow + "/" + series_id + ".P.json"
            series_data = json.load(open(load_path))
            observation_date = datetime.strptime(series_data['LastDate'], "%Y-%m-%d")

            # Create new delta algorithm
            # The average of the last two days versus the average of two days prior
            v = series_data['Metrics']['T']
            vm1 = series_data['Metrics']['T-1']
            vm2 = series_data['Metrics']['T-2']
            vm3 = series_data['Metrics']['T-3']
            delta = (v + vm1) / 2 - (vm2 + vm3) / 2

            if delta >= cutoff_change_red:
                color = 'red'
                red += 1
            elif delta >= cutoff_change_orange:
                color = 'orange'
                orange += 1
            elif delta >= cutoff_change_yellow:
                color = 'yellow'
                yellow += 1
            else:
                color = 'gray'
                gray += 1

            ref_area = series['REF_AREA']
            ref_area_parts = ref_area.split('.')

            region = ''
            if len(ref_area_parts) == 2:
                region = ref_area_parts[1]
            if len(ref_area_parts) == 3:
                region = ref_area_parts[1] + '.' + ref_area_parts[2]

            ds = DataSeries(
                status='Valid',
                color=color,
                region=region,
                agg_level=series['AGG_LEVEL'],
                activity=series['ACTIVITY'],
                # Metadata from the dataseries database file
                df_name=series['DF_NAME'],
                title=series['TITLE'],
                title_long=series['TITLE_COMPL'],
                # identifier=series['DF_NAME'] + '.' + series['ID'],
                identifier=series['ID'],
                rest_url=series['URL'],
                unit=series['UNIT'],
                field_type=series_data['Field Type'],
                code_list=series_data['Code List'],
                frequency=series_data['Frequency'],
                # TODO WORKAROUND FOR STRING DATA (UNICODE JS PARSING PROBLEM)
                dates=json.dumps(series_data['Dates']),
                metrics=json.dumps(series_data['Metrics']),
                geometry_1D=json.dumps(series_data['Geometry_1D']),
                # END WORKAROUND
                values=series_data['Values'],
                values_diff=series_data['Delta'],
                values_diff_p=series_data['PDelta'],
                last_observation_date=series_data['LastDate'],
                last_change_date=timezone.now())
            indata.append(ds)
            # ds.save()

    if Debug:
        print(tracked_n, total_n)

    chunks = 10
    chunk_size = int(len(indata) / chunks)

    if Debug:
        print(tracked_n, total_n)
        print('Inserting in chunks of ', chunk_size)

    low_end = 0
    high_end = 0
    for c in range(chunks):
        low_end = c * chunk_size
        high_end = (c+1) * chunk_size
        if Debug:
            print(low_end, high_end)
        DataSeries.objects.bulk_create(indata[low_end:high_end])
    # DataSeries.objects.bulk_create(indata[high_end:])

    # Inserting data in one chunk
    # DataSeries.objects.bulk_create(indata)

    DashBoardParams.objects.all().delete()
    params = DashBoardParams(
        red_datasets=red,
        orange_datasets=orange,
        yellow_datasets=yellow,
        gray_datasets=gray,
        total_datasets=total_n,
        tracked_datasets=tracked_n,
        live_datasets=red + orange + yellow,
        country_metadata=metadata
    )
    params.save()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted policy Dataseries'))
