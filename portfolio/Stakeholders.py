# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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


class Stakeholders(models.Model):
    """
    The Stakeholders model holds data documenting project stakeholders and the relevant social / political environment in which a Project is pursued.

    These data aim to support compliance assessment according to Equator Principles and political risk analysis

    """
    # IDENTITY

    stakeholder_identifier = models.CharField(max_length=80, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # LINKS

    project_company = models.ForeignKey('ProjectCompany', blank=True, null=True, on_delete=models.CASCADE)

    # SCORECARD

    political_and_legal_environment = models.FloatField(blank=True, null=True,
                                                        help_text='Risk Factor Group. EBA 2. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Political_and_Legal_Environment">Documentation</a>')

    legal_and_regulatory_risk = models.IntegerField(blank=True, null=True, choices=LEGAL_AND_REGULATORY_RISK_CHOICES,
                                                    help_text='Risk Factor. EBA 2.4. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    political_risk = models.IntegerField(blank=True, null=True, choices=POLITICAL_RISK_CHOICES,
                                         help_text='Risk Factor. EBA 2.1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Political_Risk">Documentation</a>')

    project_approval_risk = models.IntegerField(blank=True, null=True, choices=PROJECT_APPROVAL_RISK_CHOICES,
                                                help_text='Risk Factor. EBA 2.5. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Project_Risk">Documentation</a>')

    force_majeure_risk = models.IntegerField(blank=True, null=True, choices=FORCE_MAJEURE_RISK_CHOICES,
                                             help_text='Risk Factor. EBA 2.2. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Force_Majeure_Risk">Documentation</a>')

    government_support = models.IntegerField(blank=True, null=True, choices=GOVERNMENT_SUPPORT_CHOICES,
                                             help_text='Risk Factor. EBA 2.3. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Government_Guaranty">Documentation</a>')

    legal_regime = models.IntegerField(blank=True, null=True, choices=LEGAL_REGIME_CHOICES,
                                       help_text='Risk Factor. EBA 2.6. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/Legal_Basis">Documentation</a>')

    # OTHER

    compliance_with_standards = models.TextField(blank=True, null=True,
                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    environmental_and_social_assessment = models.TextField(blank=True, null=True,
                                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    environmental_and_social_management_system = models.TextField(blank=True, null=True,
                                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    grievance_mechanisms = models.TextField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    stakeholder_engagement = models.TextField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    stakeholders_group = models.TextField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stakeholder_identifier

    def get_absolute_url(self):
        return reverse('portfolio:Stakeholders_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Stakeholder"
        verbose_name_plural = "Stakeholders"
