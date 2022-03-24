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
from django.urls import reverse


class PortfolioManager(models.Model):
    """
    The PortfolioManager model holds data for each Portfolio Manager that is using an equinox instance. A Portfolio Manger may be a Loan Portfolio manager a Procurement contracts portfolio manager etc

    All Portfolios must belong to one (and only one) Portfolio Manager

    The PM datafields cover identity, address, contact information and ad-hoc other

    """

    # IDENTITY

    manager_identifier = models.CharField(max_length=20, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    manager_legal_entity_identifier = models.CharField(max_length=20, blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    name_of_manager = models.CharField(max_length=40, blank=True, null=True,
                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

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

    # OTHER

    pm_website = models.CharField(max_length=40, null=True, blank=True,
                                  help_text='Specific Website URL. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.manager_identifier

    def get_absolute_url(self):
        return reverse('portfolio:PortfolioManager_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio Manager"
        verbose_name_plural = "Portfolio Managers"
