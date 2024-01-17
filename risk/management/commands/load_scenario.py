# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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

from risk.Scenarios import Scenario


class Command(BaseCommand):
    help = 'Imports scenario data'

    # Delete existing objects
    Scenario.objects.all().delete()

    # Import data from file
    data = pd.read_json("Scenario.json")

    """

    name = models.CharField(max_length=200, help_text="A way to identify the scenario projection")
    description = models.TextField(blank=True, null=True, help_text="Scenario Description")
    cutoff_date = models.DateTimeField(blank=True, null=True,
    scenario_type = models.CharField(blank=True, null=True, max_length=80, help_text="Scenario Type or Category")
    scenario_no = models.IntegerField(default=1, help_text="Number of Scenarios")
    scenario_probabilities = models.JSONField(blank=True, null=True, help_text="Scenario Probabilities (Optional). 
    factor_no = models.IntegerField(default=1, help_text="The Number of Scenario Factors (Variables)")
    factor_values = models.JSONField(blank=True, null=True, help_text="Factor Values under the Projection as a 
    factor_units = models.JSONField(blank=True, null=True, help_text="Factor Variable Name / Units")
    timepoint_no = models.IntegerField(default=1, help_text="Number of Timepoints (Periods + 1)")
    timepoints = models.JSONField(blank=True, null=True, help_text="Timepoint Values")
    
    """
    indata = []
    serial = 0
    for index, entry in data.iterrows():
        sc = Scenario(
            name=entry['name'],
            description='Scenario Description',
            cutoff_date=entry['cutoff_date'],
            scenario_type=entry['scenario_type'],
            factor_values=entry['factor_values'],
            factor_units=entry['factor_units'],
            timepoint_no=len(entry['timepoints']),
            timepoints=entry['timepoints'])
        serial += 1

        indata.append(sc)

    Scenario.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted scenario data into db'))
