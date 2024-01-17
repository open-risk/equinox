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

"""

Created Wed Jun 10 12:48:51 CEST 2020

"""

import os
import pickle
import time
from datetime import datetime

from django.core.management.base import BaseCommand

import policy.settings as settings


class Command(BaseCommand):
    help = 'Create policy data dataflow directories'
    Debug = False
    Logging = True

    start_time = time.time()
    start_timestamp = datetime.isoformat(datetime.now())
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    datapath = settings.DATA_PATH

    if Logging:
        logfile = open(settings.logfile_path, 'a')
        logfile.write('> Creating Dataflow Directory \n')
        logfile.write('> Starting at: ' + str(date) + '\n')

    dataflow_dict = pickle.load(open(datapath + '/dataflow_dict' + '.pkl', 'rb'))

    for key in dataflow_dict:
        DF_DIR = datapath + 'dataflows/' + key
        if Debug:
            print(DF_DIR)
        # shutil.rmtree(DF_DIR)
        os.mkdir(DF_DIR)

    if Logging:
        logfile.write("> Created  Policy Data Dataflow Directory \n")
        logfile.write("> Execution Time: %s seconds --- \n" % (time.time() - start_time))
        logfile.write(80 * '=' + '\n')
        logfile.close()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully created policy dataflow directories'))
