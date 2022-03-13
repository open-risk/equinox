from django.core.management.base import BaseCommand
from portfolio.EmissionsSource import BuildingEmissionsSource


class Command(BaseCommand):
    def handle(self, *args, **options):
        BuildingEmissionsSource.objects.all().delete()
