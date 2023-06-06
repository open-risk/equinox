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
from portfolio.Counterparty import Counterparty
from portfolio.Asset import PowerPlant

class Certificate(models.Model):
    """
    The Certificate model holds data for each individual Energy Certificate in the Portfolio


    """

    # IDENTIFICATION
    certificate_identifier = models.CharField(max_length=80, blank=True, null=True,
                                       help_text='Unique EECS Certificate Number.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Certficate_Number">Documentation</a>')

    # LINKS
    seller = models.ForeignKey('Counterparty', blank=True, null=True, on_delete=models.CASCADE, related_name='Seller', help_text='EECS Account Holder (Certificate Seller). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Account_Holder">Documentation</a>')

    buyer = models.ForeignKey('Counterparty', blank=True, null=True, on_delete=models.CASCADE, related_name='Buyer', help_text='EECS Account Holder (Certificate Buyer). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Account_Holder">Documentation</a>')

    production_device = models.ForeignKey('PowerPlant', blank=True, null=True, on_delete=models.CASCADE, help_text='EECS Production Device. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Production_Device">Documentation</a>')

    # CERTIFICATE DATA

    # production period
    production_start = models.DateField(blank=True, null=True, help_text='EECS Production Period Start. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Production_Period">Documentation</a>')

    production_end = models.DateField(blank=True, null=True, help_text='EECS Production Period End. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Production_Period">Documentation</a>')

    # technology
    technology_code = models.CharField(max_length=80, blank=True, null=True,
                                       help_text='EECS Technology Code. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Technology_Code">Documentation</a>')

    # delivery date
    delivery_date = models.DateField(blank=True, null=True, help_text='EECS Delivery Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Delivery_Date">Documentation</a>')

    # quantity
    contract_quantity = models.IntegerField(default=1, blank=True, null=True,
                                       help_text='EECS Contract Quantity. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Contract_Quantity">Documentation</a>')

    # contract price

    contract_price = models.FloatField(blank=True, null=True,
                                       help_text='EECS Contract Price. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Contract_Price">Documentation</a>')

    # EECS DOMAIN

    production_country = models.CharField(max_length=80, blank=True, null=True,
                                        help_text='Country / Countries of Production. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Production_Country">Documentation</a>')

    production_issuing_body = models.CharField(max_length=80, blank=True, null=True,
                                        help_text='Authorised Issuing Body of the Country / Countries of Production. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Issuing_Body">Documentation</a>')

    delivery_country = models.CharField(max_length=80, blank=True, null=True,
                                        help_text='Country of Delivery')

    deliver_issuing_body = models.CharField(max_length=80, blank=True, null=True,
                                        help_text='Authorised Issuing Body of Country of Delivery. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Issuing_Body">Documentation</a>')


    # OTHER


    support_type = models.CharField(max_length=40, blank=True, null=True,
                                        help_text='Type of support (no support, production support, etc.)')


    ics = models.CharField(max_length=40, blank=True, null=True,
                                        help_text='Independent Criteria Scheme')


    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.certificate_identifier

    def get_absolute_url(self):
        return reverse('portfolio:certificate_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
