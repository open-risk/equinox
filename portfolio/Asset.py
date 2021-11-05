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
from django.contrib.gis.db.models import PointField, PolygonField
from django.urls import reverse
from datetime import datetime


class Asset(models.Model):
    """
    The Asset model holds asset specific data for each real asset (plant, infrastructure etc) that is being financed


    """

    #
    # GHG Data
    #

    asset_ghg_emissions = models.FloatField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    #
    # Geographic Data
    #
    asset_basin_of_influence = PolygonField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    asset_perimeter = PolygonField(blank=True, null=True,
                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # Financial Data
    #

    activation_of_guarantee = models.BooleanField(blank=True, null=True,
                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    address_of_registered_location = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    asset_class = models.IntegerField(blank=True, null=True, choices=ASSET_CLASS_CHOICES,
                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    asset_identifier = models.TextField(blank=True, null=True,
                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')



    asset_purchase_obligation = models.BooleanField(blank=True, null=True,
                                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    business_description = models.TextField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    city_of_registered_location = models.TextField(blank=True, null=True,
                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    collateral_insurance = models.BooleanField(blank=True, null=True,
                                               help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    collateral_insurance_coverage_amount = models.FloatField(blank=True, null=True,
                                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    collateral_insurance_provider = models.TextField(blank=True, null=True,
                                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    collateral_type = models.IntegerField(blank=True, null=True, choices=COLLATERAL_TYPE_CHOICES,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    configuration = models.TextField(blank=True, null=True,
                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    country_of_registered_location = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    currency_of_collateral = models.TextField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_country_of_registration = models.TextField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_opex_and_overheads = models.FloatField(blank=True, null=True,
                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    date_of_initial_valuation = models.DateField(blank=True, null=True,
                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    date_of_latest_valuation = models.DateField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    date_of_the_latest_residual_valuation = models.DateField(blank=True, null=True,
                                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    description = models.TextField(blank=True, null=True,
                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    design_and_technology_risk = models.IntegerField(blank=True, null=True, choices=DESIGN_AND_TECHNOLOGY_RISK_CHOICES,
                                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    engine_size = models.FloatField(blank=True, null=True,
                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    estimated_useful_life = models.FloatField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    geographic_region_classification = models.TextField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    geographic_region_of_registered_location = models.TextField(blank=True, null=True,
                                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    guarantee_amount = models.FloatField(blank=True, null=True,
                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    industry_segment = models.TextField(blank=True, null=True,
                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    initial_residual_valuation_date = models.DateField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    initial_residual_value = models.FloatField(blank=True, null=True,
                                               help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    initial_valuation_amount = models.FloatField(blank=True, null=True,
                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    latest_residual_value = models.FloatField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    latest_valuation_amount = models.FloatField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    legal_owner = models.TextField(blank=True, null=True,
                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    manufacturer_of_collateral = models.TextField(blank=True, null=True,
                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    name_or_model_of_collateral = models.TextField(blank=True, null=True,
                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    new_or_used = models.IntegerField(blank=True, null=True, choices=NEW_OR_USED_CHOICES,
                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    option_to_buy_price = models.FloatField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_country_of_registration = models.TextField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    postcode_of_registered_location = models.TextField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    project_characteristics = models.FloatField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    registration_number = models.TextField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    type_of_initial_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_INITIAL_VALUATION_CHOICES,
                                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    type_of_latest_valuation = models.IntegerField(blank=True, null=True, choices=TYPE_OF_LATEST_VALUATION_CHOICES,
                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    type_of_legal_owner = models.IntegerField(blank=True, null=True, choices=TYPE_OF_LEGAL_OWNER_CHOICES,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    year_of_manufacture = models.DateField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    year_of_registration = models.DateField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.asset_identifier

    def get_absolute_url(self):
        return reverse('portfolio:Asset_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Project Asset"
        verbose_name_plural = "Project Assets"
