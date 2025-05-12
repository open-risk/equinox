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


from django.test import TestCase

from portfolio.Asset import Building, PowerPlant
from portfolio.Borrower import Borrower
from portfolio.Certificate import Certificate
from portfolio.Contractor import Contractor
from portfolio.Counterparty import Counterparty
from portfolio.EmissionsSource import BuildingEmissionsSource, EmissionsSource, GPCEmissionsSource, GPPEmissionsSource
from portfolio.Loan import Loan
from portfolio.Mortgage import Mortgage
from portfolio.Operator import Operator
from portfolio.PortfolioManager import PortfolioManager
from portfolio.Portfolios import LimitStructure, PortfolioSnapshot, PortfolioTable, ProjectPortfolio
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
from portfolio.models import AreaSource, MultiAreaSource, PointSource


class PortfolioModelTests(TestCase):

    def test_area_source_str(self):
        geom = 'POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))'
        AreaSource.objects.create(name='test', location=geom)
        instance = AreaSource.objects.get()
        self.assertEquals("test", str(instance))

    def test_point_source_str(self):
        geom = 'POINT(0 0)'
        PointSource.objects.create(name='test', location=geom)
        instance = PointSource.objects.get()
        self.assertEquals("test", str(instance))

    def test_multiarea_source_str(self):
        geom = 'MULTIPOLYGON (((4.881969 52.394135, 4.88192 52.394225, 4.881783 52.39433, 4.881699 52.394356, 4.881663 52.394402, 4.881588 52.394448, 4.881546 52.394514, 4.881506 52.394534, 4.881427 52.394545, 4.881353 52.394533, 4.881275 52.394491, 4.881188 52.394467, 4.881063 52.394398, 4.881019 52.394347, 4.880958 52.394332, 4.880725 52.394221, 4.880682 52.394182, 4.880675 52.394143, 4.880597 52.394103, 4.880576 52.394054, 4.880595 52.394009, 4.88068 52.393949, 4.880774 52.393929, 4.880894 52.39396, 4.880963 52.393941, 4.881161 52.393779, 4.881274 52.393747, 4.881347 52.393759, 4.881596 52.393879, 4.881658 52.393943, 4.881733 52.393964, 4.881936 52.394078, 4.881969 52.394135), (4.881534 52.394129, 4.881337 52.394261, 4.881145 52.39416, 4.881331 52.394025, 4.881534 52.394129)))'
        MultiAreaSource.objects.create(name='test', location=geom)
        instance = MultiAreaSource.objects.get()
        self.assertEquals("test", str(instance))

    def test_borrower_str(self):
        Borrower.objects.create(counterparty_identifier='test')
        instance = Borrower.objects.get()
        self.assertEquals("test", str(instance))

    def test_building_str(self):
        Building.objects.create(protection_identifier='test')
        instance = Building.objects.get()
        self.assertEquals("test", str(instance))

    def test_building_emissions_source_str(self):
        BuildingEmissionsSource.objects.create(source_identifier='test')
        instance = BuildingEmissionsSource.objects.get()
        self.assertEquals("test", str(instance))

    def test_emissions_source_str(self):
        EmissionsSource.objects.create(source_identifier='test')
        instance = EmissionsSource.objects.get()
        self.assertEquals("test", str(instance))

    def test_gpc_emissions_source_str(self):
        GPCEmissionsSource.objects.create(source_identifier='test')
        instance = GPCEmissionsSource.objects.get()
        self.assertEquals("test", str(instance))

    def test_gpp_emissions_source_str(self):
        GPPEmissionsSource.objects.create(source_identifier='test')
        instance = GPPEmissionsSource.objects.get()
        self.assertEquals("test", str(instance))

    def test_contractor_str(self):
        Contractor.objects.create(contractor_identifier=1)
        instance = Contractor.objects.get()
        self.assertEquals("1", str(instance))

    def test_counterparty_str(self):
        Counterparty.objects.create(counterparty_identifier=1)
        instance = Counterparty.objects.get()
        self.assertEquals("1", str(instance))

    def test_limit_structure_str(self):
        LimitStructure.objects.create(name='test')
        instance = LimitStructure.objects.get()
        self.assertEquals("test", str(instance))

    def test_loan_str(self):
        Loan.objects.create(contract_identifier='test')
        instance = Loan.objects.get()
        self.assertEquals("test", str(instance))

    def test_swap_str(self):
        Swap.objects.create(swap_identifier='test')
        instance = Swap.objects.get()
        self.assertEquals("test", str(instance))

    def test_certificate_str(self):
        Certificate.objects.create(certificate_identifier='test')
        instance = Certificate.objects.get()
        self.assertEquals("test", str(instance))

    def test_power_plant_str(self):
        PowerPlant.objects.create(production_device_number='test')
        instance = PowerPlant.objects.get()
        self.assertEquals("test", str(instance))

    def test_mortgage_str(self):
        Mortgage.objects.create(contract_identifier='test')
        instance = Mortgage.objects.get()
        self.assertEquals("test", str(instance))

    def test_operator_str(self):
        Operator.objects.create(operator_identifier='test')
        instance = Operator.objects.get()
        self.assertEquals("test", str(instance))

    def test_portfoliomanager_str(self):
        PortfolioManager.objects.create(name_of_manager='test')
        instance = PortfolioManager.objects.get()
        self.assertEquals("test", str(instance))

    def test_portfoliosnapshot_str(self):
        PortfolioSnapshot.objects.create(name='test')
        instance = PortfolioSnapshot.objects.get()
        self.assertEquals("test", str(instance))

    def test_portfoliotable_str(self):
        ProjectPortfolio.objects.create()
        project_portfolio = ProjectPortfolio.objects.get()
        PortfolioTable.objects.create(portfolio_id=project_portfolio)
        instance = PortfolioTable.objects.get()
        self.assertEquals("1", str(instance))

    def test_primary_effect_str(self):
        PrimaryEffect.objects.create(primary_effect_identifier='test', primary_effect_description='')
        instance = PrimaryEffect.objects.get()
        self.assertEquals("test", str(instance))

    def test_project_str(self):
        Project.objects.create(project_identifier='test', project_description='')
        instance = Project.objects.get()
        self.assertEquals("test", str(instance))

    def test_project_activity_str(self):
        ProjectActivity.objects.create(project_activity_identifier='test', project_activity_description='',
                                       baseline_procedure_justification='')
        instance = ProjectActivity.objects.get()
        self.assertEquals("test", str(instance))

    def test_project_category_str(self):
        ProjectCategory.objects.create(name='test', depth=1)
        instance = ProjectCategory.objects.get()
        self.assertEquals('Project Category: {}'.format('test'), str(instance))

    def test_project_company_str(self):
        ProjectCompany.objects.create(project_company_identifier='test')
        instance = ProjectCompany.objects.get()
        self.assertEquals("test", str(instance))

    def test_project_event_str(self):
        ProjectEvent.objects.create(project_event_identifier='test')
        instance = ProjectEvent.objects.get()
        self.assertEquals("test", str(instance))

    def test_revenue_str(self):
        Revenue.objects.create(revenue_group_identifier='test')
        instance = Revenue.objects.get()
        self.assertEquals("test", str(instance))

    def test_project_portfolio_str(self):
        ProjectPortfolio.objects.create(name='test')
        instance = ProjectPortfolio.objects.get()
        self.assertEquals("test", str(instance))

    def test_secondary_effect_str(self):
        SecondaryEffect.objects.create(secondary_effect_identifier='test', secondary_effect_description='')
        instance = SecondaryEffect.objects.get()
        self.assertEquals("test", str(instance))

    def test_sponsor_str(self):
        Sponsor.objects.create(sponsor_identifier='test')
        instance = Sponsor.objects.get()
        self.assertEquals("test", str(instance))

    def test_stakeholders_str(self):
        Stakeholders.objects.create(stakeholder_identifier='test')
        instance = Stakeholders.objects.get()
        self.assertEquals("test", str(instance))
