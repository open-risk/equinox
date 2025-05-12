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

"""

import json

from django.core.management.base import BaseCommand
from django.utils import timezone

import policy.settings as settings
from policy.models import DashBoardParams
from policy.models import DataFlow
from policy.models import DataSeries


class Command(BaseCommand):
    help = 'Imports policy Dataflow metadata list into the database'
    Debug = False

    path = settings.DATA_PATH
    dataflows_file = settings.dataflows_file
    dimensions_file = settings.dimensions_file
    dataseries_file = settings.dataseries_update_file

    # Do a backup (for emergency use only)
    # TODO Make readable by update workflow
    # all_data = serializers.serialize("json", DataFlow.objects.all())
    # f = open(path + "django.backup.json", 'w')
    # f.write(all_data)
    # f.close()
    # json.dump(updated_dataflows, open("update_test.json",'w'))

    # Delete existing DataFlow objects
    DataFlow.objects.all().delete()

    # Expand Policy Categories with user-friendly menu labels
    dictionary = {
        '1': 'OxCGRT Policy Data',
    }

    # Import updated dataflow list from file
    dataflows = json.load(open(dataflows_file))
    # Get dataseries from DB
    # dataseries = DataSeries.objects.all()
    # Get dimensions metadata from file
    dimensions = json.load(open(dimensions_file))

    # # Total dataseries
    # total_n = 0
    # # Tracked dataseries
    # tracked_n = 0

    total_df = 0

    for df in dataflows:

        total_df += 1

        category_dict = df['CATEGORY_LIST']
        category_id = category_dict['OXFORD']

        dataset_id = []
        observation_list = []
        # total_n += df['GOOGLE_N']

        # All tracked by default
        # GOOGLE_N = DASHBOARD_N
        if df['TRACKED']:
            dimension_data = dimensions[df['IDENTIFIER']]
            # tracked_n += df['DASHBOARD_N']
            # Fetch all dataseries for this dataflow
            dataseries = DataSeries.objects.filter(df_name=df['IDENTIFIER'])

            #
            # use these to keep track of significant changes
            red = 0
            orange = 0
            yellow = 0
            gray = 0

            for series in dataseries:
                # Append the series identifier

                dataset_id.append({'id': series.identifier, 'desc': series.title_long})

                # Create color code statistics per workflow
                if series.df_name == df['IDENTIFIER']:
                    if series.color == u'red':
                        red += 1
                    elif series.color == u'orange':
                        orange += 1
                    elif series.color == u'yellow':
                        yellow += 1
                    else:
                        gray += 1
            # print(df['IDENTIFIER'], yellow)
            # observation_list = [red, orange, yellow, gray]

            # Name is the full name country
            # Identifier is the 2 letter country code

            # TODO geoslices is set to zero (populate_db_geoslices)
            dataflow = DataFlow(
                name=df['NAME'],
                identifier=df['IDENTIFIER'],
                short_desc=df['SHORT_DESC'],
                long_desc=df['LONG_DESC'],
                geo=df['GEO'],
                geoslices=0,
                node_url="https://localhost/api/",
                dimensions=dimension_data,
                dataset_id=dataset_id,
                available_n=df['OXFORD_N'],
                dashboard_n=df['DASHBOARD_N'],
                regions_n=df['REGIONS_N'],
                subregions_n=df['SUBREGIONS_N'],
                live_n=red + orange + yellow,
                id=df['ID'],
                tracked=df['TRACKED'],
                update=df['UPDATE'],
                selectors=df['SELECTORS'],
                category_list=df['CATEGORY_LIST'],
                menu_category=dictionary[str(category_id)],
                freshness=observation_list,
                last_change_date=timezone.now())

            dataflow.save()

    # if Debug is True:
    #     print(total_n, tracked_n)

    # params = DashBoardParams.objects.get(id=2)

    params = DashBoardParams.objects.all().first()
    #
    # if not params:
    #     params = DashBoardParams()
    #
    # params.total_datasets = total_n
    # params.tracked_datasets = tracked_n
    params.total_dataflows = total_df
    params.save()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted policy Dataflows'))
