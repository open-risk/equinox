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

"""
Created Tue Dec  8 20:54:39 CET 2020


"""
from django.core.management.base import BaseCommand

from portfolio.Asset import ProjectAsset, Building, PowerPlant
from portfolio.Borrower import Borrower
from portfolio.Certificate import Certificate
from portfolio.Contractor import Contractor
from portfolio.Counterparty import Counterparty
from portfolio.EmissionsSource import EmissionsSource, GPCEmissionsSource, BuildingEmissionsSource, GPPEmissionsSource
from portfolio.Loan import Loan
from portfolio.Mortgage import Mortgage
from portfolio.Operator import Operator
from portfolio.PortfolioManager import PortfolioManager
from portfolio.Portfolios import ProjectPortfolio, PortfolioSnapshot, PortfolioTable, LimitStructure
from portfolio.PrimaryEffect import PrimaryEffect
from portfolio.Project import Project
from portfolio.ProjectActivity import ProjectActivity
from portfolio.ProjectCategory import ProjectCategory
from portfolio.ProjectCompany import ProjectCompany
from portfolio.ProjectEvent import ProjectEvent
from portfolio.Revenue import Revenue
from portfolio.SecondaryEffect import SecondaryEffect
from portfolio.Sponsor import Sponsor
from portfolio.Stakeholders import Stakeholders
from portfolio.Swap import Swap
from portfolio.models import PointSource, AreaSource, MultiAreaSource


class Command(BaseCommand):
    help = 'Deletes all portfolio data from the database (no backup!)'
    Debug = False

    ProjectAsset.objects.all().delete()
    Building.objects.all().delete()
    PowerPlant.objects.all().delete()
    PointSource.objects.all().delete()
    AreaSource.objects.all().delete()
    MultiAreaSource.objects.all().delete()
    PortfolioManager.objects.all().delete()
    ProjectPortfolio.objects.all().delete()
    PortfolioSnapshot.objects.all().delete()
    PortfolioTable.objects.all().delete()
    LimitStructure.objects.all().delete()
    Borrower.objects.all().delete()
    Contractor.objects.all().delete()
    Counterparty.objects.all().delete()
    EmissionsSource.objects.all().delete()
    GPCEmissionsSource.objects.all().delete()
    BuildingEmissionsSource.objects.all().delete()
    GPPEmissionsSource.objects.all().delete()
    Loan.objects.all().delete()
    Mortgage.objects.all().delete()
    Operator.objects.all().delete()
    PrimaryEffect.objects.all().delete()
    Project.objects.all().delete()
    ProjectActivity.objects.all().delete()
    ProjectCategory.objects.all().delete()
    ProjectCompany.objects.all().delete()
    ProjectEvent.objects.all().delete()
    Revenue.objects.all().delete()
    SecondaryEffect.objects.all().delete()
    Sponsor.objects.all().delete()
    Stakeholders.objects.all().delete()
    Swap.objects.all().delete()
    Certificate.objects.all().delete()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleted all portfolio data. Good Luck!'))
