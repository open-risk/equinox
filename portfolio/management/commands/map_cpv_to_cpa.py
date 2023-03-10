# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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

import json
import os

from django.core.management.base import BaseCommand

from portfolio.Project import Project
from equinox.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Map a CPV Code to a CPA Code'

    # Load the mapping table from disk
    FILE = os.path.join(BASE_DIR, 'reference/cpv_cpa_dict.json')
    f = open(FILE, mode='r')
    cpv_map = json.load(f)
    # Update the CPA code for all projects
    indata = []
    for pr in Project.objects.all():
        if len(pr.cpv_code) == 8:
            pr.cpa_code = cpv_map[pr.cpv_code]
        else: # hack for string based definition of single digit division cpv codes (03, 09 etc)
            cpv_code = '0' + pr.cpv_code
            pr.cpa_code = cpv_map[cpv_code]
        indata.append(pr)

    Project.objects.bulk_update(indata, ['cpa_code'])
    f.close()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully mapped CPV codes to CPA codes'))
