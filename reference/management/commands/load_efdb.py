import csv
from django.core.management import BaseCommand
from reference.EmissionFactor import EmissionFactor


class Command(BaseCommand):
    help = 'Load an emissions factor csv file into equinox. Currently the only format supported is the IPCC EFDB database (exported as | -separated CSV file)'

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
