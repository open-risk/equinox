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

from portfolio.PortfolioManager import PortfolioManager


class Command(BaseCommand):
    help = 'Imports portfolio manager data'

    # Delete existing objects
    PortfolioManager.objects.all().delete()

    # Import data from file
    data = pd.read_csv("pm.csv", header='infer', delimiter=',')

    """
    OFFICIALNAME,ADDRESS,TOWN,POSTAL_CODE,COUNTRY,PHONE,E_MAIL,FAX,NUTS,URL_GENERAL,URL_BUYER,CONTACT_POINT,NATIONALID
    """
    indata = []
    serial = 0
    for index, entry in data.iterrows():
        pm = PortfolioManager(
            manager_identifier=entry['PK'],
            manager_legal_entity_identifier=entry['NATIONALID'],
            name_of_manager=entry['OFFICIALNAME'],
            address=entry['ADDRESS'],
            town=entry['TOWN'],
            postal_code=entry['POSTAL_CODE'],
            country=entry['COUNTRY'],
            phone=entry['PHONE'],
            email=entry['E_MAIL'],
            fax=entry['FAX'],
            region=entry['NUTS'],
            website=entry['URL_GENERAL'],
            pm_website=entry['URL_BUYER'],
            contact_point=entry['CONTACT_POINT'])
        serial += 1

        indata.append(pm)

    PortfolioManager.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted portfolio manager data into db'))
