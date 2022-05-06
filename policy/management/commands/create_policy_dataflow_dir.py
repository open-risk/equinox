"""

Created Wed Jun 10 12:48:51 CEST 2020

"""

import os
import pickle
import time
from datetime import datetime

import policy.settings as settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create policy data dataflow directories'
    Debug = False
    Logging = True

    start_time = time.time()
    start_timestamp = datetime.isoformat(datetime.now())
    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    datapath = settings.ROOT_PATH + settings.DATA_PATH

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
        logfile.write(80*'=' + '\n')
        logfile.close()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully created policy dataflow directories'))
