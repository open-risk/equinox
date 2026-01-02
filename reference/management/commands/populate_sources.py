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

from django.core.management import BaseCommand

from portfolio.EmissionsSource import GPPEmissionsSource
from portfolio.Project import Project
from reference.EmissionIntensity import intensity


class Command(BaseCommand):
    help = 'parse projects and if applicable generate an associated emissions source'

    def handle(self, *args, **kwargs):
        pset = Project.objects.all()

        """
          iterate over procurement / project portfolio
          read emissions intensity from cpv_code dictionary
          set co2_amount as emissions intensity times project budget
          save update source data
          
          mode = 0 is a testing mode

        """
        mode = 0

        if mode == 0:
            i = 1
            for p in pset.iterator():
                if p.cpv_code[:2] in intensity:
                    print(p.cpv_code[:2], intensity[p.cpv_code[:2]])
                    source = GPPEmissionsSource()
                    source.source_identifier = 'GPP' + str(i)
                    print(source.source_identifier)
                    i += 1
                    source.project = p
                    source.comments = 'Testing the EEIO Method'
                    source.save()
