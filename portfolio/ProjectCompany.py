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


from django.db import models
from django.urls import reverse

from portfolio.model_choices import *


class ProjectCompany(models.Model):
    """
    The Project Company model holds data for a large sustainability oriented Project (Project Finance) involving a special purpose entity. A Project Company always refers to a Project but a Project may not involve a special purpose company


    """

    # IDENTIFICATION

    project_company_identifier = models.CharField(max_length=80, blank=True, null=True,
                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    project_company_lei = models.CharField(max_length=80, blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # LINKS

    project = models.ForeignKey('Project', blank=True, null=True, on_delete=models.CASCADE,
                                help_text="The Project Company who's revenue is documented")

    # SCORECARD

    financial_ratios = models.IntegerField(blank=True, null=True, choices=FINANCIAL_RATIOS_CHOICES,
                                           help_text='Risk Factor. EBA 1.2. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Financial_Ratios">Documentation</a>')

    refinancing_risk = models.IntegerField(blank=True, null=True, choices=REFINANCING_RISK_CHOICES,
                                           help_text='Risk Subfactor. EBA 1.4.1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Refinancing_Risk">Documentation</a>')

    control_over_cash_flow = models.IntegerField(blank=True, null=True, choices=CONTROL_OVER_CASH_FLOW_CHOICES,
                                                 help_text='Risk Factor. EBA 5.3.  <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    covenant_package = models.IntegerField(blank=True, null=True, choices=COVENANT_PACKAGE_CHOICES,
                                           help_text='Risk Factor. EBA 5.4. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    reserve_funds = models.IntegerField(blank=True, null=True, choices=RESERVE_FUNDS_CHOICES,
                                        help_text='Risk Factor. EBA 5.5. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    pledge_of_assets = models.IntegerField(blank=True, null=True, choices=PLEDGE_OF_ASSETS_CHOICES,
                                           help_text='Risk Factor. EBA 5.2. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    assignment_of_contracts_and_accounts = models.IntegerField(blank=True, null=True,
                                                               choices=ASSIGNMENT_OF_CONTRACTS_AND_ACCOUNTS_CHOICES,
                                                               help_text='Risk Factor. EBA 5.1.  <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # OTHER

    financial_strength = models.FloatField(blank=True, null=True,
                                           help_text='Risk Factor Group. EBA 1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Financial_Strength">Documentation</a>')

    cash_sweep = models.BooleanField(blank=True, null=True,
                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    covenants = models.TextField(blank=True, null=True,
                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    debt_service_coverage_ratio = models.FloatField(blank=True, null=True,
                                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    debttoequity_ratio = models.FloatField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    dividend_restrictions = models.BooleanField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    financial_structure = models.FloatField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    impact_category = models.IntegerField(blank=True, null=True, choices=IMPACT_CATEGORY_CHOICES,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    independent_escrow_account = models.BooleanField(blank=True, null=True,
                                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    independent_monitoring_and_reporting = models.TextField(blank=True, null=True,
                                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    independent_review = models.TextField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    interest_coverage_ratio = models.FloatField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    legal_type_of_project = models.IntegerField(blank=True, null=True, choices=LEGAL_TYPE_OF_PROJECT_CHOICES,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    loan_life_coverage_ratio = models.FloatField(blank=True, null=True,
                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    mandatory_prepayments = models.BooleanField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    name_of_project = models.TextField(blank=True, null=True,
                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    payment_cascade = models.BooleanField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    payment_deferrals = models.BooleanField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    life_coverage_ratio = models.FloatField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    reporting_and_transparency = models.TextField(blank=True, null=True,
                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    security_package = models.FloatField(blank=True, null=True,
                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_company_identifier

    def get_absolute_url(self):
        return reverse('portfolio:ProjectCompany_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Project Company"
        verbose_name_plural = "Project Companies"
