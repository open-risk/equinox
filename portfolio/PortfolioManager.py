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


class PortfolioManager(models.Model):
    """
    The PortfolioManager model holds static reference data for each Portfolio Manager that is using (or is represented) in an equinox instance. A Portfolio Manager may be a Loan Portfolio manager in a Bank, a Procurement contracts portfolio manager in a Public Authority, a Project Finance manager etc

    All Portfolios belong to one (and only one) Portfolio Manager

    The PM data fields cover identity, address, contact information and ad-hoc other details

    """

    # LEGAL IDENTITY

    name_of_manager = models.CharField(max_length=200, blank=True, null=True,
                                       help_text='Full name of entity (portfolio manager)')

    manager_identifier = models.IntegerField(blank=True, null=True,
                                             help_text='Unique (integer) internal identifier of the entity')

    manager_legal_entity_identifier = models.CharField(max_length=40, blank=True, null=True,
                                                       help_text='Legal Entity Identifier. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # ENTITY NATURE

    entity_type = models.CharField(max_length=40, null=True, blank=True,
                                   help_text='The type of the entity, e.g. from an applicable category list')

    entity_activity = models.CharField(max_length=80, null=True, blank=True,
                                       help_text='The main activity the entity, e.g. from an applicable category list')

    # ADDRESS INFORMATION OF AN ENTITY'S LEGAL ADDRESS

    address = models.CharField(max_length=200, null=True, blank=True,
                               help_text='Street Address of the entity headquarters / legal address <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    postal_code = models.CharField(max_length=20, null=True, blank=True,
                                   help_text='The Postal Code of the entity legal address <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    town = models.CharField(max_length=40, null=True, blank=True,
                            help_text='The Town / City Name of the entitys legal address. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    region = models.CharField(max_length=40, null=True, blank=True,
                              help_text='The NUTS Code of region of the entitys address. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    country = models.CharField(max_length=40, null=True, blank=True,
                               help_text='The Country Name of the entity legal address. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # ENTITY CONTACT INFORMATION

    phone = models.CharField(max_length=100, null=True, blank=True,
                             help_text='Phone Number <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    fax = models.CharField(max_length=100, null=True, blank=True,
                           help_text='Fax Number <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    email = models.CharField(max_length=200, null=True, blank=True,
                             help_text='Email Address <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    contact_point = models.CharField(max_length=100, null=True, blank=True,
                                     help_text='Contact Point. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    website = models.CharField(max_length=200, null=True, blank=True,
                               help_text='Website URL. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    # OTHER AUXILIARY INFORMATION

    pm_website = models.CharField(max_length=200, null=True, blank=True,
                                  help_text='Specific Website URL. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_manager

    def get_absolute_url(self):
        return reverse('portfolio:PortfolioManager_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio Manager"
        verbose_name_plural = "Portfolio Managers"
