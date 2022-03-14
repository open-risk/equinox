from django.core.management.base import BaseCommand
from portfolio.EmissionsSource import BuildingEmissionsSource
from portfolio.models import AreaSource, MultiAreaSource


class Command(BaseCommand):
    def handle(self, *args, **options):
        BuildingEmissionsSource.objects.all().delete()
        AreaSource.objects.all().delete()
        MultiAreaSource.objects.all().delete()
