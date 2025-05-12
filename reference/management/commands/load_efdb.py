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

import csv

from django.core.management import BaseCommand

from reference.EmissionFactor import EmissionFactor


class Command(BaseCommand):
    help = 'Load an emissions factor csv file into equinox. Currently the only format supported is the IPCC EFDB database (exported as | separated CSV file)'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, delimiter='|')
            next(reader)
            for row in reader:
                EmissionFactor.objects.create(
                    EF_ID=row[0],
                    IPCC_Category=row[1],
                    Gases=row[2],
                    Fuel=row[3],
                    Parameter_Type=row[4],
                    Description=row[5],
                    Technology_Practices=row[6],
                    Parameter_Conditions=row[7],
                    Regional_Conditions=row[8],
                    Control_Technologies=row[9],
                    Other_Properties=row[10],
                    Value=row[11],
                    Unit=row[12],
                    Equation=row[13],
                    IPCC_Worksheet=row[14],
                    Data_Source=row[15],
                    Technical_Reference=row[16],
                    English_Abstract=row[17],
                    Lower_Bound=row[18],
                    Upper_Bound=row[19],
                    Data_Quality=row[20],
                    Data_Quality_Reference=row[21],
                    Other_Data_Quality=row[22],
                    Data_Provider_Comments=row[23],
                    Other_Comments=row[24],
                    Data_Provider=row[25],
                    Link=row[26]
                )
