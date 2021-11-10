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


class Sponsor(models.Model):
    """
    The Sponsor model holds data about the entity that principally supports the Project. Depending on context it may be the only or largest shareholder, a guarantor or similar.


    """

    # IDENTITY
    sponsor_identifier = models.CharField(max_length=80, blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    sponsor_legal_entity_identifier = models.TextField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    registration_number = models.TextField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # LINKS
    project_company = models.ForeignKey('ProjectCompany', blank=True, null=True, on_delete=models.CASCADE,
                                        help_text="Project Company that is Sponsored by this Sponsor")

    # SCORECARD

    sponsor_support = models.IntegerField(blank=True, null=True, choices=SPONSOR_SUPPORT_CHOICES,
                                          help_text='Risk Factor. EBA 4.3. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    sponsor_track_record = models.IntegerField(blank=True, null=True, choices=SPONSOR_TRACK_RECORD_CHOICES,
                                               help_text='Risk Factor. EBA 4.2. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    sponsor_financial_strength = models.IntegerField(blank=True, null=True, choices=SPONSOR_FINANCIAL_STRENGTH_CHOICES,
                                                     help_text='Risk Factor. EBA 4.1. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    # OTHER

    strength_of_sponsor = models.FloatField(blank=True, null=True,
                                            help_text='Risk Factor Group <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    address_of_registered_location = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    annual_ebit = models.FloatField(blank=True, null=True,
                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    annual_revenue = models.FloatField(blank=True, null=True,
                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    basis_of_financial_statements = models.IntegerField(blank=True, null=True,
                                                        choices=BASIS_OF_FINANCIAL_STATEMENTS_CHOICES,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    business_description = models.TextField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    cash_and_cash_equivalent_items = models.FloatField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    city_of_registered_location = models.TextField(blank=True, null=True,
                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    country_of_registered_location = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    currency_of_financial_statements = models.TextField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_assets = models.FloatField(blank=True, null=True,
                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_external_credit_rating = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_internal_credit_rating = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    date_of_incorporation = models.DateField(blank=True, null=True,
                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    date_of_latest_annual_financial_statements = models.DateField(blank=True, null=True,
                                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    external_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    financial_statements_type = models.IntegerField(blank=True, null=True, choices=FINANCIAL_STATEMENTS_TYPE_CHOICES,
                                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    financials_audited = models.BooleanField(blank=True, null=True,
                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    fixed_assets = models.FloatField(blank=True, null=True,
                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    geographic_region_classification = models.TextField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    geographic_region_of_registered_location = models.TextField(blank=True, null=True,
                                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    industry_segment = models.TextField(blank=True, null=True,
                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    internal_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    market_capitalisation = models.FloatField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    name_of_project = models.TextField(blank=True, null=True,
                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    net_assets = models.FloatField(blank=True, null=True,
                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    number_of_fte = models.FloatField(blank=True, null=True,
                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    number_of_joint_counterparties = models.FloatField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    postcode_of_registered_location = models.TextField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    source_of_current_external_credit_rating = models.TextField(blank=True, null=True,
                                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    source_of_external_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')






    total_assets = models.FloatField(blank=True, null=True,
                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    total_debt = models.FloatField(blank=True, null=True,
                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    total_liabilities = models.FloatField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    guarantee_amount = models.FloatField(blank=True, null=True,
                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sponsor_identifier

    def get_absolute_url(self):
        return reverse('portfolio:Sponsor_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"
