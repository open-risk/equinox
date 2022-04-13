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

from django.core.management.base import BaseCommand
from portfolio.EmissionsSource import GPPEmissionsSource
from reference.intensity import intensity


class Command(BaseCommand):
    def handle(self, *args, **options):
        gpp_set = GPPEmissionsSource.objects.all()

        """
          iterate over procurement portfolio (project portfolio)
          read emissions intensity from cpv_code dictionary
          set co2_amount as emissions intensity times project budget
          save update source data     
        """

        for source in gpp_set.iterator():
            if source.project.cpv_code[:2] in intensity and source.project.project_budget > 0:
                multiplier = intensity[source.project.cpv_code[:2]]
                source.co2_amount = round(source.project.project_budget * multiplier / 1000000, 1)
                source.save()
