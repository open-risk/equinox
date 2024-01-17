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

from django.db import models
from django.urls import reverse

from portfolio.model_choices import *


class Revenue(models.Model):
    """
    The Revenue model holds data to facilitate revenue risk analysis of Project that is being financed


    """

    revenue_group_identifier = models.TextField(
        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # LINKS

    project_company = models.ForeignKey('ProjectCompany', blank=True, null=True, on_delete=models.CASCADE,
                                        help_text="The Project Company who's revenue is documented")

    # SCORECARD

    market_conditions = models.IntegerField(blank=True, null=True, choices=MARKET_CONDITIONS_CHOICES,
                                            help_text='Risk Factor. EBA 1.1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Market_Conditions">Documentation</a>')

    stress_analysis = models.IntegerField(blank=True, null=True, choices=STRESS_ANALYSIS_CHOICES,
                                          help_text='Risk Factor. EBA 1.3. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Scenario_Analysis">Documentation</a>')

    revenue_contract_robustness = models.IntegerField(blank=True, null=True,
                                                      choices=REVENUE_CONTRACT_ROBUSTNESS_CHOICES,
                                                      help_text='Risk SubFactor. EBA 3.4.1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    offtake_contract_case = models.IntegerField(blank=True, null=True, choices=OFFTAKE_CONTRACT_CASE_CHOICES,
                                                help_text='Risk SubFactor. EBA 3.4.2. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    no_offtake_contract_case = models.IntegerField(blank=True, null=True, choices=NO_OFFTAKE_CONTRACT_CASE_CHOICES,
                                                   help_text='Risk SubFactor. EBA 3.4.3. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    supply_cost_risks = models.IntegerField(blank=True, null=True, choices=SUPPLY_COST_RISKS_CHOICES,
                                            help_text='Risk SubFactor. EBA 3.5.1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    reserve_risk = models.IntegerField(blank=True, null=True, choices=RESERVE_RISK_CHOICES,
                                       help_text='Risk SubFactor. EBA 3.5.2. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # OTHER

    price_risk = models.FloatField(blank=True, null=True,
                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    revenue_assessment = models.FloatField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    supplier_track_record = models.FloatField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    supply_risk = models.FloatField(blank=True, null=True,
                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    transportation_risk = models.FloatField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    volume_risk = models.FloatField(blank=True, null=True,
                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.revenue_group_identifier

    def get_absolute_url(self):
        return reverse('portfolio:Revenue_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Revenue"
        verbose_name_plural = "Revenue"
