# Copyright (c) 2021 Open Risk (https://www.openriskmanagement.com)
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
from portfolio.model_choices import *
from django.urls import reverse


class Stakeholders(models.Model):
    """
    The stakeholders model holds data documenting project stakeholders and the relevant social / political environment. These data aim to support compliance assessment according to Equator Principles and political risk analysis

    """

    compliance_with_standards = models.TextField(blank=True, null=True,
                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    environmental_and_social_assessment = models.TextField(blank=True, null=True,
                                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    environmental_and_social_management_system = models.TextField(blank=True, null=True,
                                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    force_majeure_risk = models.IntegerField(blank=True, null=True, choices=FORCE_MAJEURE_RISK_CHOICES,
                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    government_support = models.IntegerField(blank=True, null=True, choices=GOVERNMENT_SUPPORT_CHOICES,
                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    grievance_mechanisms = models.TextField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    legal_and_regulatory_risk = models.IntegerField(blank=True, null=True, choices=LEGAL_AND_REGULATORY_RISK_CHOICES,
                                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    political_and_legal_environment = models.FloatField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    political_risk = models.IntegerField(blank=True, null=True, choices=POLITICAL_RISK_CHOICES,
                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    project_approval_risk = models.IntegerField(blank=True, null=True, choices=PROJECT_APPROVAL_RISK_CHOICES,
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
        return self.stakeholders_group

    def get_absolute_url(self):
        return reverse('portfolio:Stakeholders_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Stakeholder"
        verbose_name_plural = "Stakeholders"
