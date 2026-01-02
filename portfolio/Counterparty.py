# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
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


class Counterparty(models.Model):
    """
    The Counterparty model holds data for a generic Counteparty to an EECS Contract. Can be a buyer or seller.

    """

    # IDENTITY

    counterparty_identifier = models.IntegerField(null=True, blank=True,
                                                  help_text='Unique Internal Integer Identifier')

    counterparty_legal_entity_identifier = models.CharField(max_length=200, blank=True, null=True,
                                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    name_of_counterparty = models.CharField(max_length=200, null=True, blank=True,
                                            help_text='Full Name of Counterparty')

    # LINKS

    # EECS REGISTRY

    eecs_account_no = models.CharField(max_length=40, null=True, blank=True,
                                       help_text='EECS Account No. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    eecs_registration_database = models.CharField(max_length=40, null=True, blank=True,
                                                  help_text='EECS Registration Database. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EECS_Registration_Database">Documentation</a>')

    eecs_registry_operator = models.CharField(max_length=40, null=True, blank=True,
                                              help_text='EECS Registry Operator. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # ADDRESS

    address = models.CharField(max_length=40, null=True, blank=True,
                               help_text='Street Address <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    postal_code = models.CharField(max_length=20, null=True, blank=True,
                                   help_text='The Postal Code <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    town = models.CharField(max_length=20, null=True, blank=True,
                            help_text='Town / City Name. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    region = models.CharField(max_length=10, null=True, blank=True,
                              help_text='NUTS Code of Region where counterparty is registered.')

    country = models.CharField(max_length=40, null=True, blank=True,
                               help_text='Country Name. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # CONTACT INFORMATION (PERSON)

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

    # Bank Account Information

    bank_name = models.CharField(max_length=40, null=True, blank=True,
                                 help_text='Bank Name. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    bank_account_no = models.CharField(max_length=40, null=True, blank=True,
                                       help_text='Bank Account No. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    bic_swift_code = models.CharField(max_length=40, null=True, blank=True,
                                      help_text='BIC-/Swift-code. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    iban = models.CharField(max_length=40, null=True, blank=True,
                            help_text='IBAN. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    vat_registration_no = models.CharField(max_length=40, null=True, blank=True,
                                           help_text='VAT Registration No. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.counterparty_identifier)

    def get_absolute_url(self):
        return reverse('portfolio:counterparty_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Counterparty"
        verbose_name_plural = "Counterparties"
