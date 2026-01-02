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

"""

Created Wed Jun 10 12:48:51 CEST 2020

"""

from django.core.management.base import BaseCommand
from django.db.models import Q
from django.utils import timezone

from policy.models import DataFlow
from policy.models import DataSeries
from policy.models import GeoSlice
from policy.settings import activities_short


# ATTN This command must be executed before populate_db_dataflows (to ensure correct dates)

# Hardwired to produce six geoslices for the different policy data types for Europe

class Command(BaseCommand):
    help = 'Create and insert policy data geoslices into the database'
    Debug = False

    # the 28 countries of EU (keeping UK in)
    geolocations = {
        "AT": "Austria",
        "BE": "Belgium",
        'BA': 'Bosnia and Herzegovina',
        "BG": "Bulgaria",
        'BY': 'Belarus',
        'CH': 'Switzerland',
        "CY": "Cyprus",
        "CZ": "Czech Republic",
        "DE": "Germany",
        "DK": "Denmark",
        "EE": "Estonia",
        "ES": "Spain",
        "FI": "Finland",
        "FR": "France",
        "GB": "United Kingdom",
        "GR": "Greece",
        "HR": "Croatia",
        "HU": "Hungary",
        "IE": "Ireland",
        "IT": "Italy",
        "LT": "Lithuania",
        "LU": "Luxembourg",
        "LV": "Latvia",
        "MT": "Malta",
        'MK': 'North Macedonia',
        'MD': 'Moldova',
        'NO': 'Norway',
        "NL": "Netherlands",
        "PL": "Poland",
        "PT": "Portugal",
        "RO": "Romania",
        "SE": "Sweden",
        "SI": "Slovenia",
        "SK": "Slovakia",
        'RS': 'Serbia'
    }

    # Delete existing DataSeries objects
    GeoSlice.objects.all().delete()

    dataflows = DataFlow.objects.all()

    # one geoslice for each activity
    for ac in activities_short:
        # All our dataflows are by definition Country Level
        # for df in dataflows:

        # fetch the country level activity of all countries
        # ds_list = DataSeries.objects.filter(df_name=df.name)
        f1 = Q(agg_level='Country')
        f2 = Q(activity=ac)
        ds_list = DataSeries.objects.filter(f1 & f2)

        if Debug:
            print(len(ds_list))

        #
        # PART 1: Construct the list of Geoslices (a list of ID's)
        #

        # Select the dataseries that have valid locations
        geo_members = []

        for ds in ds_list:
            # id_string = ds.identifier.split('.')
            # ATTN hardcoded location
            country_code = ds.df_name
            # add dataseries to geoslice
            if country_code in geolocations:
                # construct geoslice ID
                # id_string.insert(2, u'ALL')
                # print(id_string)
                # slice_id = '.'.join(id_string)
                geo_members.append(ds.identifier)

        unique_list = set(geo_members)
        if Debug:
            print(geo_members)

        #
        # PART 2: Populate Geoslice records with data
        #
        # create geoslice database record
        geoslice = GeoSlice(
            identifier='EU.' + ac,
            df_name='',
            short_desc=ac + '.EU Geoslice',
            long_desc=ac + '.EU Geoslice',
            dimensions=None,
            dataset_id=geo_members,
            last_change_date=timezone.now())

        geoslice.save()

        if Debug:
            print(geoslice)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully created policy data Geoslices'))
