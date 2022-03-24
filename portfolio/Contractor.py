# Copyright (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)
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
    The Contractor model holds data for each Contractor involved in the construction of the Project or the fulfillment of a Procurement contract

    Is a type of Counterparty

    The Contractor data fields cover
    - identity, type, address
    - links to contracts and buyers
    - EBA scorecard fields

    """


    # IDENTITY

    contractor_identifier = models.CharField(max_length=80, null=True,
                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    contractor_legal_entity_identifier = models.TextField(blank=True, null=True,
                                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    name_of_contractor = models.TextField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    is_sme = models.BooleanField(blank=True, null=True, help_text="Whether the entity is an SME or not")

    # ADDRESS

    address = models.CharField(max_length=40, null=True, blank=True,
                               help_text='Street Address <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    postal_code = models.CharField(max_length=20, null=True, blank=True,
                                   help_text='The Postal Code <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    town = models.CharField(max_length=20, null=True, blank=True,
                            help_text='Town / City Name. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    region = models.CharField(max_length=10, null=True, blank=True,
                              help_text='NUTS Code of Region. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    country = models.CharField(max_length=20, null=True, blank=True,
                               help_text='Country Name. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # CONTACT

    phone = models.CharField(max_length=20, null=True, blank=True,
                             help_text='Phone Number <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    fax = models.CharField(max_length=20, null=True, blank=True,
                           help_text='Fax Number <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    email = models.CharField(max_length=20, null=True, blank=True,
                             help_text='Email Address <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    contact_point = models.CharField(max_length=10, null=True, blank=True,
                                     help_text='Contact Point. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    website = models.CharField(max_length=40, null=True, blank=True,
                               help_text='Website URL. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # LINKS

    project_company = models.ForeignKey('ProjectCompany', blank=True, null=True, on_delete=models.CASCADE, help_text="Project Company that sourced this contractor")

    # SCORECARD

    permitting_and_siting = models.IntegerField(blank=True, null=True, choices=PERMITTING_AND_SITING_CHOICES,
                                                help_text='Risk SubFactor. EBA 3.2.1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    completion_guarantees_and_liquidated_damages = models.IntegerField(blank=True, null=True,
                                                                       choices=COMPLETION_GUARANTEES_AND_LIQUIDATED_DAMAGES_CHOICES,
                                                                       help_text='Risk SubFactor. EBA 3.2.4. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    type_of_construction_contract = models.IntegerField(blank=True, null=True,
                                                        choices=TYPE_OF_CONSTRUCTION_CONTRACT_CHOICES,
                                                        help_text='Risk SubFactor. EBA 3.2.2. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    contractor_track_record = models.IntegerField(blank=True, null=True, choices=CONTRACTOR_TRACK_RECORD_CHOICES,
                                                  help_text='Risk SubFactor. EBA 3.2.5. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    # OTHER

    completion_guarantees = models.BooleanField(blank=True, null=True,
                                                help_text='Whether there are completion guarantees for the contract. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    liquidated_damages = models.BooleanField(blank=True, null=True,
                                             help_text='Whether there are liquidated damages for the contract. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')





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
