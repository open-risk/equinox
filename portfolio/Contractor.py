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


class Contractor(models.Model):
    """
    The Contractor model holds data for each for each Contractor involved in the construction of the project being financed


    """

    completion_guarantees = models.BooleanField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    completion_guarantees_and_liquidated_damages = models.IntegerField(blank=True, null=True,
                                                                       choices=COMPLETION_GUARANTEES_AND_LIQUIDATED_DAMAGES_CHOICES,
                                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    completion_risk = models.IntegerField(blank=True, null=True, choices=COMPLETION_RISK_CHOICES,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    construction_risk = models.FloatField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    contractor_identifier = models.TextField(blank=True, null=True,
                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    contractor_legal_entity_identifier = models.TextField(blank=True, null=True,
                                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    contractor_track_record = models.IntegerField(blank=True, null=True, choices=CONTRACTOR_TRACK_RECORD_CHOICES,
                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    liquidated_damages = models.BooleanField(blank=True, null=True,
                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    name_of_contractor = models.TextField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    permitting_and_siting = models.IntegerField(blank=True, null=True, choices=PERMITTING_AND_SITING_CHOICES,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    type_of_construction_contract = models.IntegerField(blank=True, null=True,
                                                        choices=TYPE_OF_CONSTRUCTION_CONTRACT_CHOICES,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contractor_identifier

    def get_absolute_url(self):
        return reverse('portfolio:Contractor_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Contractor"
        verbose_name_plural = "Contractors"
