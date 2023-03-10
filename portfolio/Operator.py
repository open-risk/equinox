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
from portfolio.model_choices import *
from django.urls import reverse


class Operator(models.Model):
    """
    The Operator model holds data for each Operator involved in the operation of a Project


    """

    # IDENTITY

    operator_identifier = models.CharField(max_length=80, blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    operator_lei = models.TextField(blank=True, null=True,
                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # LINKS
    project_company = models.ForeignKey('ProjectCompany', blank=True, null=True, on_delete=models.CASCADE, help_text="The Project Company that contracted this Operator")

    # SCORECARD

    o_and_m_contract = models.IntegerField(blank=True, null=True, choices=O_AND_M_CONTRACT_CHOICES,
                                           help_text='Risk SubFactor. EBA 3.3.1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    operator_track_record = models.IntegerField(blank=True, null=True, choices=OPERATOR_TRACK_RECORD_CHOICES,
                                                help_text='Risk SubFactor. EBA 3.3.2. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    # OTHER
    operating_risk = models.FloatField(blank=True, null=True,
                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')



    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.operator_identifier

    def get_absolute_url(self):
        return reverse('portfolio:Operator_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Operator"
        verbose_name_plural = "Operators"
