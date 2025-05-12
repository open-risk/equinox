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

import pandas as pd
from django.core.management.base import BaseCommand

from portfolio.Contractor import Contractor
from portfolio.Project import Project


class Command(BaseCommand):
    help = 'Imports Contractor data'

    # Delete existing objects
    Contractor.objects.all().delete()

    # Import data from file
    data = pd.read_csv("co.csv", header='infer', delimiter=',')

    """
    SME,OFFICIALNAME,NATIONALID,ADDRESS,TOWN,POSTAL_CODE,COUNTRY,NUTS,PHONE,E_MAIL,URL,FAX

    """
    indata = []
    serial = 10000
    for index, entry in data.iterrows():
        pr = Project.objects.get(pk=entry['PROJECT'])
        co = Contractor(
            contractor_identifier=entry['PK'],
            project=pr,
            is_sme=entry['SME'],
            contractor_legal_entity_identifier=entry['NATIONALID'],
            name_of_contractor=entry['OFFICIALNAME'],
            address=entry['ADDRESS'],
            town=entry['TOWN'],
            postal_code=entry['POSTAL_CODE'],
            country=entry['COUNTRY'],
            phone=entry['PHONE'],
            email=entry['E_MAIL'],
            fax=entry['FAX'],
            region=entry['NUTS'],
            website=entry['URL'])
        serial += 1

        indata.append(co)

    Contractor.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted contractor data into db'))
