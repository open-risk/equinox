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

from portfolio.Project import Project
from portfolio.ProjectActivity import ProjectActivity


class Command(BaseCommand):
    help = 'Imports project activity data'

    # Delete existing objects
    ProjectActivity.objects.all().delete()

    # Import data from file
    data = pd.read_csv("pa.csv", header='infer', delimiter=',')

    """
    TITLE,NUTS,MAIN_SITE,SHORT_DESCR

    """
    indata = []
    serial = 10000

    for index, entry in data.iterrows():
        pr = Project.objects.get(pk=entry['PROJECT'])

        # TODO fix null issue with markdown field
        pa = ProjectActivity(
            project_activity_identifier=entry['PK'],
            project=pr,
            project_activity_title=entry['TITLE'],
            project_activity_description=entry['SHORT_DESCR'],
            region=entry['NUTS'],
            baseline_procedure_justification="",
            main_site=entry['MAIN_SITE'])

        serial += 1

        indata.append(pa)
        # pa.save()

    ProjectActivity.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted project activity data into db'))
