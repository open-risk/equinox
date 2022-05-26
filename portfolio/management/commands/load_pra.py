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

import pandas as pd
from django.core.management.base import BaseCommand

from portfolio.Asset import ProjectAsset
from portfolio.Project import Project


class Command(BaseCommand):
    help = 'Imports project asset data'

    # Delete existing objects
    ProjectAsset.objects.all().delete()

    # Import data from file
    data = pd.read_csv("pra.csv", header='infer', delimiter=',')

    """
    PK,PROJECT,ASSET_CLASS,DESCRIPTION,REGISTRATION_NUMBER,LEGAL_OWNER,ASSET_GHG_EMISSIONS,CITY_OF_REGISTERED_LOCATION,COUNTRY_OF_REGISTERED_LOCATION


    """
    indata = []
    serial = 10000

    for index, entry in data.iterrows():
        pr = Project.objects.get(pk=entry['PROJECT'])

        pra = ProjectAsset(
            asset_identifier=entry['PK'],
            project=pr,
            asset_class=entry['ASSET_CLASS'],
            description=entry['DESCRIPTION'],
            registration_number=entry['REGISTRATION_NUMBER'],
            legal_owner=entry['LEGAL_OWNER'],
            asset_ghg_emissions=entry['ASSET_GHG_EMISSIONS'],
            city_of_registered_location=entry['CITY_OF_REGISTERED_LOCATION'],
            country_of_registered_location=entry['COUNTRY_OF_REGISTERED_LOCATION'])

        serial += 1

        indata.append(pra)

    ProjectAsset.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted project asset data into db'))
