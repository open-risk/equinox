"""
Created Tue Dec  8 20:54:39 CET 2020

Modified from mobility data
Updated at 3/3/21
"""
from django.core.management.base import BaseCommand
from policy.models import DashBoardParams, GeoSlice
from policy.models import DataSeries, DataFlow


class Command(BaseCommand):
    help = 'Deletes all policy data from the database (no backup!)'
    Debug = False

    DataFlow.objects.all().delete()
    DataSeries.objects.all().delete()
    DashBoardParams.objects.all().delete()
    GeoSlice.objects.all().delete()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleted all policy data. Good Luck!'))
